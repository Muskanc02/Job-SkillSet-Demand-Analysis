# Job Skills & Demand Analysis from LinkedIn Job Listings

## Overview
This project involves web scraping job listings from LinkedIn to analyze the demand for various data-related roles. The automated script collects job data for **Data Analyst, Data Scientist, and Data Engineer** roles, providing insights into job trends, required skills, and industry demands.

## Data Collection
- **Platform:** LinkedIn
- **Job Titles Scraped:**
  - Data Analyst
  - Data Scientist
  - Data Engineer
- **Total Listings Scraped:** ~4372 for Germany and Spain.
- ** Saving cookies:** The cookies are saved for login details on LinkedIN with username and password using a pickle file.
- **Pagination Handling:** The script navigates through **40 pages** per job title.
- **Scrolling & Loading:** Implemented scrolling and wait time to ensure all job listings load before moving to the next page.

## Technologies Used
- **Python** (for automation & data processing)
- **Selenium** (for web scraping)
- **ChromeDriver Installer** (to automate browser interactions)
- **UV (Unplugged Virtual Environments)** (for managing dependencies)

## Project Environment & Dependencies
A **project environment** was created using **uv**, which helps manage dependencies efficiently. The required dependencies are listed below and can be installed using a `pyproject.toml` file.

### Dependencies
```toml
dependencies = [
    "numpy>=2.0.2",
    "pandas>=2.2.3",
    "matplotlib>=3.9.2",
    "seaborn>=0.13.2",
    "jupyter>=1.1.1",
    "ipykernel>=6.29.5",
    "selenium>=4.0.0",  # Added Selenium
    "webdriver_manager>=4.0.0",
    "langdetect>=1.0.9",
    "wordcloud>=1.9.4",
    "statsmodels>=0.14.4",
    "matplotlib-venn>=1.1.2"
]
```

## Exploratory Data Analysis (EDA)
After collecting the job data, **Exploratory Data Analysis (EDA)** was performed to identify trends and insights. The following techniques were used:
- **Data Cleaning:** Removed duplicates, handled missing values, and standardized job titles.
- **Skill Analysis:** Extracted key skills mentioned in job descriptions using text analysis.
-**Regex-based Skill Extraction: Used regular expressions (regex) to search for specific skill keywords within job descriptions and stored the extracted skills corresponding to each job ID.
- **Job SKILL SET Demand:** Visualized demand for different roles in Data Anaytics and across two locations I.e GERMANY and SPAIN
- **Skill and in demand Gap analysis :Coverage for skill sets in the boot camps for different job roles.

### Data Visualizations in Python
To better understand the data, multiple visualizations were created using **Matplotlib, Seaborn, and additional libraries:**
- **Word Clouds** (`wordcloud`) to highlight the most frequently mentioned skills.
- **Statistical Analysis** (`statsmodels`) to identify significant trends.
- **Venn Diagrams** (`matplotlib-venn`) to compare skill overlaps between job roles.
- **Bar Charts & Heatmaps** (`matplotlib` & `seaborn`) to visualize job distribution, required skills, and company trends.

## Tableau Dashboard
To make the insights more interactive, a **Tableau dashboard** was created. The dashboard includes:
- **Job Market Skill Set Analysis:** View of how the skill sets are in demand according to current Job postings on LinkedIn for below three roles.:
Data ANALYST
Data ENGINEER
Data SCIENTIST


- **Skill Frequency Analysis:** A breakdown of the most requested skills across roles.

https://public.tableau.com/app/profile/muskan.chawla2373/viz/JobListingAnalysis_17417071327610/Dashboard1?publish=yes
Also available as tableau work book in git hub repo.

Presentation Link : https://docs.google.com/presentation/d/12E7MEW84s4_W8v-4T5Ldzq2DhbVKjqFdJgOeIMZZ-ak/edit#slide=id.g33f481e1cda_0_37

## How to Run the Script
1. Install dependencies:
   ```sh
   uv pip install -r project.toml
   ```
2. Ensure you have **Google Chrome** installed.
3. Run the script:
   ```sh
   python GetLinkedInJobListings.ipynb
   ```
4. The output will be stored in a CSV/JSON file for further analysis.

## Future Enhancements
- Expand job search to other platforms like **Indeed** and **Glassdoor**.
- Perform  text analysis on job descriptions using some Machine Learning Model to identify the most in-demand skills.
- Enhance Tableau dashboard with more advanced filters and real-time updates.

## Contact
For any queries or collaborations, feel free to reach out!
Muskan.chawla02@gmail.com

---

