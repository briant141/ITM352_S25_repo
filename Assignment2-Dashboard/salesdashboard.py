# Sales Dashboard Application
# This assignment is basically about how a program will load a sales data, lets us as the user to perform the analysis
# as well as using a pre-built options or having a custom pivot tables. Note I used AI like ChatGPT to help in some sections

import pandas as pd
import numpy as np
import time
import os
import sys
from datetime import datetime

# It loads the sales data that we got from the CSV file, it will then peform basic validation to see if it works
# and then prepares the data by coverting the data formats and checking all of the required columns
def load_csv(file_path):
    print(f"Loading CSV file: {file_path}")
    start_time = time.time()

    try:
        df = pd.read_csv(file_path, engine="pyarrow", on_bad_lines="skip")
        load_time = time.time() - start_time

        print(f"CSV file loaded successfully in {load_time:.2f} seconds. Noice")
        print(f"Number of rows: {len(df)}")
        print(f"Columns: {list(df.columns)}")
                                                            # Asked AI on how to get this format
        df['order_date'] = pd.to_datetime(df['order_date'], format='%m/%d/%y', errors='coerce')

        required_columns = {"quantity", "unit_price"}
        missing_columns = required_columns - set(df.columns)

        if missing_columns:
            print(f"Warning: Missing columns {missing_columns}. Some analytics may not function correctly.")
        return df
    except Exception as e:
        print(f"Error: Could not load the CSV file D: Reason: {e}")
        return None
    
# Allowing the user to choose which dataset (for my individual requirement)
# Created with AI assistance, I asked to help me create the first choice, from there I was able to make the other choices (lines 40-55)
def choose_dataset():
    print("\nSelect a dataset to load:")
    print("1. Default sales dataset (Google Drive)")
    print("2. Load local CSV file (e.g. sales_data_test.csv)")
    print("3. Enter a custom URL or file path")

    choice = input("Enter your choice (1–3): ").strip()
    if choice == "1":
        return "https://drive.google.com/uc?id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA"
    elif choice == "2":
        return input("Enter local filename: ").strip()
    elif choice == "3":
        return input("Enter full path or URL: ").strip()
    else:
        print("Invalid choice. Using default.")
        return "https://drive.google.com/uc?id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA"


# Lets us as the user preview the first few rows of the dataset, or view the full table.
def display_initial_rows(data):
    while True:
        user_input = input("\nEnter number of rows to display ('all' or press Enter to skip): ").strip().lower()
        if user_input == "":
            print("Skipping preview.")
            break
        elif user_input == "all":
            print(data)
            break
        elif user_input.isdigit():
            num_rows = int(user_input)
            if num_rows > 0:
                print(data.head(num_rows))
                break
            else:
                print("Enter a positive number :D")
        else:
            print("Invalid input :(")

# lets us quit the program
def exit_program(data):
    sys.exit("Exiting program.")

# Here I have used AI prompt to add an export functionality and changed it to work with the analysis options in the menu (lines 84-90)

def export_prompt(df_result):
    choice = input("Export to Excel? (y/n): ").strip().lower()
    if choice == 'y':
        filename = input("Enter filename (without extension): ").strip()
        if filename:
            df_result.to_excel(f"{filename}.xlsx")
            print(f"Exported to {filename}.xlsx")

# Filters out any data when the user inputs what they want
# I used the AI prompt to create a basic row/date filtering logic, then adapted it to help match the assignment requirements (lines 97-103)

def get_filtered_data(df):
    try:
        row_input = input("Enter row numbers to use (e.g. 5-20 or 1,5,10): ").strip()
        if '-' in row_input:
            start, end = map(int, row_input.split('-'))
            df = df.iloc[start:end+1]
        elif row_input:
            indices = list(map(int, row_input.split(',')))
            df = df.iloc[indices]
    except:
        print("Invalid row input. Using full dataset.")

    if 'order_date' in df.columns:
        try:
            start_date = input("Enter start date (use this setup YYYY-MM-DD) or press Enter to skip: ").strip()
            end_date = input("Enter end date (use this setup YYYY-MM-DD) or press Enter to skip: ").strip()
            if start_date:
                df = df[df['order_date'] >= pd.to_datetime(start_date)]
            if end_date:
                df = df[df['order_date'] <= pd.to_datetime(end_date)]
        except:
            print("Invalid date input. Skipping date filter.")
    return df

# This part is where R3 comes in, all of the predefined analytical tasks
# Each of the function seen here will help asks the user about filtering data by row range and then date range before going in
# I asked AI to help me get a prompt for lines 123-128 and then proceeded from there to make the rest after getting the general idea

def sales_by_region_order_type(data):
    data = get_filtered_data(data)
    data['sales'] = data['quantity'] * data['unit_price']
    pivot = pd.pivot_table(data, values='sales', index='sales_region', columns='order_type', aggfunc=np.sum)
    print(pivot)
    export_prompt(pivot)

def avg_sales_by_region_state_type(data):
    data = get_filtered_data(data)
    data['sales'] = data['quantity'] * data['unit_price']
    pivot = pd.pivot_table(data, values='sales', index='sales_region', columns=['state', 'order_type'], aggfunc=np.mean)
    print(pivot)
    export_prompt(pivot)

def sales_by_customer_type_state(data):
    data = get_filtered_data(data)
    data['sales'] = data['quantity'] * data['unit_price']
    pivot = pd.pivot_table(data, values='sales', index='state', columns=['customer_type', 'order_type'], aggfunc=np.sum)
    print(pivot)
    export_prompt(pivot)

