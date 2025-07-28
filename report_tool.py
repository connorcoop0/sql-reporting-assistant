import sqlite3
import csv
import sys
import os

def load_csv_to_sqlite(csv_file, conn, table_name="data"):
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)
        headers = [h.strip().replace(" ", "_") for h in headers]

        cursor = conn.cursor()
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        col_defs = ", ".join(f'"{h}" TEXT' for h in headers)
        cursor.execute(f"CREATE TABLE {table_name} ({col_defs})")

        for row in reader:
            cursor.execute(
                f"INSERT INTO {table_name} VALUES ({','.join(['?']*len(row))})",
                row
            )
        conn.commit()
        return headers

def run_queries(conn, table_name, headers):
    cursor = conn.cursor()

    print("\n=== TOTAL ROW COUNT ===")
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    print(cursor.fetchone()[0])

    print("\n=== FIRST 10 ROWS ===")
    cursor.execute(f"SELECT * FROM {table_name} LIMIT 10")
    for row in cursor.fetchall():
        print(row)

    print("\n=== GROUP BY COLUMN ===")
    print("Available columns:", headers)
    col = input("Enter column to group by (or leave blank to skip): ").strip()
    if col and col in headers:
        cursor.execute(f"SELECT {col}, COUNT(*) FROM {table_name} GROUP BY {col} ORDER BY COUNT(*) DESC LIMIT 10")
        for row in cursor.fetchall():
            print(row)
    else:
        print("Skipping group-by query.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python report_tool.py yourfile.csv")
        sys.exit(1)

    csv_path = sys.argv[1]
    if not os.path.exists(csv_path):
        print(f"File not found: {csv_path}")
        sys.exit(1)

    conn = sqlite3.connect(":memory:")
    try:
        headers = load_csv_to_sqlite(csv_path, conn)
        run_queries(conn, "data", headers)
    finally:
        conn.close()
