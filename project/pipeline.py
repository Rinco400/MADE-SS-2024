import pandas as pd
import requests
from io import BytesIO
import sqlite3
import os
import urllib3
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(InsecureRequestWarning)
    

def download_csv(url, headers=None):
    response = requests.get(url, headers=headers, verify=False)
    response.raise_for_status()
    df = pd.read_csv(BytesIO(response.content), encoding='latin1', delimiter=';')
    return df


def save_to_sqlite(df, table_name, db_path):
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    print(f"Saving to SQLite DB at path: {db_path}")
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()


csv_url_1 = 'https://daten.transparenz.hamburg.de/Dataport.HmbTG.ZS.Webservice.GetRessource100/GetRessource100.svc/f565c684-2c98-4c61-982d-c1ec7ec2cade/Natural_Mineralwater.csv'
csv_url_2 = 'https://daten.transparenz.hamburg.de/Dataport.HmbTG.ZS.Webservice.GetRessource100/GetRessource100.svc/fa8ce806-e088-4bfb-9aa8-87c5c61807b1/Babynahrung_Gemuese_und_Huehnchen_mit_Nudeln.csv'

sqlite_db_path = os.path.join('../data', 'cleaned_data.db')
print(f"SQLite DB Path: {sqlite_db_path}")



df1 = download_csv(csv_url_1)
df2 = download_csv(csv_url_2)

df1['Ergebnis'] = df1['Ergebnis'].replace('n.n.', 0)
df1 = df1.drop(columns=['Probenahme-Beginn Zeit', 'Probenahme-Ende Zeit', 'Umweltbereich', 'Herkunftsstaat'])

df2['Ergebnis'] = df2['Ergebnis'].replace('n.n.', 0)
df2 = df2.drop(columns=['Probenahme-Beginn Zeit', 'Probenahme-Ende Zeit', 'Umweltbereich', 'Herkunftsstaat'])

save_to_sqlite(df1, 'natural_mineralwater', sqlite_db_path)
save_to_sqlite(df2, 'babynahrung_gemuese_und_huehnchen_mit_nudeln', sqlite_db_path)

