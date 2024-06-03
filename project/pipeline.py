import os
import pandas as pd
import sqlite3
import ssl
from urllib.request import urlretrieve

# Define URLs for datasets
baby_food_url = "https://daten.transparenz.hamburg.de/Dataport.HmbTG.ZS.Webservice.GetRessource100/GetRessource100.svc/fa8ce806-e088-4bfb-9aa8-87c5c61807b1/Babynahrung_Gemuese_und_Huehnchen_mit_Nudeln.csv"
natural_mineralwater_url = "https://daten.transparenz.hamburg.de/Dataport.HmbTG.ZS.Webservice.GetRessource100/GetRessource100.svc/f565c684-2c98-4c61-982d-c1ec7ec2cade/Natural_Mineralwater.csv"

# Define local file paths
project_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(project_dir, "data")
baby_food_file = os.path.join(data_dir, "Babynahrung_Gemuese_und_Huehnchen_mit_Nudeln.csv")
natural_mineralwater_file = os.path.join(data_dir, "Natural_Mineralwater.csv")
baby_food_db = os.path.join(data_dir, "baby_food.db")
natural_mineralwater_db = os.path.join(data_dir, "natural_mineralwater.db")
merged_db = os.path.join(data_dir, "merged_data.db")

# Create data directory if it doesn't exist
os.makedirs(data_dir, exist_ok=True)

# Disable SSL certificate verification (use with caution)
ssl._create_default_https_context = ssl._create_unverified_context

# Download datasets
urlretrieve(baby_food_url, baby_food_file)
urlretrieve(natural_mineralwater_url, natural_mineralwater_file)

# Load datasets
baby_food_df = pd.read_csv(baby_food_file, encoding='latin1', delimiter=';', on_bad_lines='skip')
natural_mineralwater_df = pd.read_csv(natural_mineralwater_file, encoding='latin1', delimiter=';', on_bad_lines='skip')

# Data Cleaning and Transformation
baby_food_df['Probenahme-Beginn Datum'] = pd.to_datetime(baby_food_df['Probenahme-Beginn Datum'], format='%d.%m.%Y')
natural_mineralwater_df['Probenahme-Beginn Datum'] = pd.to_datetime(natural_mineralwater_df['Probenahme-Beginn Datum'], format='%d.%m.%Y')

# Ensure the 'Ergebnis' column is numeric for both datasets
baby_food_df['Ergebnis'] = pd.to_numeric(baby_food_df['Ergebnis'], errors='coerce')
natural_mineralwater_df['Ergebnis'] = pd.to_numeric(natural_mineralwater_df['Ergebnis'], errors='coerce')

# Drop rows with missing 'Ergebnis' values
baby_food_df.dropna(subset=['Ergebnis'], inplace=True)
natural_mineralwater_df.dropna(subset=['Ergebnis'], inplace=True)

# Rename 'Ergebnis' columns for clarity before merging
baby_food_df.rename(columns={'Ergebnis': 'Radioactivity_Baby_Food'}, inplace=True)
natural_mineralwater_df.rename(columns={'Ergebnis': 'Radioactivity_Mineral_Water'}, inplace=True)

# Merge datasets on 'Probenahme-Beginn Datum'
merged_df = pd.merge(baby_food_df, natural_mineralwater_df, on='Probenahme-Beginn Datum', suffixes=('_baby', '_water'))

# Store cleaned and merged dataset in SQLite database
def store_in_db(df, db_path, table_name):
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()

store_in_db(merged_df, merged_db, 'merged_data')

# Also store individual cleaned datasets
store_in_db(baby_food_df, baby_food_db, 'baby_food')
store_in_db(natural_mineralwater_df, natural_mineralwater_db, 'natural_mineralwater')

print(f"Data pipeline executed successfully and datasets are stored in {data_dir}.")


