import pandas as pd
import json
import os
from langdetect import detect, DetectorFactory
import re
# Ensure consistent language detection
DetectorFactory.seed = 0  


# List of relevant skills to ensure they appear
predefined_skills = ['Tableau', 'TABLEAU','Power BI', 'PowerBI','Python', 'SQL', 'Java','PowerBi','Microsoft Power Bi','ETL Tool',
                    'Azure', 'AWS','SAP','Cloud', 'R','Excel', 'A/B testing','ETL','Bigquery','Google Analytics','Looker','DataStudio','BigQuery','Postgres','Scala','MS-SQL'
                    'Redshift','Google Data Studio', 'Databricks','Pandas','NumPy','Numpy','Ruby','Google Cloud','Google cloud','Googlecloud','GoogleCloud','Airflow',
                    'scikit-learn','Scikit-learn','Scikit','scikit','sci-kit','Sci-kit','Sci-Kit','Git','GitLab','gitlab','ETL-Pipelines','MariaDB','Oracle',
                    'Jupyter','git','docker','MS SQL Server','SQL','CI/CD','cloud data platforms','SAS','Microsoft Excel','Google Sheets',
                    'A/B testing','QlickCloud','ERP','Adobe Analytics','REST API','No-SQL','Amazon Web Sevices','PostgreSQL','Google Data Studio'
                    'Azure Data Stack','Alteryx',' DAX','MDX','Qlik','Business Intelligence Tool','QlickCloud','Microsoft Power BI','A/B tests',
                    'MS Power BI','Power Query','Snowflake','ETL tools','Census','dbt','OLAP','ETL processes','KPI dashboards',
                    'KPI','MS Office','Excel','SAP','Databricks','Google Data Studio','Salesforce','Matomo','Google Analytics 4','Google Big Querry',
                    'Excel/Google Sheets','MySQL','Data Mining','Statistics','Data Statistics','AWS Stack','Glue', 'Lambda', 'Athena', 'Quicksight','LUA',
                    'GCP','Scala','Talend','Microsoft Azure','Terraform','Kinesis','Spark','Salesforce','Kafka','MongoDB','C#','MS SQL Server (SSIS/SSAS)',
                    'PySpark','Microsoft Azure','CI/CD','Apache Spark','ETL pipelines','Airflow','Kubernetes','Scala','Google Cloud Platform','Exasol',
                    'Docker','Terraform','Puppet','Ansible','Golang','Ruby','MicroStrategy',
                    'Machine Learning (ML)','Large Language Models (LLMs)','Datalakehouse','ML','LLMs','data visualization tools','BI Tools','Business Intelligence Tools'
                    'Gitlab','MATLAB','R','Julia','dask','GCP Vertex AI','Amazon SageMaker','Predictive Modelling'
                    'Scikit-Learn', 'Scikit-learn','Keras', 'PyTorch', 'TensorFlow','SKLearn', 'SciPy','Scipy','MLOps','Spacy', 'NLTK', 'OpenCV','NLP',
                    'artificial neural networks','Generative AI','Linear Regression', 'Logistic Regression', 'Decision Trees', 'Random Forest', 'XGBoost',
                    'sci-kit-learn','predictive analysis','Theano','Text Mining','Text processing','Visual Basic','Pyspark:','Qliksense:','Spark']




# Predefined industries with associated keywords in English , German & Spanish
industry_keywords_English = {
                    "Healthcare": ["healthcare", "medical", "hospital", "patient", "pharma"],
                    "Banking & Financial Services": ["banking", "fintech", "financial", "insurance", "investment"],
                    "Telecom": ["telecom", "5g", "network", "communications", "wireless"],
                    "Travel": ["travel", "tourism", "hospitality", "airlines", "vacation"],
                    "Product": ["product", "software", "SaaS", "tech company", "cloud"],
                    "Sales & Marketing":["web tracking","advertisement","marketing","advertisements","sales","Markets","Customer","customer experience"],
                    "AI":["Artificial","Artificial Intelligence","AI","Machine learning","chatbots"],
                    "Digital":["digital","digital transformation","technology","transformation"],
                    "Consulting":["Advisory","consulting","consultancy","clients"],
                    "IT":["IT","Information and Technology"],
                    "Unknown": []  # Default category
                    }
