# NYU Events Scraper

## Executive Summary
This project provides an automated pipeline to collect and clean even data from the [NYU Events Calendar](https://events.nyu.edu/).

**Motivation / Problem Statement:**  
NYU hosts hundreds of events each semester, but browsing them online can be difficult due to fragmented categories, limited filtering, and lack of export options. By building a scraper + validation pipeline, this project makes event data **searchable, analyzable, and reusable** 
Our goals:
- Collect event metadata (title, date/time, location, URL, description).  
- Standardize and validate data quality.  
- Transform into clean JSON/CSV files for downstream applications.  
-  Ensure reliability through retries, deduplication, and flexible output.  

This tool saves time for students, staff, and developers who want structured access to NYU’s event data.

---

## 🛠 Technical Architecture

The system consists of **three main stages**:

```mermaid
flowchart TD
    A[NYU Events Website] --> B[Selenium Scraper]
    B --> C[Validators.py: Data Quality Checks]
    C --> D[Data Transformers: Normalize + Enrich]
    D --> E[Export via JSON + CSV]
    E --> F[Data Folder for Storage]

--- 

## Setup and Deployment Instructions

### 1. Clone Repository
```bash
git clone https://github.com/<your-username>/PIP-assignment-2.git
cd PIP-assignment-2

### 2. Create Virtual Environment

### 3. Install Dependencies 
pip install -r requirements.txt

### 4. Run Scraper
python3 src/main.py

### 5.Output Files

After running you'll find the raw data json file, along with transformed version of the data in both json and csv, all found within the data folder
