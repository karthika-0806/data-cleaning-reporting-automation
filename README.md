# Automated Data Cleaning & Reporting System

## Overview

This project automates the process of data cleaning, preprocessing, and report generation using Python. The system loads raw datasets, identifies data quality issues, cleans the data, generates reports, and exports the cleaned dataset for further analysis.

The goal is to reduce manual effort, improve data quality, and create a repeatable workflow for handling large datasets.

---

## Features

- Automated dataset loading
- Missing value detection and handling
- Duplicate record removal
- Data preprocessing and cleaning
- Automated report generation
- Statistical summary creation
- Data visualization using charts
- Export of cleaned dataset

---

## Technologies Used

- Python
- Pandas
- Matplotlib
- NumPy
- CSV Files

---

## Project Workflow

1. Load raw dataset
2. Analyze data quality
3. Detect missing values
4. Remove duplicate records
5. Fill missing values
6. Generate cleaning report
7. Create summary statistics
8. Generate visualizations
9. Export cleaned dataset

---

## Project Structure

```text
Automated-Data-Cleaning-Reporting-System/
│
├── automation.py
├── dataset.csv
├── cleaned_data.csv
├── report.txt
├── summary_statistics.csv
├── missing_values_chart.png
├── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/automated-data-cleaning-reporting-system.git
```

Navigate to the project folder:

```bash
cd automated-data-cleaning-reporting-system
```

Install required libraries:

```bash
pip install pandas matplotlib numpy
```

---

## Usage

Run the automation script:

```bash
python automation.py
```

The script will:

- Load the dataset
- Clean missing values
- Remove duplicates
- Generate reports
- Create charts
- Save cleaned data

---

## Output Files

### Cleaned Dataset

```text
cleaned_data.csv
```

Contains the processed dataset after cleaning.

### Cleaning Report

```text
report.txt
```

Contains:

- Original records count
- Records after cleaning
- Duplicate records removed
- Missing values before cleaning
- Missing values after cleaning

### Statistical Summary

```text
summary_statistics.csv
```

Contains descriptive statistics for the dataset.

### Visualization

```text
missing_values_chart.png
```

Graphical representation of dataset quality metrics.

---

## Sample Results

```text
Original Records: 113390

Records After Cleaning: 87396

Duplicates Removed: 31994

Missing Values Before Cleaning: 129425

Missing Values After Cleaning: 0
```

---

## Learning Outcomes

This project demonstrates:

- Data Cleaning
- Data Preprocessing
- Data Analysis
- Data Quality Management
- Automation with Python
- Report Generation
- Data Visualization

---

## Future Improvements

- Interactive dashboard using Power BI
- Automated scheduling using Task Scheduler
- Email report generation
- Web-based interface
- Machine learning integration

---

## Author

Developed as part of a Data Cleaning & Reporting Automation project using Python and Pandas.
