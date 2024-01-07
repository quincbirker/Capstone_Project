# Hooked on Books
## A Book Recommender System

### Author: Quinci Birker

--------------------------------------------------------------------

## Introduction

This project aims to give people more incentive to pick up a book and start reading. It can be daunting to go out and purchase a book when you have no idea if you will like it or not. I want to give readers a an easy way to know if a book is worth reading, or not. 

From my own experience, I’m picky with what books I read. If I read a book that I don’t enjoy, I tend to give up on reading altogether and it can take months before I look for another book to read. By the end of this project, I hope to assist in someone's reading journey and get them hooked on books. 

This dataset is sourced from Goodreads, a well-known online book catalog website. It encompasses an extensive collection of over 52,000 books. Updated last on November 9, 2020, it provides a rich basis for this analysis. The beginning of this project delves into Exploratory Data Analysis (EDA), offering visuals and insights that set the stage for further investigation. The primary aim here is to thoroughly understand the dataset and craft hypotheses, laying the groundwork for developing a personalized book recommendation model. The baseline model employed is logistic regression, serving as a foundation for more sophisticated model iterations.

### The User

This model targets two main user groups:

1. Individual readers seeking personalized book recommendations. This recommendation system will be great for both reluctant and avid readers.
2. Bookstores aiming to enhance customer satisfaction and increase sales through better book suggestions. This model can be provided to customers to increase the likelihood of them enjoying the book and coming back for more.

### Big Idea

The core concept involves users inputting certain features about a book and the model will either output 'I recommend this book' or 'I do not recommend this book'. 

--------------------------------------------------------------------

## Project Organization

Folder: Notebooks 
1. EDA_&_Baseline_Modeling.ipynb
2. Advanced_Modeling-Part_1.ipynb
3. Feature_Engineering-Part_2.ipynb
4. Advanced_Modeling_Final.ipynb
  Folder: data 
  1. books_1.Best_Books_Ever.csv - the original dataset
  2. GoodReads_Dataset_cleaned.csv - a copy of the cleaned dataset
  3. y_train/test, X_train/test csv files - copy of the separated dataframes, ready for modeling

Folder: Presentations
1. Sprint_1-EDA.pdf
2. Sprint_2-EDA_&_Baseline_Modeling.pdf
3. Sprint_3-Final_Project.pdf
--------------------------------------------------------------------

### Data Cleaning, Preprocessing, and Baseline Modeling

The initial state of the dataset presented a challenge with numerous missing values and several irrelevant columns. Our cleaning process primarily focused on:
- Eliminating non-essential columns and rows that didn't contribute value to the project.
- Thoroughly inspecting and handling missing data to ensure dataset integrity.

Given that most dataset variables were categorical, our preprocessing efforts centered around:
- Converting these categorical values into numerical representations for effective analysis.
- Resolving complexities in the 'genres' column, which originally contained over 1,000 genres with formatting-induced duplicates. This column underwent significant cleaning to prepare it for further analysis.

The baseline model is a logistic regression model, chosen for its simplicity in binary classification problems. This model's accuracy was quite low to begin with, at just over 54 percent. This still provide a good baseline and hopefully future models will be able to outperform this accuracy.

--------------------------------------------------------------------

### Next Steps

Going back into data cleaning and preprocessing
- Consolidating similar genres for a more practical model. 
- Looking at the 'authors' column to include each author's average rating, offering deeper insights for book recommendations.

- Testing out different models
    - Random Forest 
    - Neural Network
    - Gradient Descent 
    
- Using grid-search for narrowing down the model parameters

- For the evaluation process, these are the metrics that will be considered:
    - Accuracy - the dataset is close to being balanced so the accuracy score will be a fundamental metric
    - Precision and Recall - these metrics will be used in addition to accuracy, since the dataset is not completely balanced
    
--------------------------------------------------------------------

### Datasets:

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





