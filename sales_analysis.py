import pandas as pd


def load_sales_data(file_name):
    sales_data = pd.read_csv(file_name)
    return sales_data


def explore_sales_data(sales_data):
    print("First 5 rows of dataset:")
    print(sales_data.head())

    print("\nDataset shape:")
    print(sales_data.shape)

    print("\nColumn names:")
    print(sales_data.columns.tolist())

    print("\nData types:")
    print(sales_data.dtypes)


def clean_sales_data(sales_data):
    sales_data = sales_data.drop_duplicates()

    numeric_columns = sales_data.select_dtypes(include="number").columns
    sales_data[numeric_columns] = sales_data[numeric_columns].fillna(
        sales_data[numeric_columns].median()
    )

    return sales_data


def analyze_sales_data(sales_data):
    total_revenue = sales_data["Total_Sales"].sum()
    average_sales = sales_data["Total_Sales"].mean()
    highest_sale = sales_data["Total_Sales"].max()
    lowest_sale = sales_data["Total_Sales"].min()
    best_selling_product = sales_data.groupby("Product")["Quantity"].sum().idxmax()

    print("\nSales Analysis Report")
    print("----------------------")
    print(f"Total Revenue: ₹{total_revenue}")
    print(f"Average Sales: ₹{average_sales:.2f}")
    print(f"Highest Sale: ₹{highest_sale}")
    print(f"Lowest Sale: ₹{lowest_sale}")
    print(f"Best Selling Product: {best_selling_product}")


def main():
    file_name = "sales_data.csv"

    sales_data = load_sales_data(file_name)

    explore_sales_data(sales_data)

    cleaned_sales_data = clean_sales_data(sales_data)

    analyze_sales_data(cleaned_sales_data)


main()