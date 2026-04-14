# This file extracts the datasets using pandas
import pandas as pd
from pathlib import Path
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # relative directory using os
BASE_DIR_2 = Path(__file__).resolve.parent.parent #relative directory using path

def data_loader(file_name):
    file_path = os.path.join(BASE_DIR, file_name)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_name} not found.")
    df = pd.read_csv(file_path)
    print(f"{file_path} loaded with {len(df)} rows.")

    return df

def extracter():
    customers = data_loader("olist_customers_dataset.csv")
    geolocation = data_loader("olist_geolocation_dataset.csv")
    items = data_loader("olist_order_items_dataset")
    payments = data_loader("olist_order_payment_dataset")
    reviews = data_loader("olist_order_reviews_dataset")
    orders = data_loader("olist_orders_dataset")
    prodcuts = data_loader("olist_products_dataset")
    sellers = data_loader("olist_sellers_dataset")
    category = data_loader("product_category_name_translation")

    return customers, geolocation, items, payments, reviews, orders, prodcuts, sellers, category

if __name__ == "__main__":
    extracter()