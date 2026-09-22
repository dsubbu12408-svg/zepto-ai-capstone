\# Zepto AI Capstone - Data Pipeline



\## Module 1: Data Collection, Cleaning and SQL Analysis



This module collects, cleans and analyzes book data using Python, Pandas and SQLite.



\## Dataset



\- Total books collected: 100

\- Categories represented: 14

\- Raw dataset: books.csv

\- Cleaned dataset: books\_cleaned.csv



\## Data Cleaning



The pipeline performs:



\- Price cleaning and conversion to numeric GBP

\- GBP to INR conversion

\- Rating conversion from words to numbers

\- Availability conversion to True/False

\- Category preservation

\- Cleaned dataset generation



\## Files



\- books.csv - Raw scraped dataset

\- books\_cleaned.csv - Cleaned dataset

\- scraper.py - Data collection script

\- cleaner.py - Data cleaning script

\- database.py - SQLite database creation

\- queries.py - SQL and Pandas analysis queries

\- books.db - SQLite database

\- config.py - Configuration

\- requirements.txt - Python dependencies



\## SQLite Database



The database contains two related tables.



\### categories



\- category\_id - Primary Key

\- category\_name - Category name



\### books



\- book\_id - Primary Key

\- title

\- price\_gbp

\- price\_inr

\- rating

\- in\_stock

\- category\_id - Foreign Key



The books.category\_id references categories.category\_id.



\## SQL Analysis



The project includes more than five SQL queries:



1\. Total number of books

2\. Average price in INR

3\. Books grouped by rating

4\. Books grouped by category

5\. Number of books in stock

6\. Top 10 expensive books

7\. Books joined with categories



Query results are loaded using pandas.read\_sql().



\## JOIN and pandas.merge



The SQL JOIN between books and categories is reproduced using pandas.merge().



\## How to Run



\### Clean the data



```bash

python cleaner.py

## Module 1 Completion Summary

Module 1 has been completed successfully.

The completed work includes automated web scraping, data collection, data cleaning and transformation, Pandas analysis, SQLite database storage, SQL queries, JOIN operations, Pandas `read_sql()` and `merge()`, and analysis of book categories, prices, ratings, and availability.

All Module 1 deliverables have been documented and committed to the GitHub repository.
