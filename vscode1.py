import pandas as pd
import os

df = pd.read_excel(r"C:\Users\LENOVO\Downloads\Dataset for Data Analytics.xlsx")

print("First 5 Rows")
print(df.head())

print("\nLast 5 Rows")
print(df.tail())

print("\nDataset Information")
print(df.info())

print("\nDataset Shape")
print(df.shape)

print("\nColumn Names")
print(df.columns.tolist())

print("\nStatistical Summary")
print(df.describe())

print("\nMissing Values Before Cleaning")
print(df.isnull().sum())

duplicates = df.duplicated().sum()
print("\nDuplicate Rows:", duplicates)

df = df.drop_duplicates()

df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns

for col in numeric_columns:
    df[col] = df[col].fillna(df[col].mean())

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["UnitPrice"] = pd.to_numeric(df["UnitPrice"], errors="coerce")
df["ItemsInCart"] = pd.to_numeric(df["ItemsInCart"], errors="coerce")
df["TotalPrice"] = pd.to_numeric(df["TotalPrice"], errors="coerce")

text_columns = df.select_dtypes(include="object").columns

for col in text_columns:
    df[col] = df[col].str.strip()

for col in ["Product", "PaymentMethod", "OrderStatus", "ReferralSource"]:
    df[col] = df[col].str.title()

print("\nMissing Values After Cleaning")
print(df.isnull().sum())

print("\nUpdated Data Types")
print(df.dtypes)

print("\nCleaned Dataset Preview")
print(df.head())

output_path = r"C:\Users\LENOVO\Downloads\Cleaned_Dataset_v2.xlsx"

df.to_excel(output_path, index=False)

print("\nDataset cleaned successfully!")
print("File Saved:", os.path.exists(output_path))
print("Saved Location:", output_path)