import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# SALES DATA
# -----------------------------

data = {
    "Product": [
        "Laptop",
        "Mouse",
        "Keyboard",
        "Monitor",
        "Printer",
        "Headphones",
        "Webcam"
    ],

    "Category": [
        "Electronics",
        "Accessories",
        "Accessories",
        "Electronics",
        "Electronics",
        "Accessories",
        "Accessories"
    ],

    "Quantity": [10, 50, 30, 15, 8, 25, 20],

    "Price": [50000, 500, 1500, 12000, 8000, 2000, 3000]
}

# -----------------------------
# CREATE DATAFRAME
# -----------------------------

df = pd.DataFrame(data)

# -----------------------------
# CALCULATE REVENUE
# -----------------------------

df["Revenue"] = df["Quantity"] * df["Price"]

# -----------------------------
# BASIC STATISTICS
# -----------------------------

total_revenue = df["Revenue"].sum()
average_revenue = df["Revenue"].mean()

best_selling_product = df.loc[df["Quantity"].idxmax(), "Product"]

highest_revenue_product = df.loc[df["Revenue"].idxmax(), "Product"]

lowest_revenue_product = df.loc[df["Revenue"].idxmin(), "Product"]

# -----------------------------
# TOP 3 PRODUCTS
# -----------------------------

top_products = df.sort_values(
    by="Revenue",
    ascending=False
).head(3)

# -----------------------------
# CATEGORY ANALYSIS
# -----------------------------

category_revenue = df.groupby(
    "Category"
)["Revenue"].sum()

# -----------------------------
# DISPLAY REPORT
# -----------------------------

print("\n==============================")
print(" SALES ANALYSIS REPORT ")
print("==============================\n")

print(df)

print("\n---------- SUMMARY ----------")

print(f"Total Revenue        : ₹{total_revenue:,}")
print(f"Average Revenue      : ₹{average_revenue:,.2f}")
print(f"Best Selling Product : {best_selling_product}")
print(f"Highest Revenue Item : {highest_revenue_product}")
print(f"Lowest Revenue Item  : {lowest_revenue_product}")

print("\n---------- TOP 3 PRODUCTS ----------")
print(top_products[["Product", "Revenue"]])

print("\n---------- CATEGORY REVENUE ----------")
print(category_revenue)

# -----------------------------
# EXPORT REPORT
# -----------------------------

df.to_csv("sales_report.csv", index=False)

# -----------------------------
# BAR CHART
# -----------------------------

plt.figure(figsize=(8, 5))

plt.bar(df["Product"], df["Revenue"])

plt.title("Product Revenue Analysis")
plt.xlabel("Products")
plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig("revenue_bar_chart.png")

plt.show()

# -----------------------------
# PIE CHART
# -----------------------------

plt.figure(figsize=(7, 7))

plt.pie(
    df["Revenue"],
    labels=df["Product"],
    autopct="%1.1f%%"
)

plt.title("Revenue Share by Product")

plt.savefig("revenue_pie_chart.png")

plt.show()

print("\nFiles Generated Successfully")
print("✔ sales_report.csv")
print("✔ revenue_bar_chart.png")
print("✔ revenue_pie_chart.png")