def total_qty_price_by_region_product(data):
    data = get_filtered_data(data)
    data['sales'] = data['quantity'] * data['unit_price']
    pivot = pd.pivot_table(data, index='sales_region', columns='product_name', values=['quantity', 'sales'], aggfunc=np.sum)
    print(pivot)
    export_prompt(pivot)

def total_qty_price_by_customer_type(data):
    data = get_filtered_data(data)
    data['sales'] = data['quantity'] * data['unit_price']
    pivot = pd.pivot_table(data, index='customer_type', values=['quantity', 'sales'], aggfunc=np.sum)
    print(pivot)
    export_prompt(pivot)

def max_min_sales_by_category(data):
    data = get_filtered_data(data)
    data['sales'] = data['quantity'] * data['unit_price']
    pivot = data.groupby('product_category')['sales'].agg(['max', 'min'])
    print(pivot)
    export_prompt(pivot)

def unique_employees_by_region(data):
    data = get_filtered_data(data)
    if 'employee' not in data.columns:
        print("Missing 'employee' column.")
        return
    pivot = data.groupby('sales_region')['employee'].nunique()
    print(pivot)
    export_prompt(pivot)

# Users will have the option to select a number of choices in the interface, if they put something invalid it will show an error
# I asked AI to help me build this multi-select input handler, then simplified it to fit class formatting and validation (lines 177-189

def get_user_selection(options, prompt): 
    print(prompt) 
    for i, option in enumerate(options):
        print(f"{i+1}. {option}") 
    choice = input("Enter the number(s) of your choice(s), separated by commas: ").strip()
    try:
        selected = [options[int(i.strip()) - 1] for i in choice.split(',') if i.strip().isdigit() and 1 <= int(i.strip()) <= len(options)]
        if not selected:
            raise ValueError
        return selected
    except:
        print("Invalid selection. Using default option (first in list).")
        return [options[0]]

# One of the selection choices, specifically on how to get us a custom pivot table (generate and filter out data)
# I asked AI help me get started on how to create a dynamic pivot table generator for the R4 requirement
# and then the possible customization to match requirements (lines 194-221)

def generate_custom_pivot_table(data):
    data = get_filtered_data(data)
    row_options = list(data.columns)
    rows = get_user_selection(row_options, "Select rows:")
    col_options = [col for col in row_options if col not in rows]
    cols = get_user_selection(col_options, "Select columns:")
    value_options = list(data.select_dtypes(include=['number']).columns)
    values = get_user_selection(value_options, "Select values:")
    agg_options = ['sum', 'mean', 'count']
    agg_func = get_user_selection(agg_options, "Select aggregation function:")

    if not rows or not values:
        print("No rows or values selected. Cannot create pivot table.")
        return

    try:
        pivot_table = pd.pivot_table(
            data,
            index=rows,
            columns=cols if cols else None,
            values=values,
            aggfunc=agg_func[0] if len(agg_func) == 1 else agg_func
        )
        print(pivot_table)
        export_prompt(pivot_table)
    except Exception as e:
        print(f"Failed to create pivot table: {e}")
        return

# This is the display menu, users can choose one of the options or to quit
# I asked AI for assisstance on how to create a basic menu interface and from there used to create the rest of the interfaces 
# (lines 227-250) issubset was a really useful function I found through the use of AI (determining a set is a subset of another)
def display_menu(data):
    menu_options = [("Show the first n rows of sales data", display_initial_rows)]

    if {"sales_region", "order_type", "quantity", "unit_price"}.issubset(data.columns):
        menu_options.append(("Total sales by region and order_type", sales_by_region_order_type))

    if {"sales_region", "state", "order_type", "quantity", "unit_price"}.issubset(data.columns):
        menu_options.append(("Average sales by region/state/order_type", avg_sales_by_region_state_type))

    if {"state", "customer_type", "order_type", "quantity", "unit_price"}.issubset(data.columns):
        menu_options.append(("Sales by customer type/order type by state", sales_by_customer_type_state))

    if {"sales_region", "product_name", "quantity", "unit_price"}.issubset(data.columns):
        menu_options.append(("Total qty & price by region and product", total_qty_price_by_region_product))

    if {"customer_type", "quantity", "unit_price"}.issubset(data.columns):
        menu_options.append(("Total qty & price by customer type", total_qty_price_by_customer_type))

    if {"product_category", "quantity", "unit_price"}.issubset(data.columns):
        menu_options.append(("Max & min sales price by category", max_min_sales_by_category))

    if {"sales_region", "employee"}.issubset(data.columns):
        menu_options.append(("Number of unique employees by region", unique_employees_by_region))

    # This part allows us to exit from the program as well as adding the options to create a custom pivot table
    menu_options.append(("Create a custom pivot table", generate_custom_pivot_table))
    menu_options.append(("Exit the program", exit_program))

# I used AI here to help me on lines 256-259, these lines helped me create the structure and loop of displaying the menu
    while True:
        print("\nMenu:")
        for i, (label, _) in enumerate(menu_options, 1):
            print(f"{i}. {label}")

        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= len(menu_options):
                menu_options[choice - 1][1](data)
            else:
                print("Invalid option.")
        except ValueError:
            print("Please enter a valid number.")


# The main part of the function that helps loads in the data and actually launching the dashboard menu to show up
def main():
    print("Launching Sales Dashboard...")
    file_path = choose_dataset()
    df = load_csv(file_path)
    if df is not None:
        display_menu(df)
main()
