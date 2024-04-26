Certainly! Here's a README summary for your MongoDB-based data analysis project:

---

## MongoDB City Inspections Analysis

### Project Overview

This project involves the analysis of city inspection data using MongoDB, a NoSQL database, to perform queries and aggregations. We utilize data from city inspections for the years 2015 and 2016 to explore inspection patterns, identify violations, and provide insights into business compliance across various regions.

### Key Features

- **Data Import:** Scripts to import JSON data into MongoDB, transforming each data point into a document within a MongoDB collection.
- **Inspection Analysis:** Capabilities to count total inspections, analyze yearly inspection data, and extract specific business information.
- **Violation Detection:** An interactive prompt for users to check if a business has any violations, with case-sensitive search functionality.
- **Regional Violation Summary:** Detailed reports on business violations in Brooklyn and Bronx, including address information and violation counts.
- **Zip-Code Search:** User-driven searches to find the number of businesses within a given zip-code, featuring a random selection of business names.
- **Flushing Business Report:** (For teams of three) Insights on businesses located in Flushing, with details on those with violations.

### Getting Started

#### Prequisites

- MongoDB
- Python 3.8 or higher
- Python libraries: `pymongo`, `json`, `random`

#### Installation and Setup

1. Ensure MongoDB is installed and running on your system.
2. Clone the repository and navigate to the project directory.
3. Install the required Python libraries using `pip install -r requirements.txt`.
4. Use the provided scripts to import the JSON data into your MongoDB instance.

### Usage

- Run `import_data.py` to load the inspection data into MongoDB.
- Execute `inspection_count.py` to get the total number of inspections and yearly breakdown.
- Use `business_check.py` to input a business name and receive violation status.
- Invoke `regional_violations.py` to analyze violations by region.
- Run `zipcode_businesses.py` for the total number of businesses and a random list of names within a zip-code.
- `flushing_businesses.py` provides additional analysis for Flushing area.
