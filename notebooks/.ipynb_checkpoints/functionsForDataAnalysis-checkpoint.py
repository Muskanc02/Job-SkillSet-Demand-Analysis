import re
skill_mapping_xx = {
    "Python": ["Python", "Pandas", "NumPy", "Numpy", "Scipy", "SciPy", "Scikit-learn", "scikit-learn", "PyTorch", "TensorFlow", "PySpark", "Jupyter"],
    "SQL": ["SQL", "MySQL", "PostgreSQL", "Postgres", "MSSQL", "MS SQL Server", "MS SQL Server (SSIS/SSAS)", "Snowflake", "Oracle", "MariaDB"],
    "Cloud": ["Cloud", "Google Cloud", "Google Cloud Platform", "GCP", "Microsoft Azure", "Azure", "AWS", "AWS Stack", "Lambda", "Kinesis", "Google Big Query", "BigQuery", "bigquery"],
    "Power BI": ["Power BI", "Microsoft Power BI", "PowerBI", "PowerBi", "MS Power BI"],
    "Tableau": ["Tableau"],
    "Excel": ["Excel", "Microsoft Excel", "Excel/Google Sheets", "Google Sheets"],
    "ETL": ["ETL", "ETL processes", "ETL pipelines", "ETL tools", "ETL-Pipelines", "ETL Tool"],
    "Data Engineering": ["Airflow", "dbt", "Glue", "Talend", "Athena", "Datalakehouse"],
    "Machine Learning": ["ML", "Machine Learning (ML)", "MLOps", "Large Language Models (LLMs)", "Predictive Analysis"],
    "Big Data": ["Spark", "Apache Spark", "Kafka", "Dask"],
    "Cloud Data Platforms": ["Cloud Data Platforms", "Snowflake", "BigQuery", "Google Big Query"],
    "DevOps": ["CI/CD", "Docker", "Kubernetes", "Git", "git", "GitLab", "Ansible", "Terraform"],
    "Statistics": ["Statistics", "A/B testing", "A/B tests", "Data Statistics"],
    "BI Tools": ["Business Intelligence Tool", "MicroStrategy", "Looker", "Qlik", "Qliksense", "QlickCloud", "SAP", "Salesforce", "Alteryx", "Google Data Studio"],
    "NLP": ["NLP", "Text Mining", "NLTK", "XGBoost"],
    "Programming": ["Java", "Scala", "MATLAB", "R", "R Programming", "Ruby", "Golang", "LUA", "C#", "Visual Basic"],
    "Data Science": ["Random Forest", "Decision Trees"],
    "AI & Deep Learning": ["Deep Learning", "Keras", "OpenCV", "Theano"],
    "APIs & Integration": ["REST API"],
    "Other Tools": ["Power Query", "DAX", "MDX", "KPI", "KPI dashboards"]
}

skill_mapping_extra = {
    "Python": ["Python", "Pandas", "NumPy", "Numpy"],
    "SQL": ["SQL", "MySQL", "MSSQL", "MS SQL Server", "Oracle", "MariaDB"],
    "R": ["R", "R Programming"],
    "Cloud Platforms": ["Cloud", "Google Cloud", "Google Cloud Platform", "GCP", "Google Big Query", "BigQuery", "bigquery"],
    "Power BI": ["Power BI", "Microsoft Power BI", "PowerBI", "PowerBi", "MS Power BI","Power Query", "DAX", "MDX"],
    "Tableau": ["Tableau"],
    "Excel": ["Excel", "Microsoft Excel", "Excel/Google Sheets", "Google Sheets"],
    "ETL Tools": ["ETL", "ETL processes", "ETL pipelines", "ETL tools", "ETL-Pipelines", "ETL Tool"],
    "Data Engineering": ["Airflow", "dbt", "Glue", "Talend", "Athena", "Datalakehouse","CI/CD", "Docker", "Kubernetes", "Git", "git", "GitLab", "Ansible", "Terraform"],
    "Machine Learning": ["ML", "Machine Learning (ML)", "MLOps", "Large Language Models (LLMs)", "Predictive Analysis","NLP", "Text Mining", "NLTK", "XGBoost","Random Forest", "Decision Trees","Deep Learning", "Keras", "OpenCV", "Theano","Scipy", "SciPy", "Scikit-learn", "scikit-learn", "PyTorch", "TensorFlow", "PySpark"],
    "Big Data": ["Spark", "Apache Spark", "Kafka", "Dask"],
    "Statistics": ["Statistics", "A/B testing", "A/B tests", "Data Statistics"],
    "BI Tools": ["Business Intelligence Tool", "MicroStrategy", "Looker", "Qlik", "Qliksense", "QlickCloud", "SAP", "Salesforce", "Alteryx", "Google Data Studio"],
    "Programming": ["Java", "Scala", "MATLAB", "Ruby", "Golang", "LUA", "C#", "Visual Basic","REST API"],
    "Other Tools": ["Power Query", "DAX", "MDX", "KPI", "KPI dashboards"]
}


