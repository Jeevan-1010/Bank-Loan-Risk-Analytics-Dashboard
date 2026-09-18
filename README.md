# Bank Loan & Risk Analytics Dashboard

An end-to-end **Bank Loan Analysis and Risk Analytics** project using **Python, Pandas, NumPy, and Microsoft Power BI**.

The project analyzes loan applications, approval patterns, funded amounts, credit scores, income groups, loan purposes, and default risk through an interactive Power BI dashboard.

## Project Overview

The objective of this project is to transform raw bank loan data into meaningful business insights using Python for preprocessing and Power BI for analytics and visualization.

### Key Areas

* Loan application analysis
* Loan approval analysis
* Approval rate analysis
* Loan default analysis
* Credit score segmentation
* Income segmentation
* Loan amount segmentation
* Risk category analysis
* Loan purpose analysis
* State-wise loan analysis
* Time-based application trends

## Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Microsoft Power BI**
* **DAX**
* **Microsoft Excel**
* **Git & GitHub**

## Project Workflow

```text
Raw Dataset
     ↓
Python Data Preprocessing
     ↓
Feature Engineering
     ↓
Processed CSV
     ↓
Power BI Data Model
     ↓
Calendar Dimension
     ↓
DAX Measures
     ↓
Interactive Dashboard
```

## Dataset

The project uses a bank loan dataset containing information related to:

* Application Date
* Approval Date
* Disbursement Date
* Annual Income
* Credit Score
* Loan Amount
* Loan Purpose
* State
* Application Channel
* Approval Flag
* Default Flag
* Risk Category

## Step 1: Python Preprocessing

Python and Pandas are used to:

* Load the raw dataset
* Convert date columns
* Handle data types
* Create income bands
* Create credit score bands
* Create loan amount bands
* Export the processed dataset

Example:

```python
import pandas as pd
import numpy as np

df = pd.read_excel(
    'Bank_Loan_Analysis_15000.xlsx',
    sheet_name='Sheet1'
)

date_cols = [
    'Application_Date',
    'Approval_Date',
    'Disbursement_Date'
]

for col in date_cols:
    df[col] = pd.to_datetime(
        df[col],
        errors='coerce'
    )

income_bins = [
    0, 300000, 600000, 1000000,
    1500000, np.inf
]

income_labels = [
    '< 300k',
    '300k-600k',
    '600k-1M',
    '1M-1.5M',
    '> 1.5M'
]

df['Income_Band'] = pd.cut(
    df['Annual_Income'],
    bins=income_bins,
    labels=income_labels
)

df.to_csv(
    'Processed_Bank_Loan_Data.csv',
    index=False
)
```

## Step 2: Power BI Data Model

The processed CSV is imported into Power BI.

A Calendar dimension is created using DAX and connected to the loan application date.

```text
Calendar[Date]
      │
      │ 1 : *
      ↓
Processed_Bank_Loan_Data[Application_Date]
```

## Step 3: DAX Measures

The dashboard uses DAX measures including:

### Total Applications

```DAX
Total Applications =
COUNTROWS('Processed_Bank_Loan_Data')
```

### Total Approved Loans

```DAX
Total Approved Loans =
CALCULATE(
    [Total Applications],
    'Processed_Bank_Loan_Data'[Approval_Flag] = 1
)
```

### Approval Rate

```DAX
Approval Rate % =
DIVIDE(
    [Total Approved Loans],
    [Total Applications],
    0
)
```

### Total Default Loans

```DAX
Total Default Loans =
CALCULATE(
    [Total Applications],
    'Processed_Bank_Loan_Data'[Default_Flag] = 1
)
```

### Default Rate

```DAX
Default Rate % =
DIVIDE(
    [Total Default Loans],
    [Total Approved Loans],
    0
)
```

### Average Loan Amount

```DAX
Avg Loan Amount =
AVERAGE(
    'Processed_Bank_Loan_Data'[Loan_Amount]
)
```

### Total Funded Amount

```DAX
Total Funded Amount =
CALCULATE(
    SUM(
        'Processed_Bank_Loan_Data'[Loan_Amount]
    ),
    'Processed_Bank_Loan_Data'[Approval_Flag] = 1
)
```

## Dashboard

The Power BI dashboard contains:

### KPI Cards

* Total Applications
* Total Approved Loans
* Approval Rate
* Default Rate
* Average Loan Amount

### Charts

* Application and Approval Rate Trend
* Approval and Default Rate by Credit Score
* Risk Category vs Income Band
* Loan Purpose Breakdown
* Funded Amount by Loan Purpose
* Applications by State
* Defaults by Loan Purpose

### Filters

Users can interactively filter the dashboard using:

* Year
* State
* Loan Purpose
* Application Channel

## Key Business Questions

The dashboard helps answer questions such as:

1. How many loan applications were received?
2. How many applications were approved?
3. What is the overall approval rate?
4. What is the default rate among approved loans?
5. Which credit score groups have different approval/default patterns?
6. Which income groups have higher default rates?
7. Which loan purposes receive the highest funding?
8. How do loan applications change over time?
9. How do loan applications vary by state?
10. What are the major risk segments in the loan portfolio?

## Repository Structure

```text
Bank-Loan-Risk-Analytics-Dashboard/
│
├── data/
│   ├── raw/
│   │   └── Bank_Loan_Analysis_15000.xlsx
│   │
│   └── processed/
│       └── Processed_Bank_Loan_Data.csv
│
├── python/
│   └── preprocessing.py
│
├── powerbi/
│   └── Bank_Loan_Risk_Analytics.pbix
│
├── screenshots/
│   └── dashboard.png
│
├── requirements.txt
│
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Bank-Loan-Risk-Analytics-Dashboard.git
```

Install the Python dependencies:

```bash
pip install pandas numpy openpyxl
```

## Running the Project

### 1. Prepare the dataset

Place the raw Excel dataset inside:

```text
data/raw/
```

### 2. Run preprocessing

```bash
python python/preprocessing.py
```

The processed dataset will be generated in:

```text
data/processed/Processed_Bank_Loan_Data.csv
```

### 3. Open Power BI

Open:

```text
powerbi/Bank_Loan_Risk_Analytics.pbix
```

If required, update the CSV data source path in Power BI.

## Skills Demonstrated

This project demonstrates practical skills in:

* Python
* Pandas
* NumPy
* Data Cleaning
* Feature Engineering
* Exploratory Data Analysis
* Data Modeling
* DAX
* Power BI
* Dashboard Development
* Data Visualization
* Business Analytics
* Risk Analytics

## Author

**Jeevan M**

MCA — RNS Institute of Technology, Bengaluru

Interests: Artificial Intelligence, Machine Learning, Data Analytics, Generative AI

---

## License

This project is created for educational and portfolio purposes.
