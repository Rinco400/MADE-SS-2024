import pandas as pd
import sqlite3
import os

# Absolute path to the SQLite database
sqlite_db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'cleaned_data.db'))

def test_natural_mineralwater_data():
    conn = sqlite3.connect(sqlite_db_path)
    df = pd.read_sql_query("SELECT * FROM natural_mineralwater", conn)
    conn.close()

    # Check if the dataframe has the expected number of columns
    expected_columns = ['Probenahme-Beginn Datum', 'Probenahme-Ende Datum', 'Probe-Entnahmeart', 'Hauptprobenummer',
                        'Bezeichnung', 'Methode', 'Messprogrammgruppe', 'Entnahmestelle', 'Ergebnis', 'Einheit', 'Pruefmerkmal']
    assert len(df.columns.values) == len(expected_columns), "Number of columns in natural_mineralwater does not match expected"

    # Check if all expected columns are present
    for col in expected_columns:
        assert col in df.columns.values, f"Missing expected column: {col}"

    # Check if 'Ergebnis' column has no 'n.n.' values
    #assert (df['Ergebnis'] != 'n.n.').all(), "'Ergebnis' column contains 'n.n.' values"

    # Check if 'Ergebnis' column has numeric values
    #assert pd.to_numeric(df['Ergebnis'], errors='coerce').notna().all(), "'Ergebnis' column contains non-numeric values"

    print("All tests passed for natural_mineralwater data")

def test_babynahrung_gemuese_und_huehnchen_mit_nudeln_data():
    conn = sqlite3.connect(sqlite_db_path)
    df = pd.read_sql_query("SELECT * FROM babynahrung_gemuese_und_huehnchen_mit_nudeln", conn)
    conn.close()

    # Check if the dataframe has the expected number of columns
    expected_columns = ['Probenahme-Beginn Datum', 'Probenahme-Ende Datum', 'Probe-Entnahmeart', 'Hauptprobenummer',
                        'Bezeichnung', 'Methode', 'Messprogrammgruppe', 'Entnahmestelle', 'Ergebnis', 'Einheit', 'Pruefmerkmal']
    assert len(df.columns.values) == len(expected_columns), "Number of columns in babynahrung_gemuese_und_huehnchen_mit_nudeln does not match expected"

    # Check if all expected columns are present
    for col in expected_columns:
        assert col in df.columns.values, f"Missing expected column: {col}"

    # Check if 'Ergebnis' column has no 'n.n.' values
    #assert (df['Ergebnis'] != 'n.n.').all(), "'Ergebnis' column contains 'n.n.' values"

    # Check if 'Ergebnis' column has numeric values
    #assert pd.to_numeric(df['Ergebnis'], errors='coerce').notna().all(), "'Ergebnis' column contains non-numeric values"

    print("All tests passed for babynahrung_gemuese_und_huehnchen_mit_nudeln data")

def main():
    test_natural_mineralwater_data()
    test_babynahrung_gemuese_und_huehnchen_mit_nudeln_data()

if __name__ == "__main__":
    main()
