# IFB Service Operations Analytics

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange?logo=mysql)
![Tableau](https://img.shields.io/badge/Tableau-Public-lightblue?logo=tableau)
![SQL](https://img.shields.io/badge/SQL-Advanced-green)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

## Project Overview

An end-to-end service operations analytics system built on **real operational data** from IFB Industries. This project covers the full data analyst workflow — from raw CSV ingestion to an interactive executive dashboard — demonstrating production-level skills in Python, SQL, data modeling, and Tableau.

> **Business Problem:** IFB's service operations team needed visibility into technician productivity, pending call backlogs, repeat service failures, and branch-level performance across multiple franchise locations — all currently tracked manually in spreadsheets.

> **Solution:** Built a star-schema MySQL data warehouse fed by a Python ETL pipeline, with interactive Tableau dashboards enabling real-time operational monitoring.

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Data Ingestion & Cleaning | Python (Pandas, SQLAlchemy) |
| Database | MySQL 8.0 |
| Data Modeling | Star Schema (Fact + Dimension Tables) |
| Analytics | Advanced SQL |
| Visualization | Tableau Public |
| Version Control | Git, GitHub |

---

## Architecture

```
Raw CSV Files
      ↓
Python ETL (Pandas - Clean, Transform, Load)
      ↓
MySQL Data Warehouse (Star Schema)
      ↓
Advanced SQL Analytics Queries
      ↓
Tableau Interactive Dashboards
```

---

## Data Model — Star Schema

```
                    dim_branch
                        |
dim_technician — fact_pending_calls — dim_product
                        |
                   dim_franchise
```

**Fact Table:** `fact_pending_calls` — 5,000 service records

**Dimension Tables:**
- `dim_branch` — 4 service branches
- `dim_franchise` — 5 franchise partners per branch
- `dim_product` — 5 product categories (AC, REF, WM, DW, MWO)
- `dim_technician` — all field technicians

---

## Dashboards

### Dashboard 1 — Executive Operations Overview
**KPIs:** Total Calls | Closed Tickets | Avg Delay Hours | Repeat Call %

**Charts:**
- Branch-wise Pending Workload (stacked by status)
- Product Failure Analysis (volume by product + status)
- Compliant Density Heatmap (pincode-level service distribution across India)
- Repeat Failure Zones (geographic map of repeat service hotspots)

### Dashboard 2 — Field Performance
**Charts:**
- Technician Productivity (ranked by ticket volume + closure rate)
- Worst Performing Branches (pending calls + repeat % by franchise)
- Repeat Failure Zones Map (filtered to repeat calls only)

**Interactive Filters:** Branch, Product, Franchise Name, Technician, Status

---

## Key Business Questions Answered

- Which branches have the highest pending call backlog?
- Which technicians have the lowest closure rates?
- Which products generate the most repeat service calls?
- Which geographic zones have the highest service failure density?
- Which franchise-branch combinations are underperforming?
- What is the average delay between call booking and scheduled visit?

---

## SQL Analytics Highlights

```sql
-- Technician Productivity Score
SELECT 
    t.technician_name,
    COUNT(*) AS total_calls,
    SUM(CASE WHEN f.status = 'Closed' THEN 1 ELSE 0 END) AS closed_calls,
    ROUND(SUM(CASE WHEN f.status = 'Closed' THEN 1 ELSE 0 END) 
          / COUNT(*) * 100, 2) AS productivity_pct
FROM fact_pending_calls f
JOIN dim_technician t ON f.technician_id = t.technician_id
GROUP BY t.technician_name
ORDER BY productivity_pct DESC;
```

```sql
-- Branch Risk Analysis
SELECT 
    b.branch_name,
    COUNT(*) AS total_calls,
    SUM(CASE WHEN f.repeat_call_flag = 'Yes' THEN 1 ELSE 0 END) AS repeat_calls,
    AVG(f.delay_hours) AS avg_delay_hours
FROM fact_pending_calls f
JOIN dim_branch b ON f.branch_id = b.branch_id
GROUP BY b.branch_name
ORDER BY repeat_calls DESC;
```

---

## Repository Structure

```
IFB-Service-Analytics/
├── SQL/                        # Schema creation + analytics queries
├── Scripts/                    # Python ETL pipeline
├── Dashboard/                  # Tableau workbook (.twb)
├── Screenshots/                # Dashboard exports
├── Data/                       # Raw and cleaned data
├── Notebook/                   # EDA notebooks
└── README.md
```

---

## How to Run This Project

**1. Set up MySQL database**
```sql
CREATE DATABASE ifb_service_analytics;
```

**2. Run Python ETL script**
```bash
python Scripts/import_pending_calls.py
```

**3. Execute SQL schema files in order**
```
SQL/01_create_schema.sql
SQL/02_populate_dimensions.sql
SQL/03_populate_fact.sql
```

**4. Open Tableau workbook**
Connect to MySQL → localhost → ifb_service_analytics → Open Dashboard/.twb file

---

## About

Built as a portfolio project to demonstrate end-to-end data analytics capability using real service operations data from IFB Industries.

**Author:** Anubhav Chakraborty  
**LinkedIn:** [https://www.linkedin.com/in/anubhav-chakraborty-analyst/]  
**Google Data Analytics Certificate:** [https://coursera.org/share/a0183dd0523660090c1ee7eae9cda821]
