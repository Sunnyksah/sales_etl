# Sales ETL Pipeline

A modular ETL (Extract → Transform → Load) pipeline that processes raw sales data from CSV files, applies cleaning and transformation logic, and loads the results into a PostgreSQL database.

Built to demonstrate production-style data engineering practices: separation of concerns, configuration management, and a clean handoff between pipeline stages.

---

## What it does

| Stage | File | Description |
|-------|------|-------------|
| Extract | `extract/extract_csv.py` | Reads raw CSV into a pandas DataFrame |
| Transform | `transform/transform_sales.py` | Cleans data, fixes types, computes Revenue |
| Load | `load/load_postgres.py` | Writes clean data to PostgreSQL via SQLAlchemy |
| Orchestrate | `main.py` | Runs all three stages in order |
| Configure | `config.py` | Centralises paths and DB connection settings |

---

## Project structure
```
sales_etl/
├── data/
│   └── raw/
│       └── sales.csv            # raw input data (not tracked in git)
├── extract/
│   └── extract_csv.py           # extraction logic
├── transform/
│   └── transform_sales.py       # transformation and cleaning logic
├── load/
│   └── load_postgres.py         # PostgreSQL load logic
├── main.py                      # pipeline orchestrator
├── config.py                    # paths and DB connection config
├── requirements.txt
└── .gitignore
```

---

## Setup
```bash
# Clone the repo
git clone https://github.com/SunnyKsah/sales_etl.git
cd sales_etl

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

---

## Prerequisites

- Python 3.10+
- PostgreSQL installed and running locally
- A database created and connection details added to `config.py`
```python
# config.py
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "your_db_name",
    "user": "your_username",
    "password": "your_password"
}
```

> Never commit real credentials. Add `config.py` to `.gitignore` or use environment variables with `python-dotenv`.

---

## Run
```bash
python main.py
```

The pipeline runs all three stages in sequence and logs progress to the terminal.

---

## Transformation logic

The transform stage handles:

- **Type fixing** — converts date strings to `datetime`, numeric strings to `float`
- **Null handling** — drops or fills missing values depending on the column
- **Deduplication** — removes exact duplicate rows
- **Computed column** — calculates `Revenue = Quantity × Unit Price`
- **String standardisation** — strips whitespace, applies consistent casing to categorical columns

---

## Key concepts demonstrated

- **Modular ETL design** — each stage (extract, transform, load) is isolated in its own module, making each independently testable and replaceable
- **SQLAlchemy over raw psycopg2** — SQLAlchemy provides a database-agnostic ORM layer; swapping PostgreSQL for MySQL requires changing one connection string, not rewriting load logic
- **Config separation** — all environment-specific values live in `config.py`, not hardcoded across files
- **`if __name__ == "__main__"`** — `main.py` can be imported without auto-executing, which matters when scheduling with Airflow or cron
- **DataFrame as pipeline contract** — each stage receives and returns a DataFrame, making the interface between stages explicit and predictable

---

## Tech stack

- Python 3.10+
- pandas
- SQLAlchemy
- psycopg2
- PostgreSQL

---

## Roadmap

- [ ] Add logging with Python's `logging` module (replace print statements)
- [ ] Add CLI arguments with `argparse` to pass custom file paths
- [ ] Dockerise the pipeline
- [ ] Schedule with Apache Airflow


