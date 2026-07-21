# Task 1: Data Cleaning

## Objective

The objective of this task is to clean a raw dataset by identifying and handling missing values, removing duplicate records, correcting incorrect data formats, and preparing the data for analysis.

---

## Project Description

In this project, a raw dataset was cleaned using **Python** and the **Pandas** library. The cleaning process included inspecting the dataset, handling missing values, removing duplicate records, correcting data types, formatting text fields, and exporting the cleaned dataset to a new Excel file.

---

## Features

* Loaded the dataset from an Excel file.
* Displayed dataset information and summary statistics.
* Identified missing (null) values.
* Removed duplicate rows.
* Filled missing values:

  * Replaced missing **CouponCode** values with `"No Coupon"`.
  * Filled missing numeric values with the column mean.
* Converted columns to appropriate data types:

  * Date
  * Quantity
  * Unit Price
  * Items in Cart
  * Total Price
* Removed unwanted spaces from text fields.
* Standardized text formatting using title case.
* Saved the cleaned dataset as a new Excel file.

---

## Technologies Used

* Python 3
* Pandas
* Visual Studio Code
* Microsoft Excel

---

## Project Structure

```text
Task-01-Data-Cleaning/
│── README.md
│── vscode1.py
│── Dataset for Data Analytics.xlsx
│── Cleaned_Dataset.xlsx

```

---

## How to Run

1. Install Python 3.
2. Install the required library:

```bash
pip install pandas openpyxl
```

3. Open the project in Visual Studio Code.
4. Update the dataset file path if required.
5. Run the program:

```bash
python vscode1.py
```

---

## Output

After execution, the program:

* Displays dataset information.
* Shows missing values before and after cleaning.
* Removes duplicate records.
* Corrects data formats.
* Saves the cleaned dataset as:

```text
Cleaned_Dataset.xlsx
```

---

## Key Skills

* Data Cleaning
* Data Preparation
* Handling Missing Values
* Removing Duplicates
* Data Type Conversion
* Python Programming
* Pandas Library
* Excel Data Processing

---

## Learning Outcomes

* Learned how to clean real-world datasets.
* Improved data quality for analysis.
* Worked with Excel files using Pandas.
* Prepared data for visualization and machine learning projects.

---

## Author

**Aboli Gurav**
