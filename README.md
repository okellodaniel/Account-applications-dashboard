# Account applications
_____

### Introduction
This is a project that is done in fulfilment of the data engineering zoomcamp course. It entails various technologies that are consumed to create a data pipeline and ingest a dataset from kaggle, clean, transform, analyse, aggregate the data and finally create a report.

### Problem statement
Uganda is currently in the midst of a transformative phase in digital banking. This transformation is characterized by the adoption of modern technologies for customer acquisition and account opening, including platforms like WhatsApp, mobile applications, web applications, and Unstructured Supplementary Service Data (USSD).
Despite these advancements, a significant challenge persists: there is limited visibility into the efficiency of these customer acquisition processes. Current systems offer little insight into the number of applications submitted, the various stages of the account opening process, demographic data of applicants, or regional distribution of applications by district.
This lack of transparency hinders the ability to make data-driven decisions and optimize processes. Therefore, this project aims to address this gap by creating a robust data pipeline. This pipeline will aggregate data into a centralized source, enabling the application of data engineering techniques to enhance data management.
Subsequently, data analytics methods will be employed to derive valuable business insights from this data. These insights will shed light on the efficiency of the account opening process, ultimately contributing to the optimization of digital banking services in Uganda.
This project aligns with the broader goal of leveraging technology to improve financial services, fostering economic growth, and enhancing the customer experience in the digital banking sector. By providing a clearer picture of the account opening process, we can help drive the digital banking transformation in Uganda forward.

### Architecture
The pipeline leverages the following tools:

- **[Kaggle](https://www.kaggle.com)**: Source of the datasets.
- **[Mage.ai](https://docs.mage.ai/introduction/overview)**: Data orchestration tool for automating data download and transformation, as well as exportation to the data warehouse.
- **[BigQuery](https://docs.mage.ai/introduction/overview)**: Cloud data warehouse for storing the transformed data, and transformed fact tables from DBT cloud.
- **[dbt](https://www.getdbt.com)**: Data transformation tool for building and running data models in BigQuery.
- **[Looker Studio](https://cloud.google.com/looker-studio?gad_source=1&gclid=CjwKCAjwoPOwBhAeEiwAJuXRh6oiq757A9yQTunwbkPM9JeszNWu1yQZWbyR3a3FDT_Zfdf4E0OuOhoCHQ4QAvD_BwE&gclsrc=aw.ds)**: Data visualization platform for creating interactive dashboards.

#### Pipeline Overview
- **Data Acquisition**: Mage.ai was leveraged to download the datasets from Kaggle, a kaggle.json file with the necessary credentials was used to facilitate this porcess.
- **Data Transformation**: Mage.ai was then used for preliminary cleaning, transformation of the dataset, and prepareation the data for loading into BigQuery (Exportation). All of this was achieved through a pipeline setup.
- **Data Storage**: The transformed data is loaded into BigQuery tables inside the customer-onboarding-applications schema.
- **Data Modeling**: dbt was leveraged for advance tranformation and data model creation on top of the BigQuery tables, creating metrics and dimensions for analysis.
- **Data Visualization**: Looker Studio connects to the dbt models in big query allowing for creation of an interactive dashboard.

#### Benefits of this architectural decision
- **Automation**: The pipeline automates data ingestion and transformation, reducing manual work and ensuring consistency.
- **Scalability**: The pipeline can handle large datasets and scale to accommodate future growth.
- **Flexibility**: dbt allows for complex data transformations and model creation.
- **Visualization**: Looker Studio provides a user-friendly interface for creating insightful dashboards.

### Getting Started

#### Pre-requisites
- Docker
- Docker Compose
- Google Cloud Platform account
- BigQuery
- dbt Cloud account
- Looker Studio account
- Kaggle account

#### Configuraitons
##### Mage.ai Docker Container
The Mage.ai framework is configured as a Docker container using a Docker Compose file. Ensure Docker and Docker Compose are installed on your machine.

##### BigQuery Access
Access to BigQuery requires access rights via a service account file. This file should be configured in the Mage.ai Docker container in the `/home/src/gcp-credentials-file.json` directory. The filename should be `gcp.json`.

##### Kaggle Dataset Access
Access to the Kaggle dataset is possible through a `kaggle.json` file that should be copied to the root of the Docker container at `/root/.kaggle/kaggle.json`.

##### dbt Cloud
The dbt Cloud version is used to create models and interact with the data exported to BigQuery. The transformed tables are moved back to BigQuery.

##### Looker Studio
Looker Studio is used to integrate with the tables in BigQuery for data visualization.

#### Instructions
1. [Clone](https://github.com/okellodaniel/account_applications_dashboard.git) this repository to your local machine.
2. Navigate to the directory containing the Docker Compose file.
3. Create a `.env` file and populate the POSTGRES database environment variables as shown below

    ```
    PROJECT_NAME=account_applications
    POSTGRES_DBNAME=postgres
    POSTGRES_SCHEMA=account_applications
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_HOST=postgres
    POSTGRES_PORT=5432
    ```
4. Create a secrets directory inside your Documents directory `~/Documents/secrets`
5. Create a `gcp-credentials-file.json` directory within the `secrets` directory and place your `gcp.json` file here. The gcp.json file should contain your google cloud service account key.
6. Create another directory `.kaggle`within the `secrets` and paste the `kaggle.json`.
7. Run `docker-compose up` to start the Mage.ai Docker container.
8. Configure the BigQuery service account file in the Mage.ai Docker container.
9. Copy the `kaggle.json` file to `/root/.kaggle/kaggle.json` in the Docker container.
10. Run your data pipeline scripts.
11. Use dbt Cloud to create models with the data in BigQuery.
12. Use Looker Studio to visualize the data in BigQuery.

## glossary
- [dbt documentation](https://cloud.getdbt.com/accounts/256688/develop/6374590/docs/index.html)
### Report
[report link](https://lookerstudio.google.com/reporting/80714f83-2281-4a3b-8f40-d262a0b1f614)
![image](https://github.com/okellodaniel/customer_onboarding_applications/assets/43291086/22f5468f-2c2d-43e8-8edb-dda7003a5e41)
