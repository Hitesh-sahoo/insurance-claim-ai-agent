# 🧠 Autonomous Insurance Claims Processing Agent

## 📌 Overview

This project is a lightweight AI-based system that processes insurance claim documents (FNOL - First Notice of Loss) and automates key steps in the claims workflow.

The system extracts important information from PDF documents, identifies missing fields, and routes the claim to the appropriate processing pipeline based on predefined business rules.

---

## 🚀 Features

* 📄 Extracts key fields from insurance claim PDFs
* ⚠️ Detects missing or incomplete information
* 🧠 Applies intelligent rule-based routing
* 💬 Generates reasoning for each decision
* 🌐 Interactive UI using Streamlit

---

## 🏗️ System Workflow

1. Upload FNOL PDF
2. Extract text using `pdfplumber`
3. Parse important fields using regex
4. Validate required fields
5. Apply routing logic:

   * Fast-track
   * Manual Review
   * Investigation
   * Specialist Queue
6. Generate explanation
7. Output structured JSON

---

## 📊 Extracted Fields

* Policy Number
* Claim Type
* Estimated Damage
* Date of Loss
* Description
* Location (if available)

---

## 🔁 Routing Rules

* 💸 Damage < 25,000 → Fast-track
* ❌ Missing required fields → Manual Review
* 🚨 Fraud-related keywords → Investigation
* 🏥 Injury claims → Specialist Queue

---

## 🛠️ Tech Stack

* Python
* pdfplumber (PDF processing)
* Regex (data extraction)
* Streamlit (UI)

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your_repo_link>
cd insurance-claim-ai-agent
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

---

## 📌 Sample Output

```json
{
  "extractedFields": {...},
  "missingFields": [...],
  "recommendedRoute": "Manual Review",
  "reasoning": "Missing required fields"
}
```

---

## ⚠️ Challenges & Approach

Insurance documents like ACORD forms are semi-structured and contain repeated labels, making extraction difficult.

To handle this:

* Implemented flexible regex patterns
* Added filtering logic to avoid incorrect matches
* Designed fallback mechanisms for missing data
* Ensured robust routing even with incomplete inputs

---

## 🔮 Future Improvements

* Integrate LLM for better extraction accuracy
* Support multiple document formats
* Add confidence scoring
* Deploy as a web service

---

## 👨‍💻 Author

Hitesh Kumar

---
