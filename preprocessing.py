import pandas as pd
import numpy as np

# 1. Load Dataset
df = pd.read_excel('Bank_Loan_Analysis_15000.xlsx', sheet_name='Sheet1')

# 2. Date Formatting
date_cols = ['Application_Date', 'Approval_Date', 'Disbursement_Date']
for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors='coerce')

# 3. Income & Credit Score Bins
income_bins = [0, 300000, 600000, 1000000, 1500000, np.inf]
income_labels = ['< 300k', '300k-600k', '600k-1M', '1M-1.5M', '> 1.5M']
df['Income_Band'] = pd.cut(df['Annual_Income'], bins=income_bins, labels=income_labels)

credit_bins = [300, 579, 669, 739, 799, 850]
credit_labels = ['Poor (300-579)', 'Fair (580-669)', 'Good (670-739)', 'Very Good (740-799)', 'Exceptional (800+)']
df['Credit_Score_Band'] = pd.cut(df['Credit_Score'], bins=credit_bins, labels=credit_labels)

loan_bins = [0, 250000, 500000, 1000000, 1500000, np.inf]
loan_labels = ['< 250k', '250k-500k', '500k-1M', '1M-1.5M', '> 1.5M']
df['Loan_Amount_Band'] = pd.cut(df['Loan_Amount'], bins=loan_bins, labels=loan_labels)

# 4. Save Processed File
df.to_csv('Processed_Bank_Loan_Data.csv', index=False)