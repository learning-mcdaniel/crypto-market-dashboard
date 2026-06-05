# Crypto Market Dashboard

## Overview

Crypto Market Dashboard is a Python-based analytics application that retrieves cryptocurrency prices from the CoinGecko API, stores historical data in a SQLite database, and displays interactive charts and metrics through a Streamlit dashboard.

This project demonstrates core data engineering and analytics concepts including:

- API data extraction
    
- Data loading and persistence
    
- Relational databases
    
- Data visualization
    
- Dashboard development
    
- Python automation
    

---

## Features

- Retrieve live cryptocurrency prices from CoinGecko
    
- Store historical price snapshots in SQLite
    
- View current Bitcoin and Ethereum prices
    
- Display historical price trends
    
- Filter data by cryptocurrency
    
- Interactive dashboard built with Streamlit
    

---

## Technology Stack

|Component|Technology|
|---|---|
|Language|Python 3|
|Dashboard|Streamlit|
|Data Processing|Pandas|
|Visualization|Plotly|
|Database|SQLite|
|API|CoinGecko|
|Version Control|Git|

---

## Project Structure

```text
crypto-dashboard/
│
├── app.py
│
├── data/
│   └── crypto.db
│
├── scripts/
│   ├── create_db.py
│   ├── extract.py
│   └── load.py
│
├── requirements.txt
│
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd crypto-dashboard
```

### Create Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate the environment:

Command Prompt:

```cmd
venv\Scripts\activate
```

PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Git Bash / MobaXterm:

```bash
source venv/Scripts/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Database Setup

Create the SQLite database:

```bash
python scripts/create_db.py
```

This creates:

```text
data/crypto.db
```

---

## Load Cryptocurrency Data

Run the data load script:

```bash
python scripts/load.py
```

Each execution inserts a new price snapshot into the database.

---

## Launch Dashboard

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

The dashboard will be available at:

```text
http://localhost:8501
```

![[dashboard.png]]


## Data Pipeline

```text
CoinGecko API
       │
       ▼
Data Extraction
       │
       ▼
SQLite Database
       │
       ▼
Pandas Data Processing
       │
       ▼
Streamlit Dashboard
```

---

## Example Workflow

1. Create the database.
    
2. Load cryptocurrency prices.
    
3. Launch the dashboard.
    
4. Repeat data loads periodically to build historical data.
    
5. Analyze price trends using the dashboard.
    

---

## Future Enhancements

### Analytics

- Date range filters
    
- Moving averages
    
- Daily percentage change
    
- Volatility metrics
    

### Data Engineering

- PostgreSQL backend
    
- Docker containerization
    
- Automated ETL scheduling
    
- Cloud deployment
    

### Dashboard

- Additional cryptocurrencies
    
- Real-time updates
    
- Portfolio tracking
    
- Custom alerts
    

---

## Learning Objectives

This project demonstrates practical experience with:

- Python programming
    
- REST APIs
    
- Database design
    
- ETL concepts
    
- Data visualization
    
- Dashboard development
    
- Version control with Git
    

---

## License

This project is provided for educational and portfolio purposes. 