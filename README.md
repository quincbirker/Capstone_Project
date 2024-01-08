# Hooked on Books
## A Book Recommender System

### Author: Quinci Birker

--------------------------------------------------------------------

## Introduction

This project aims to give people more incentive to pick up a book and start reading. It can be daunting to go out and purchase a book when you have no idea if you will like it or not. I want to give readers an easy way to know if a book is likely to be worth their time. 
From my own experience, I’m picky with what books I read. If I read a book that I don’t enjoy, I tend to give up on reading altogether and it can take months before I look for another book to read. By the end of this project, I hope to assist in someone's reading journey and get them hooked on books. 

This dataset is sourced from Goodreads, a well-known online book catalog website. It encompasses an extensive collection of over 52,000 books. Updated last on November 9, 2020, it provides a rich basis for this analysis. The beginning of this project delves into Exploratory Data Analysis (EDA), offering visuals and insights that set the stage for further investigation. The primary aim here is to thoroughly understand the dataset and craft hypotheses, laying the groundwork for developing a personalized book recommendation model. The baseline model employed is logistic regression, serving as a foundation for more sophisticated model iterations.

### The User

This model targets two main user groups:

1. Individual readers seeking personalized book recommendations. This recommendation system will be great for both reluctant and avid readers.
2. Bookstores aiming to enhance customer satisfaction and increase sales through better book suggestions. This model can be provided to customers to increase the likelihood of them enjoying the book and coming back for more.

### Big Idea

GPT
The fundamental idea is centered around a user-friendly interaction where individuals input specific details about a book, and in response, the model predicts whether it's recommendable or not. The ultimate objective is to streamline this process so that a user can simply scan a book, swiftly feed the necessary information into the model, and promptly receive a recommendation. Additionally, if the model advises against a particular book, it will suggest an alternative book that aligns with the user's preferences and resembles the book initially scanned. This system aims to enhance the reading experience by guiding users towards books they are more likely to enjoy.

--------------------------------------------------------------------
## Table of Contents

1. Project Organization
2. Data Cleaning, Preprocessing, & Feature Engineering
3. Modeling
4. Challenges and Future Steps
5. Dataset Overview

--------------------------------------------------------------------

## Project Organization

README.md - The main README document for an overview of my project

Folder: Notebooks 
1. EDA_&_Baseline_Modeling.ipynb - EDA, data cleaning/preprocessing, feature engineering, baseline model
2. Advanced_Modeling-Part_1.ipynb - Advanced modeling, error analysis, feature importance
3. Feature_Engineering-Part_2.ipynb - Continued feature engineering, specifically dealing with the 'desciption' and 'publisher' columns
4. Advanced_Modeling_Final.ipynb - Advanced modeling with the new features added, error analysis, feature importance
5. Hooked_on_Books_App.py - App (not fully complete)

Folder: Notebooks -> data 
1. books_1.Best_Books_Ever.csv - the original dataset
2. GoodReads_Dataset_cleaned.csv - a copy of the cleaned dataset
3. y_train2/test2, X_train2/test2 csv files - copy of the separated dataframes, ready for modeling
4. random_forest_model.joblib - random forest model

Folder: Presentations
1. Sprint_1-EDA.pdf - Introduction to the project, basic exploration of the dataset and hypotheses for future exploring
2. Sprint_2-EDA_&_Baseline_Modeling.pdf - Project updated: major areas for data cleaning/preprocessing, baseline model 
3. Sprint_3-Final_Project.pdf - Project updated: reviewing the project, more feature engineering steps and performance from advanced modeling.
--------------------------------------------------------------------

### Data Cleaning, Preprocessing, & Feature Engineering

**Data Cleaning**
The initial state of the dataset presented a challenge with numerous missing values and several irrelevant columns. Our cleaning process primarily focused on:
- Eliminating non-essential columns and rows that didn't contribute value to the project.
- Thoroughly inspecting and handling missing data to ensure dataset integrity.
- Filling in missing values by using information from other columns (i.e. missing pages were filled in with their mean value)
- Ensuring that value formats were consistent throughout the rows

**Data Preprocessing**
Given that most dataset variables were categorical, our preprocessing and feature engineering efforts centered around:
- Converting these categorical values into numerical representations for effective analysis.
- Converting the target variable, rating, to binary column (1 = good rating, 0 = bad rating)