industry_keywords_German = {
                    "Healthcare": ["gesundheitswesen", "medizinisch", "krankenhaus", "patient", "pharma"],
                    "Banking & Financial Services": ["bankwesen", "fintech", "finanziell", "versicherung", "investition"],
                    "Telecom": ["telekommunikation", "5g", "netzwerk", "kommunikation", "drahtlos"],
                    "Travel": ["reisen", "tourismus", "gastgewerbe", "fluggesellschaften", "urlaub"],
                    "Product": ["produkt", "software", "saas", "tech-unternehmen", "cloud"],
                    "Sales & Marketing": ["web-tracking", "werbung", "marketing", "anzeigen", "vertrieb", "märkte", "kunde", "kundenerfahrung"],
                    "AI": ["Künstlich", "Künstliche Intelligenz", "KI", "Maschinelles Lernen", "Chatbots"],
                    "Digital": ["digital", "digitale Transformation", "Technologie","transformación"],
                    "Consulting": ["Beratung", "Beratung", "Beratung", "Kunden"],
                    "IT": ["IT", "Information und Technologie"],
                    "Unknown": []  # Default category
                    }
industry_keywords_Spanish ={
                  "Healthcare": ["salud", "médico", "hospital", "paciente", "farmacéutica"],
                  "Banking & Financial Services": ["banca", "fintech", "financiero", "seguros", "inversión"],
                  "Telecom": ["telecomunicaciones", "5g", "red", "comunicaciones", "inalámbrico"],
                  "Travel": ["viaje", "turismo", "hospitalidad", "aerolíneas", "vacaciones"],
                  "Product": ["producto", "software", "SaaS", "empresa tecnológica", "nube"],
                  "Sales & Marketing": ["seguimiento web", "publicidad", "marketing", "anuncios", "ventas", "mercados", "cliente", "experiencia del cliente"],
                  "AI": ["Artificial", "Inteligencia Artificial", "IA", "aprendizaje automático", "chatbots"],
                  "Digital": ["digital", "transformación digital", "tecnología", "transformación"],
                  "Consulting": ["asesoría", "consultoría", "consultoría", "clientes"],
                  "IT": ["TI", "información y tecnología"],
                  "Unknown": []
                    }

# Merge dictionaries by combining the keyword lists
combined_industry_keywords = {
    key: industry_keywords_English.get(key, []) + industry_keywords_German.get(key, []) + industry_keywords_Spanish.get(key, [])
    for key in set(industry_keywords_English) | set(industry_keywords_German) | set(industry_keywords_Spanish)
}


location_to_country = {
    'Germany': 'Germany',
    'Greater Dusseldorf Area': 'Germany',
    'Frankfurt Rhine-Main Metropolitan Area': 'Germany',
    'Cologne Bonn Region': 'Germany',
    'Greater Munich Metropolitan Area': 'Germany',
    'Greater Bremen Area': 'Germany',
    'Osnabrück Land': 'Germany',
    'Greater Hamburg Area': 'Germany',
    'Greater Koblenz Area': 'Germany',
    'Hannover-Braunschweig-Göttingen-Wolfsburg Region': 'Germany',
    'Stuttgart Region': 'Germany',
    'Greater Dresden Area': 'Germany',
    'Greater Karlsruhe Area': 'Germany',
    'Saarland': 'Germany',
    'Germany On-site': 'Germany',
    'Greater Kassel Area': 'Germany',
    'Greater Nuremberg Metropolitan Area': 'Germany',
    'Berlin Metropolitan Area': 'Germany',
    'Greater Leipzig Area': 'Germany',
    'Greater Kiel Area': 'Germany',
    'Ruhr Region': 'Germany',
    'Spain': 'Spain',
    'Greater Madrid Metropolitan Area': 'Spain',
    'Greater Sevilla Metropolitan Area': 'Spain',
    'Greater Gijón Metropolitan Area': 'Spain',
    'Greater Barcelona Metropolitan Area': 'Spain',
    'Greater Girona Area': 'Spain',
    'Greater Bilbao Metropolitan Area': 'Spain',
    'Greater Málaga Metropolitan Area': 'Spain',
    'EMEA': 'EMEA',
    'European Economic Area': 'European Economic Area',
    'European Union': 'European Union'
}