skill_mapping = {
    "Python": ["Python", "Pandas", "NumPy", "Numpy"],
    "SQL": ["SQL", "MySQL", "MSSQL", "MS SQL Server", "Oracle", "MariaDB" ],
    "PostgresSQL":["Postgres","PostgreSQL"],
    "R": ["R", "R Programming"],
    "GCP": ["Cloud", "Google Cloud", "Google Cloud Platform", "GCP"],
    "BigQuery":["Google Big Query", "BigQuery", "bigquery","Bigquery","Google Big Querry"],
    "Azure":["Azure","Microsoft Azure"],
    "AWS":["AWS","Amazon Web Services"],
    "Power BI": ["Power BI", "Microsoft Power BI", "PowerBI", "PowerBi", "MS Power BI","Power Query", "DAX", "MDX"],
    "Tableau": ["Tableau"],
    "SAP":["SAP"],
    "Java":["Java"],
    "A/B testing":["A/B testing","A/B tests"],
    "Statistics":["Statistics","Data Statistics"],
    "Excel/Google Sheets": ["Excel", "Microsoft Excel", "Excel/Google Sheets", "Google Sheets"],
    "ETL Tools": ["ETL", "ETL processes", "ETL pipelines", "ETL tools", "ETL-Pipelines", "ETL Tool"],
    "Spark":["Apache Spark","Spark","PySSpark","Pyspark"],
    "Databricks":["Databricks"],
    "Snowflake":["Snowflake"],
    "CI/CD":["CI/CD"],
    "Statistics":["Statistics"],
    "MS Office":["MS Office"],
    "Scala":["Scala"],
    "Docker":["Docker","docker"],
    "ML":["ML","MLOps","Machine Learning (ML)","Large Language Models (LLMs)","predictive analysis"],
    "Kinesis":["Kinesis"],
    "MicroStrategy":["MicroStrategy"],
    "Quicksight":["Quicksight"],
    "git":["git","Git","GitLab"],
    "Google Data Studio":["Google Data Studio","Looker","DataStudio"],
    "MATLAB":["MATLAB"],
    "XGBoost":["XGBoost"],
    "Random Forest":["Random Forest"],
    "OLAP":["OLAP"],
    "Golang":["Golang"],
    "Exasol":["Exasol"],
    "NLTK/NLP":["NLTK","NLP"],
    "Ruby":["Ruby"],
    "MariaDB":["MariaDB"],
    "Scipy/scikit-learn":["Scipy","scikit-learn","Scikit-learn","SKLearn","SciPy"],
    "Qliksense":["Qliksense:","Qlik"],
    "dask":["dask"],
    "Decision Trees":["Decision Trees"],
    "Theano":["Theano"],
    "QlickCloud":["QlickCloud"],
    "DataStudio":["DataStudio"],
    "KPIs":["KPI dashboards","KPI","Kpi"],
    "Matomo":["Matomo"],
    "LUA":["LUA"],
    "Puppet":["Puppet"],
    "TensorFlow":["TensorFlow"],
    "PyTorch":["PyTorch"],
    "Airflow":["Airflow"],
    "Kafka":["Kafka"],
    "Kubernetes":["Kubernetes"],
    "SAS":["SAS"],
    "Terraform":["Terraform"],
    "dbt":["dbt"],
    "ERP":["ERP"],
    "Google Analytics":["Google Analytics","Google Analytics 4'"],
    "Adobe Analytics":["Adobe Analytics"],
    "Salesforce":["Salesforce"],
    "MongoDB":["MongoDB"],
    "Glue":["Glue"],
    "Julia":["Julia"],
    "Alteryx":["Alteryx"],
    "Athena":["Athena"],
    "Keras":["Keras"],
    "Lambda":["Lambda","AWS Stack"],
    "Talend":["Talend"],
    "Visual Basic":["Visual Basic"],
    "No-SQL":["No-SQL"],
    "OpenCV":["OpenCV"],
    "Census":["Census"]

}


# Function to categorize job titles based on keywords
def categorize_job_title(title):
    #title = title.lower()  # Convert to lowercase for case-insensitive comparison
    title = re.sub(r'[^\w\s]', '', title)
    if 'analyst' in title or 'Analyst' in title or 'Analysis' in title or 'analysis' in title or 'Analytics' in title or 'analytics' in title or 'Analista' in title or 'Consultor' in title or 'Consultant' in title or 'Reporting' in title or 'Datenanalyse' in title or 'Consulting' in title or 'ANALYST' in title:
        return 'Data Analyst'
    elif 'scientist' in title or 'Scientist' in title or 'Machine learning' in title or 'ML' in title or 'Machine Learning' in title or 'Science' in title or 'science' in title or 'Researcher'  in title or 'SCIENTIST' in title or 'MACHINE LEARNING ENGINEER' in title:
        return 'Data Scientist'
    elif 'engineer' in title or 'Engineer' in title:
        return 'Data Engineer'
    else:
        return 'Other'  # If no match, categorize as 'Other'

# 
#function to Map skill on one higher level
def map_skill_set(skill_set):
    mapped_skills = set()  # Use a set to avoid duplicates
    for skill in skill_set.split(','):  # Split by comma
        skill = skill.strip()  # Remove extra spaces
        for main_skill, variants in skill_mapping.items():
            if skill in variants:
                mapped_skills.add(main_skill)  # Add the mapped skill
                break  # Stop checking once mapped
    
    return ', '.join(mapped_skills)