**Feature Engineering**
- Created new columns by taking the top 20 most popular publishers
- Created a new column that counts the number of genres that a book has
- Resolving complexities in the 'genres' column, which originally contained over 1,000 genres with formatting-induced duplicates. This column underwent significant cleaning to prepare it for further analysis.
- Utilized Text Preprocessing with TF-IDF Vectorization, keeping the top 400 words from descriptions

--------------------------------------------------------------------

### Modeling

Logisitc Regression Model:
The baseline model is a logistic regression model, chosen for its simplicity in binary classification problems. This model's accuracy was quite low to begin with, at just over 54 percent.

Random Forest Classifier:
RFC adds extra randomness compared to Decision Tree Model, showing more potential for higher accuracy. For this specific project, we have a lot of features being implemented and this model is good with working with large datasets that have multiple features.
Compared to more advanced models, RFC allows for more interpretation, which is important when understanding what features play a larger role in deciding whether a book is good or bad.

XGBoost:For creating a book recommender system, XGBoost can be efficient in handling sparse data and a powerful took for this project. It also offers regularization that helps control overfitting by using L1/L2 penalities.

Key Insights from Data Modeling:

All three models had relatively low accuracy scores with Random Forest Classifier being the highest at 60 percent. When reviewing other metrics, such as recall, precision and F-1 scores there is a notable imbalance in its ability to accurately classify both classes, especially struggling with class 0 (negative rating). 

--------------------------------------------------------------------
### Challenges and Future Steps

**Challenges**
1. Lack of Relevant Information: If the models can't distinguish well between classes, it indicates a potential issue with the features used. More relevant features could be needed for better classifying.
2. Data Imbalance: Even a small imbalance can significantly impact model performance, especially for algorithms sensitive to class distribution.
3. Dataset Limitations: Real-world datasets often have limitations, and the current dataset might not capture all the nuances needed for high accuracy. Exploring additional or updated datasets could be beneficial.

**Future Steps**
1. Data Cleaning and Preprocessing:
- Genre Consolidation: Simplifying the genre categories can reduce noise and make the model more practical.
- Incorporating Author Information: Popular authors can be a strong feature, as author popularity often influences book choice.
- Word Embedding for Descriptions: Might be able to capture book descriptions more effectively.
- Awards Feature: Binary encoding of whether a book has received awards can be a useful feature, as awards can signify quality or popularity.
2. Advanced Modeling:
- Enhanced Grid Search: More thorough hyperparameter tuning can help in finding the optimal model parameters, potentially improving model performance.
- Experimentation with Different Models: Sometimes, different algorithms can capture data patterns better, so experimenting with various models could be key.
3. Recommender System:
- Shifting focus to a recommender system to provide personalized book recommendations. As of right now, the model does not consider personal preferences. The goal is to combine important features from this modeling, combined with personal interests.
- Collaborative Filtering: Makes automatic predictions about the interests of a user by collecting preferences from many users.
- Content-Based Filtering: This approach uses item features (like genre, author, description) to recommend additional items similar to what the user likes, based on their previous liking.
    
--------------------------------------------------------------------

## Dataset Overview:

Best Books Ever Dataset
- source: https://zenodo.org/records/4265096
- data/books_1.Best_Books_Ever.csv
- 52,478 rows and 25 columns

### Data Dictionary 

| Attributes  | Description | Completeness |
| ------------- | ------------- | ------------- | 
| bookId  | Book Identifier as in goodreads.com  | 100 |
| title  | Book title | 100 |
| series | Series Name | 45 |
| author | Book's Author | 100 |
| description | Book's description | 97 |
| language | Book's language | 93 |
| isbn | Book's ISBN | 92 |
| genres | Book's genres | 91 |
| characters | Main characters | 26 |
| bookFormat | Type of binding | 97 |
| edition | Type of edition (ex. Anniversary Edition) | 9 |
| pages | Number of pages | 96 |
| publisher | Editorial | 93 |
| publishDate | publication date | 98 |
| firstPublishDate | Publication date of first edition | 59 |
| awards | List of awards | 20 |
| numRatings | Number of total ratings | 100 |
| ratingsByStars | Number of ratings by stars | 97 |
| likedPercent | Derived field, percent of ratings over 2 stars (as in GoodReads) | 99 |
| setting | Story setting | 22 |
| coverImg | URL to cover image | 99 |
| bbeScore | Score in Best Books Ever list | 100 |
| bbeVotes | Number of votes in Best Books Ever list | 100 |
| price | Book's price (extracted from Iberlibro) | 73 |


Target Variable | Description   | Completeness  |
| ------------- | ------------- | ------------- | 
| rating | Global goodreads rating | 100 |
