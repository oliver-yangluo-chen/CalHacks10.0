import pandas as pd

# Replace 'your_file.xlsx' with the actual path of your Excel file
file_path = 'congress-trading-all.xlsx'

# Read the Excel file
try:
    df = pd.read_excel(file_path)
    print(df)
except FileNotFoundError:
    print(f"File not found at path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
