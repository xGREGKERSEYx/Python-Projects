# Python-Projects

Tax Fraud Detection System

Problem Statement: Our tax system is a web-based system that processes e-files, forwarding them to the relevant Taxing Authorities. Suspicious e-files are flagged for further analysis by a fraud investigator, but many of these turn out to be legitimate. We need a more sophisticated system to reduce the false positives and potentially uncover new suspicious scenarios.

Approach
Our team explored various paths to find the best solution. Here’s what we did:
Data Relevance Assessment: We carefully considered the relevance of the given data. We analyzed the meaning of each feature in the e-files. We factored in business rules and constraints.
Algorithm Exploration: Since it’s a binary classification task, we experimented with different algorithms. We explored both traditional machine learning and deep learning approaches. After thorough evaluation, we chose a random forest model. Random forests use multiple decision trees and aggregate their results.
Handling Categorical Features: Many e-file features were categorical. Traditional ML algorithms don’t handle categorical data directly. We converted relevant categorical features into numerical representations without losing their significance.
Future Work


# Work in progress
