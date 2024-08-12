# Python-Projects

## Tax Fraud Detection System

### Problem Statement
Our tax system is a web-based platform that processes e-files, forwarding them to the relevant Taxing Authorities. Suspicious e-files are flagged for further analysis by a fraud investigator, but many of these turn out to be legitimate. We need a more sophisticated system to reduce the false positives and potentially uncover new suspicious scenarios.

### Approach

#### Data Processing Overview

This document outlines the key steps taken to process the dataset, preparing it for analysis and machine learning tasks.

#### 1. Data Cleaning
We began by sanitizing the dataset to remove any hyphens within specific columns. This was done to ensure consistency and prevent potential issues during data processing. This step was crucial for ensuring that the columns containing identifiers and account numbers were properly formatted and ready for analysis.

#### 2. Feature Extraction and Transformation
Next, we created a new DataFrame by extracting and transforming key features from the original dataset:
- **Datetime Components**: The `FILED_DATETIME` column, originally storing complete timestamps, was split into its constituent parts: `DAY`, `MONTH`, `YEAR`, and `HOUR`.
- **Direct Transfer**: Other relevant columns, such as `TAX_YEAR`, `REFUND`, and `ZIPCODE`, were directly transferred into the new DataFrame.

This process helped to isolate important aspects of the data, preparing them for further analysis.

#### 3. Encoding Categorical Data
To prepare the data for machine learning models, we converted textual categorical data into numerical representations using `LabelEncoders`. This involved assigning a unique integer to each unique value within the specified columns. By transforming text data into numerical form, we ensured that it could be effectively used in subsequent computational processes, such as model training.

#### 4. Data Splitting and Shuffling
Finally, we divided the dataset into two main categories: suspicious and not suspicious entries. After categorizing the data, we further split each category into training and evaluation sets. To ensure that the training process was unbiased and robust:
- **Concatenation and Shuffling**: We concatenated and shuffled these sets before beginning the training phase.

This step was vital for maintaining the integrity and reliability of the model’s performance during evaluation.

### Work in Progress
This project is currently under development, with ongoing improvements being made to enhance the detection system's accuracy and efficiency.