# Function to find industry type
def detect_industry(description):
    if pd.isna(description):  # If job description is missing
        return "Unknown"
    
    description_lower = description.lower()  # Convert to lowercase for case-insensitive matching
    
    for industry, keywords in combined_industry_keywords.items():
        if any(keyword in description_lower for keyword in keywords):
            return industry
    
    return "Unknown"  # If no industry is matched


# Function to extract matching skills
def extract_skills(description):
    if pd.isna(description):
        return "None"

    found_skills = set()
    for skill in predefined_skills:
        if skill == "R":
            # Ensure "R" is matched as a standalone word (surrounded by space, comma, or punctuation)
            if re.search(r'\bR\b', description):
                found_skills.add("R")
        else:
            # Match other skills normally
            if re.search(r'(^|\s|,)' + re.escape(skill) + r'(:|,|\.|\s|$)', description):
                found_skills.add(skill)

    return ", ".join(found_skills) if found_skills else "None"
              

#Function to join all Jsonss
def joinAllJsonToDF()->pd.DataFrame :
    # Folder where all JSON files are stored
    folders = ["/Users/muskanchawla/Documents/IronHack/Bootcamp/Week8/Final_Project/data/raw/json/Germany",
                   "/Users/muskanchawla/Documents/IronHack/Bootcamp/Week8/Final_Project/data/raw/json/Spain"]
    
    # List to store DataFrames
    dfs = []
    
    # Loop through all JSON files in the folders mentioned above
    for json_folder in folders:
        for file in os.listdir(json_folder):
            if file.endswith(".json"):  
                file_path = os.path.join(json_folder, file)
                print(f" reading json {file_path} ")
                # Load JSON file
                with open(file_path, "r", encoding="utf-8") as f:
                    job_data = json.load(f)
        
                # Convert JSON dictionary to DataFrame
                df = pd.DataFrame.from_dict(job_data, orient="index").reset_index()
        
                # Rename 'index' column to 'job_id'
                df.rename(columns={"index": "job_id"}, inplace=True)
        
                # Convert job_id to string
                df["job_id"] = df["job_id"].astype(str)
        
                # Append DataFrame to the list
                dfs.append(df)
    
    # Merge all DataFrames into a single DataFrame
    final_df = pd.concat(dfs, ignore_index=True)
    
    return final_df



# Function to determine  required language for Job Listings
def detect_language(text):
    if not isinstance(text, str) or text.strip() == "":
        return "Unknown"

    text_lower = text.lower()  # Convert to lowercase for uniform matching

    # Check explicit language requirements first
    if re.search(r"deutsch\s*(c1|b2|c2|b1|a1|a2|required|erforderlich)", text_lower):
        return "German Required"
    elif re.search(r"english\s*(c1|b2|c2|b1|a1|a2|required)", text_lower):
        return "English Required"
    elif "english and deutsch" in text_lower or "deutsch and english" in text_lower or  "deutsch und englisch" in text_lower:
        return "English & German"
    elif re.search(r"español\s*(c1|b2|c2|b1|a1|a2|required|requerido)", text_lower):
        return "Spanish Required"

    # If no explicit mention, use language detection
    try:
        lang = detect(text)
        if lang == "de":
            return "German"
        elif lang == "en":
            return "English"
        elif lang == "es":
            return "Spanish"
        else:
            return "Other"
    except:
        return "Unknown"

# Function to split location into City, District, and Country
def split_location(location):
    parts = location.split(", ")  # Split by ", "
    
    if len(parts) == 3:
        city, district, country = parts
    elif len(parts) == 2:
        city, district, country = parts[0], None, parts[1]  # No district
    elif len(parts) == 1:
        city, district, country = None, None, parts[0]  # Only country
    else:
        city, district, country = None, None, None  # Handle unexpected cases
    
    return pd.Series([city, district, country])