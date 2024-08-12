# Python-Projects

Tax Fraud Detection System

Problem Statement: Our tax system is a web-based system that processes e-files, forwarding them to the relevant Taxing Authorities. Suspicious e-files are flagged for further analysis by a fraud investigator, but many of these turn out to be legitimate. We need a more sophisticated system to reduce the false positives and potentially uncover new suspicious scenarios.

Approach: 
Data Cleaning: We began by sanitizing the dataset to remove any hyphens within specific columns. This was done to ensure consistency and prevent potential issues during data processing. This step was crucial for ensuring that the columns containing identifiers and account numbers were properly formatted and ready for analysis.
Feature Extraction and Transformation: Next, we created a new DataFrame by extracting and transforming key features from the original dataset. For example, the FILED_DATETIME column, which originally stored complete timestamps, was split into its constituent parts: day, month, year, and hour. Additionally, we directly transferred other relevant columns such as TAX_YEAR, REFUND, and ZIPCODE into the new DataFrame. This process helped to isolate important aspects of the data and prepare them for further analysis.
Encoding Categorical Data: To prepare the data for machine learning models, we converted textual categorical data into numerical representations using LabelEncoders. This process involved assigning a unique integer to each unique value within the specified columns. By transforming text data into numerical form, we ensured that it could be effectively used in subsequent computational processes, such as model training.
Data Splitting and Shuffling: Finally, we divided the dataset into two main categories: suspicious and not suspicious entries. After categorizing the data, we further split each category into training and evaluation sets. To ensure that the training process was unbiased and robust, we concatenated and shuffled these sets before beginning the training phase. This step was vital for maintaining the integrity and reliability of the model’s performance during evaluation.

Future Work



# Work in progress
