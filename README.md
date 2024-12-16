# Kai and Karo Scraper

## Overview

**Kai and Karo Scraper** is a Python project designed to extract detailed vehicle information from the Kai and Karo website. It uses `requests` and `BeautifulSoup` to fetch and parse vehicle data, which is then structured into a CSV file for analysis or further use.

---

## Features

- Scrapes the following vehicle details:
  - Car Make
  - Year
  - Price
  - Drive Type
  - Transmission
  - Mileage
  - Torque
  - Descriptions
  - Horse Power
  - fuel type
  - acceleration
  - engine capacity
- Supports pagination for retrieving data across multiple pages.
- Includes robust error handling and retry mechanisms.I used multireading with Threadpool also with retries i.e incase of an error,a request is sent again to the link upto the 10th time.
- Saves the data into a CSV file for easy access.

---

## Technologies Used

- **Python**: Core programming language.
- **BeautifulSoup**: For HTML parsing.
- **Requests**: For sending HTTP requests.
- **Pandas**: For data handling and CSV file creation.
- **Logging**: For tracking the scraping process.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/kai-and-karo-scraper.git
   cd kai-and-karo-scraper

