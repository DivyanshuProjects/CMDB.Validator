# 🔥 CMDB.Validator

**CMDB.Validator** is a lightweight GRC automation tool designed to validate network diagram data (PDF) against a CMDB (Excel).
It supports both **automatic extraction** and **manual validation**, making it ideal for audit, compliance, and infrastructure verification tasks.

---

## 🚀 Features

### ✅ Auto Validation (PDF Mode)

* Extracts **IP addresses** and **hostnames** from PDF network diagrams
* Matches extracted data against CMDB (Excel)
* Displays:

  * ✅ Found (with row number)
  * ❌ Not Found

### 🔍 Manual Search Mode

* Search any **IP / Hostname / Device**
* Works like **Ctrl + F** across entire CMDB
* Shows exact **row number**

### 📊 CMDB Support

* Works with **any Excel format**
* No dependency on column names
* Searches across **entire sheet**

### 🖥️ GUI Interface

* Simple and clean UI (Tkinter)
* No command-line usage required

---

## 🧠 Use Cases

* GRC (Governance, Risk & Compliance) audits
* Network diagram validation
* CMDB verification
* Asset inventory checks
* Security compliance reviews

---

## ⚙️ Requirements

Install required libraries:

```bash id="9l3k2x"
pip install pymupdf pandas openpyxl
```

---

## ▶️ How to Run

```bash id="8mz1qp"
python main.py
```

---

## 🧪 Workflow

1. Load CMDB Excel file
2. Select network diagram PDF
3. Click **Run Auto Validation**
4. (Optional) Use **Manual Search Mode**

---
<img width="974" height="724" alt="image" src="https://github.com/user-attachments/assets/6a63e687-3530-4e13-a5c5-83fce3a90e4f" />


## 🔒 Security & Compatibility

* No external APIs
* No internet required
* Works in **restricted enterprise environments**
* No OCR or external binaries used

---

## 🚀 Future Enhancements

* Export results to Excel/PDF
* Highlight missing assets
* Drag & drop support
* Fuzzy matching (FW vs Firewall)
* EXE packaging for enterprise deployment

---

## 🤖 Development Note

This project was **developed with the assistance of AI tools ** to accelerate development, improve code quality, and explore GRC automation concepts.
All logic, customization, and use-case implementation were guided and adapted for real-world scenarios.

---

## 👨‍💻 Author

Developed as a **GRC Automation Project** for audit and compliance use cases.

---

## ⭐ Note

This tool is designed to reduce manual audit effort and improve accuracy in CMDB validation.

---

🔥 *Built for real-world infrastructure audits*
