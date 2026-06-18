# Automated Hardware Data Sanitizer & ETL Pipeline

A production-ready Command-Line Interface (CLI) data engineering utility built in Python. This system automates the ingestion, structural type-cleaning, and statistical repair of corrupted hardware inventory logs, dynamically exporting sanitized database files and high-resolution analytical graphics.

## 🧠 Engineering Logic & Design Decisions

Amateur data scripts frequently crash when encountering real-world user data. This pipeline implements several defensive programming strategies to ensure absolute execution stability:

1. **Type Coercion Layer:** Uses `pd.to_numeric` with `errors="coerce"` to automatically detect string-wrapped metrics (like `"65"`) and sanitize toxic non-numeric characters without breaking the execution flow.
2. **Robust Imputation Matrix:** Instead of using a simple mean/average—which gets heavily skewed by extreme market price outliers—the pipeline calculates an outlier-resistant **Median** to patch missing price slots logically.
3. **Logistics Fallback Constraints:** Missing inventory numbers are automatically assigned a zero-unit floor (`0`) to prevent dangerous operational data inflation.
4. **Automated Business Intelligence:** Dynamically evaluates stock levels against sanitized price structures to engineer a custom `Total value asset` financial column.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Core Libraries:** Pandas, Matplotlib

## 💻 How To Run the Utility

Ensure you have your raw data sheet (`messy_hardware_log.csv`) in the same directory, then execute the pipeline via your terminal:

```bash
python dataset_sanitizer.py
