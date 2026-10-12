# 📊 Product Insights Dashboard

An interactive product analytics dashboard built with **Python, Pandas, and Streamlit**. Explore product catalogs, analyze prices, compare categories, filter products, and export data through a web-based interface.

## 🚀 Project Overview

The Product Insights Dashboard transforms structured JSON product data into an interactive analytics application. It provides an easy way to explore product information, identify high-priced products, compare product categories, and inspect data quality.

This project was developed to practice Python programming, Pandas data analysis, data cleaning, and interactive dashboard development.

## ✨ Features

- **Interactive Dashboard:** Explore product data through a browser-based interface.
- **Key Metrics:** View total products, average price, highest price, and number of categories.
- **Product Search:** Search products by name.
- **Category Filters:** Filter products by one or more categories.
- **Price Range Filtering:** Narrow down products by price.
- **Category Analysis:** Compare total listed prices and average prices across categories.
- **Top Products:** Identify the 10 highest-priced products.
- **Product Catalog:** View product IDs, names, descriptions, categories, prices, and image links.
- **Data Quality Report:** Inspect missing values, unique values, and duplicate records.
- **CSV Export:** Download filtered product data for further analysis.
- **JSON Data Processing:** Load structured data using Pandas.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data processing and analysis |
| Streamlit | Interactive web dashboard |
| JSON | Product data storage |
| Git and GitHub | Version control and project hosting |

## 📁 Project Structure

```text
product-insights-dashboard/
├── sales_dashboard.py
├── sample___Data.json
├── requirements.txt
└── README.md
```

- `sales_dashboard.py` — Main Streamlit dashboard application.
- `sample___Data.json` — Product dataset.
- `requirements.txt` — Python package dependencies.
- `README.md` — Project documentation.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Replace `YOUR-USERNAME` and `YOUR-REPOSITORY` with your actual GitHub username and repository name.

### 2. Navigate to the project folder

```bash
cd YOUR-REPOSITORY
```

### 3. Create a virtual environment (recommended)

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the dashboard

```bash
python -m streamlit run sales_dashboard.py
```

Streamlit will provide a local URL, usually:

`http://localhost:8501`

Open the URL in your browser to use the dashboard.

## 📦 Dependencies

Create a `requirements.txt` file containing:

```text
pandas
streamlit
```

These are the direct dependencies used by the application. You can pin tested versions later for more reproducible installations.

## 📊 Dataset Information

The current JSON dataset contains the following fields:

| Column | Description |
|---|---|
| `id` | Unique product identifier |
| `name` | Product name |
| `description` | Product description |
| `price` | Listed product price |
| `category` | Product category |
| `image` | Product image URL |

The dashboard analyzes listed product prices and category distributions. The current dataset does not contain order transactions, quantities sold, or product costs; therefore, actual sales revenue and profit are not calculated.

## 🧠 Pandas Concepts Practiced

This project demonstrates practical applications of:

- `pd.read_json()` — Load JSON data into a DataFrame.
- `pd.to_numeric()` — Convert price values into numeric form.
- `select_dtypes()` — Identify columns by data type.
- `groupby()` — Aggregate product information by category.
- `agg()` — Calculate multiple summary statistics.
- `nlargest()` — Find the highest-priced products.
- `isna()` — Detect missing values.
- `nunique()` — Count distinct values.
- `duplicated()` — Detect duplicate records.
- `to_csv()` — Export filtered data.

## 🔮 Future Improvements

- Add interactive product image previews.
- Introduce price distribution histograms and additional charts.
- Add product-level comparisons and category rankings.
- Connect real sales transaction data to calculate revenue and profit.
- Add date-based sales trends when transaction dates become available.
- Deploy the application online using Streamlit Community Cloud or another hosting service.
- Improve the user interface with custom styling and responsive layouts.

## 🎯 Learning Outcomes

Through this project, I practiced:

- Working with JSON files in Python.
- Performing exploratory data analysis with Pandas.
- Filtering, grouping, and aggregating data.
- Building interactive applications with Streamlit.
- Exporting data and organizing a Python project.
- Preparing a project for GitHub.

## 👨‍💻 Author

**Darshil Jaiswal**

Computer Science Engineering — Artificial Intelligence and Machine Learning

GitHub: [@darshiljaiswal2-afk](https://github.com/darshiljaiswal2-afk)

---

If you find this project useful, feel free to explore the code and suggest improvements.

**Built with Python, Pandas, and Streamlit.**
