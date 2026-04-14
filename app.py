from flask import Flask, request, jsonify, send_from_directory
import pandas as pd
import fitz  # PyMuPDF
import re
import os

app = Flask(__name__, static_folder=".")

# -------- TEXT EXTRACT (PDF) --------
def extract_text_pdf(file_storage):
    pdf_bytes = file_storage.read()
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# -------- EXTRACT IP + HOSTNAME --------
def extract_entities(text):
    ips = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', text)
    hosts = re.findall(r'\b[A-Z]{2,}-\d+\b', text.upper())
    return list(set(ips + hosts))

# -------- LOAD CMDB --------
def load_cmdb(file_storage):
    df = pd.read_excel(file_storage)
    search_map = {}
    for idx, row in df.iterrows():
        row_number = idx + 2
        for cell in row:
            if pd.notna(cell):
                value = str(cell).strip().upper()
                if value:
                    search_map[value] = row_number
    return search_map

# -------- IN-MEMORY STORE --------
cmdb_store = {}

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/upload-cmdb", methods=["POST"])
def upload_cmdb():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file"}), 400
    try:
        cmdb_store["map"] = load_cmdb(file)
        return jsonify({"message": "CMDB loaded", "entries": len(cmdb_store["map"])})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/validate-pdf", methods=["POST"])
def validate_pdf():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No PDF"}), 400
    if "map" not in cmdb_store:
        return jsonify({"error": "Load CMDB first"}), 400
    try:
        text = extract_text_pdf(file)
        entities = extract_entities(text)
        results = []
        for item in entities:
            key = item.strip().upper()
            if key in cmdb_store["map"]:
                results.append({"entity": item, "status": "found", "row": cmdb_store["map"][key]})
            else:
                results.append({"entity": item, "status": "not_found", "row": None})
        return jsonify({"entities": results})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/search", methods=["POST"])
def search():
    data = request.json
    query = data.get("query", "").strip().upper()
    if "map" not in cmdb_store:
        return jsonify({"error": "Load CMDB first"}), 400
    if query in cmdb_store["map"]:
        return jsonify({"status": "found", "row": cmdb_store["map"][query]})
    return jsonify({"status": "not_found"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)