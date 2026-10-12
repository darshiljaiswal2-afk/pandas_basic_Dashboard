import pandas as pd
import streamlit as st
from pathlib import Path

# ----------------------------
# 1. Page configuration
# ----------------------------
st.set_page_config(
    page_title="Product Insights Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Product Insights Dashboard")
st.caption("Explore products, prices, and categories")

# ----------------------------
# 2. Load JSON data
# ----------------------------
file_path = Path(__file__).with_name(
    "sample___Data.json"
)

@st.cache_data
def load_data(path):
    return pd.read_json(path)

try:
    df = load_data(str(file_path))

except FileNotFoundError:
    st.error("JSON file not found beside sales_dashboard.py.")
    st.stop()

except (ValueError, TypeError) as error:
    st.error(f"Could not read JSON: {error}")
    st.stop()

required_columns = {
    "id", "name", "description",
    "price", "category", "image"
}

missing = required_columns - set(df.columns)

if missing:
    st.error(f"Missing expected columns: {sorted(missing)}")
    st.stop()

df["price"] = pd.to_numeric(
    df["price"], errors="coerce"
)

df["category"] = df["category"].fillna("Unknown")
df["name"] = df["name"].fillna("Unnamed product")

# ----------------------------
# 3. Sidebar filters
# ----------------------------
st.sidebar.header("Filters")

search = st.sidebar.text_input(
    "Search product name"
)

categories = sorted(
    df["category"].unique().tolist()
)

selected_categories = st.sidebar.multiselect(
    "Choose categories",
    categories,
    default=categories
)

valid_prices = df["price"].dropna()

filtered = df[
    df["category"].isin(selected_categories)
].copy()

if search:
    filtered = filtered[
        filtered["name"].str.contains(
            search, case=False, na=False
        )
    ]

if not valid_prices.empty:
    min_price = float(valid_prices.min())
    max_price = float(valid_prices.max())

    if min_price < max_price:
        price_range = st.sidebar.slider(
            "Price range",
            min_value=min_price,
            max_value=max_price,
            value=(min_price, max_price)
        )

        filtered = filtered[
            filtered["price"].between(
                price_range[0], price_range[1]
            )
            | filtered["price"].isna()
        ]

# ----------------------------
# 4. KPI cards
# ----------------------------
st.subheader("Key Metrics")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Products", f"{len(filtered):,}")

c2.metric(
    "Average Price",
    f"{filtered['price'].mean():,.2f}"
    if filtered["price"].notna().any()
    else "N/A"
)

c3.metric(
    "Highest Price",
    f"{filtered['price'].max():,.2f}"
    if filtered["price"].notna().any()
    else "N/A"
)

c4.metric(
    "Categories",
    f"{filtered['category'].nunique():,}"
)

# ----------------------------
# 5. Category analysis
# ----------------------------
st.subheader("Category Analysis")

if not filtered.empty:
    category_summary = (
        filtered.groupby("category")
        .agg(
            Products=("id", "count"),
            Average_Price=("price", "mean"),
            Total_Listed_Price=("price", "sum")
        )
        .sort_values(
            "Total_Listed_Price",
            ascending=False
        )
    )

    st.write("Total listed price by category")
    st.bar_chart(category_summary["Total_Listed_Price"])

    st.write("Average price by category")
    st.bar_chart(category_summary["Average_Price"])

    st.dataframe(
        category_summary.round(2),
        use_container_width=True
    )
else:
    st.info("No products match the selected filters.")

# ----------------------------
# 6. Highest-priced products
# ----------------------------
st.subheader("Highest-Priced Products")

top_products = (
    filtered.dropna(subset=["price"])
    .nlargest(10, "price")
)

st.dataframe(
    top_products[
        ["id", "name", "category", "price"]
    ],
    use_container_width=True,
    hide_index=True
)

# ----------------------------
# 7. Product catalog
# ----------------------------
st.subheader("Product Catalog")

display_columns = [
    "id", "name", "category",
    "price", "description", "image"
]

st.dataframe(
    filtered[display_columns],
    use_container_width=True,
    hide_index=True,
    column_config={
        "price": st.column_config.NumberColumn(
            "Price",
            format="%.2f"
        ),
        "image": st.column_config.LinkColumn(
            "Product Image URL",
            display_text="Open image"
        )
    }
)

# ----------------------------
# 8. Download filtered data
# ----------------------------
csv_bytes = filtered.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    "Download filtered products as CSV",
    data=csv_bytes,
    file_name="filtered_products.csv",
    mime="text/csv"
)

# ----------------------------
# 9. Data quality
# ----------------------------
with st.expander("Data Quality Report"):
    quality = pd.DataFrame({
        "Data Type": df.dtypes.astype(str),
        "Missing Values": df.isna().sum(),
        "Unique Values": df.nunique()
    })

    st.dataframe(
        quality,
        use_container_width=True
    )

    st.write(
        "Duplicate rows:",
        int(df.duplicated().sum())
    )
