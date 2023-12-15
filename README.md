# Capstone Project - Sprint 2

### Author: Quinci Birker


## Introduction

This dataset, sourced from Goodreads, a well-known online book catalog, encompasses an extensive collection of over 52,000 books. Updated last on November 9, 2020, it provides a rich basis for this analysis. The begining of this project delves into Exploratory Data Analysis (EDA), offering visuals and insights that set the stage for further investigation. The primary aim here is to thoroughly understand the dataset and craft hypotheses, laying the groundwork for developing a personalized book recommendation model. The baseline model employed is logistic regression, serving as a foundation for more sophisticated model iterations.

### Problem Area

Finding a book that resonates with one's taste can be challenging. Often, an unsatisfactory reading experience leads to a reluctance in exploring new books. This project seeks to address this issue by offering tailored book recommendations, enhancing readers' engagement and encouraging them to explore more literature.

### The User

This model targets two main user groups:

1. Individual readers seeking personalized book recommendations. This recommendation system will be great for both reluctant and avid readers.
2. Bookstores aiming to enhance customer satisfaction and increase sales through better book suggestions. This model can be provided to customers to increase the likelihood of them enjoying the book and coming back for more.

### Big Idea

The core concept involves users inputting titles they've enjoyed in the past, prompting the model to generate suggestions for future reading. This approach aims to streamline the discovery of new books aligned with individual preferences.

### Impact

This project aims to give people more incentive to pick up a book and start reading. It can be daunting to go out and purchase a book when you have no idea if you will like it or not. I want to give readers a personalized recommendation so that they can easily find a book that they will enjoy. 
From my own experience, I’m picky with what books I read. If I read a book that I don’t enjoy, I tend to give up on reading altogether and it can take months before I look for another book to read. By the end of this project, I hope to assist in someone's reading journey and get them hooked on books. 

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





