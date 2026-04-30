# Automated Economic Classification & Risk Scoring of Nigerian Government Payment Reports

Machine learning system for classifying and analyzing Nigerian government payment transactions from the Open Treasury Portal between 2020 and 2025.

---

## Overview

Nigeria’s Open Treasury Portal publishes payments daily, but the data is:

* Fragmented across files
* Unstructured (free-text descriptions)
* Difficult to analyze at scale

This project solves that by:

* Automatically classifying payment descriptions into NCOA economic categories
* Scoring each transaction for observable risk indicators to flag potentially suspicious transactions
* Integrating results into an interactive Power BI dashboard for expenditure analysis 

---

## Dataset

**Source:** [Nigeria Open Treasury Portal](www.opentreasury.gov.ng)

Each transaction includes:

* Payment Number
* Organization (MDA)
* Beneficiary Name
* Description
* Amount
* Date

---

## Methodology

### 1. Data Collection

* Automated scraping of daily payment reports using Python
* Consolidation into a unified dataset

### 2. Data Preprocessing

* Text cleaning and normalization

* Beneficiary classification:

  * Contractor
  * Individual
  * MDA
  * Unknown

* Feature engineering:

  * Date variables (year, month)
  * MDA mapping
  * COFOG classification

---

### 3. Text Classification

Payment descriptions were transformed using:

* **TF-IDF Vectorization**

Models used:

* Logistic Regression
* Support Vector Machine (SVM)

**Best Model:** SVM

* Achieved **94% accuracy**

---

### 4. Risk Scoring Model

Developed using transaction-level indicators:

* Duplicate payments
* Missing descriptions
* Unknown beneficiaries
* Contractor registration status (via CAC lookup)

Transactions are assigned risk flags to highlight those requiring further review.

---

### 5. Dashboard Integration

Results were deployed into a **Power BI dashboard** featuring:

* Expenditure trends over time
* MDA-level analysis
* Contractor analysis
* Risk exploration tools
* Transaction-level drilldowns

---

## Key Results

* Successfully automated classification of unstructured government payment data
* Achieved **high classification accuracy (94%) using SVM**
* Developed a scalable **risk identification framework**
* Enabled interactive exploration of federal expenditure patterns

---

## Dashboard Preview

* Risk flag distribution
* Contractor insights

**Summary Page. Treemap chart can be drilled down to individual agencies, and then further to explore payment types and classification**
<img width="1426" height="799" alt="image" src="https://github.com/user-attachments/assets/aef657a1-d511-4963-a4be-9508fe504830" />

**Functional Trends by Year and MDA**
<img width="1409" height="799" alt="image" src="https://github.com/user-attachments/assets/4983a91c-bd49-41cc-866c-595de3909008" />

**MDA Analysis Page**
<img width="1412" height="793" alt="image" src="https://github.com/user-attachments/assets/4914be13-43c4-4521-b6e6-1110e229de7e" />

**Payment Risk Explorer**
<img width="1400" height="791" alt="image" src="https://github.com/user-attachments/assets/89a4ac7a-5db6-498f-ab70-1091de281f47" />

**Contractor Analysis Page**
<img width="1408" height="791" alt="image" src="https://github.com/user-attachments/assets/e7f6bc11-c2d6-4393-bce1-fabccfb3c889" />

**Payments into Individual Accounts**
<img width="1404" height="798" alt="image" src="https://github.com/user-attachments/assets/a1f2a5d9-bbb3-4394-93ff-666f619c50b0" />

---

## Limitations

* Model performance depends on the size and accuracy of the manually labeled data.
* Payment descriptions are inconsistently formatted and manually entered, and some descriptions span multiple economic categories, making single-label classification imperfect
* CAC verification was subject to system availability and name-spelling inconsistencies

---

## Future Improvements

* Expand the labelled dataset to improve coverage of underrepresented NCOA categories
* Explore transformer-based models (e.g. BERT) for improved classification of ambiguous descriptions
* Develop **predictive risk models** using anomaly detection
* Automate the full pipeline to process new daily payment reports as they are published
* Deploy as a web-based public tool integrated with the Open Treasury Portal

---

## How to Run

```bash
# Clone the repository
git clone https://github.com/yourusername/project-name.git

# Install dependencies
pip install -r requirements.txt

# Run notebooks or scripts
```

---

## Disclaimer

* This project uses publicly available government data.It does *not make legal claims or accusations of fraud*, and risk scores are **analytical indicators only**.

---

## Author

**Izu Ononugbo**
B.Sc. Software Engineering
Baze University, Abuja

[LinkedIn](linkedin.com/izuononugbo)

---

## Acknowledgements

* BudgIT Foundation
* Open Treasury Portal (Federal Government of Nigeria)

---
