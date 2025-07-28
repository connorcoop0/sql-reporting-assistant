# SQL Reporting Assistant

A simple Python tool to quickly analyze CSV files using SQL queries. Load your CSV data into an in-memory SQLite database and get instant insights.

## Features

- **Instant CSV Analysis**: Load any CSV file and get immediate statistics
- **Data Preview**: View the first 10 rows to understand your data structure
- **Group By Analysis**: Interactive column grouping with frequency counts
- **In-Memory Processing**: Fast analysis without creating temporary files
- **Error Handling**: Graceful handling of missing files and edge cases

## Quick Start

```bash
python report_tool.py your_data.csv
```

## What You'll Get

1. **Total Row Count** - See how much data you're working with
2. **Data Preview** - First 10 rows to understand the structure
3. **Interactive Analysis** - Choose any column to group by and see value frequencies

## Example Output

```
=== TOTAL ROW COUNT ===
1000

=== FIRST 10 ROWS ===
('John', 'Doe', 'Engineer', '50000')
('Jane', 'Smith', 'Manager', '75000')
...

=== GROUP BY COLUMN ===
Available columns: ['First_Name', 'Last_Name', 'Job_Title', 'Salary']
Enter column to group by (or leave blank to skip): Job_Title

('Engineer', 450)
('Manager', 200)
('Analyst', 350)
```

## Requirements

- Python 3.6+
- No external dependencies (uses built-in libraries only)

## How It Works

1. Loads your CSV file into an in-memory SQLite database
2. Automatically cleans column headers (removes spaces, special characters)
3. Provides interactive analysis options
4. All processing happens in memory for speed

## Use Cases

- Quick data exploration
- Understanding data distribution
- Finding most common values in categorical columns
- Getting basic statistics before deeper analysis
- Data quality checks

## License

MIT License - feel free to use and modify as needed!