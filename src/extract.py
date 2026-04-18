# This file extracts the datasets using pandas
# made by Ralu Ofoche
import pandas as pd
from pathlib import Path
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # relative directory using os
BASE_DIR_2 = Path(__file__).resolve().parent.parent #relative directory using path

def data_loader(file_name):
    file_path = BASE_DIR_2 / "data" / "raw" / file_name
    print(f"this is the path {file_path}")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_name} not found.")
    df = pd.read_csv(file_path)
    print(f"{file_path} loaded with {len(df)} rows.")

    return df

def extracter():
    customer_data = {
        "customers" : data_loader("olist_customers_dataset.csv"),
        "geolocation" : data_loader("olist_geolocation_dataset.csv"),
        "items" : data_loader("olist_order_items_dataset.csv"),
        "payments" : data_loader("olist_order_payments_dataset.csv"),
        "reviews" : data_loader("olist_order_reviews_dataset.csv"),
        "orders" : data_loader("olist_orders_dataset.csv"),
        "prodcuts" : data_loader("olist_products_dataset.csv"),
        "sellers" : data_loader("olist_sellers_dataset.csv"),
        "category" : data_loader("product_category_name_translation.csv")
    }
    print(customer_data["category"].columns.tolist())
    return customer_data

if __name__ == "__main__":
    extracter()
    

