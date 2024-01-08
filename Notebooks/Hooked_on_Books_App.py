### KICKOFF - CODING AN APP IN STREAMLIT

### import libraries
import pandas as pd
import streamlit as st
import joblib

#######################################################################################################################################
### LAUNCHING THE APP ON THE LOCAL MACHINE
### 1. Save your *.py file (the file and the dataset should be in the same folder)
### 2. Open git bash (Windows) or Terminal (MAC) and navigate (cd) to the folder containing the *.py and *.csv files
### 3. Execute... streamlit run <name_of_file.py>
### 4. The app will launch in your browser. A 'Rerun' button will appear every time you SAVE an update in the *.py file

#######################################################################################################################################
### Create a title

st.title("Hooked on Books - Live coding an app")

#######################################################################################################################################
### MODEL INFERENCE

st.subheader("Using pretrained models with user input")

# A. Load the model using joblib
model = joblib.load('data/random_forest_model.joblib')

# B. Set up input fields
pages = st.number_input('Enter the number of pages', min_value=1, value=300)
numRatings = st.number_input('Enter the number of ratings', min_value=1, value=100)
description = st.text_area('Enter the book description')
bbeScore = st.number_input('Enter the BBE Score', min_value=0.0, value=3.5)
genres = st.text_input('Enter the book genres', 'Fantasy, Adventure')

# C. # Function for preprocessing
def preprocess_input(pages, numRatings, description, bbeScore, genres, top_publishers, mlb, vectorizer):
    # Create a DataFrame for the input
    input_df = pd.DataFrame({
        'pages': [pages],
        'numRatings': [numRatings],
        'description': [description],
        'bbeScore': [bbeScore],
        'genres': [genres.split(', ')]  # Split genres string into a list
    })

    # Process genres
    input_df['genres'] = input_df['genres'].apply(lambda genres: [genre.strip() for genre in genres])
    input_df = input_df.join(pd.DataFrame(mlb.transform(input_df.pop('genres')), columns=mlb.classes_))

    # Process description
    desc_vec = vectorizer.transform(input_df['description'])
    desc_df = pd.DataFrame(desc_vec.toarray(), columns=vectorizer.get_feature_names_out())
    input_df = pd.concat([input_df.drop(['description'], axis=1), desc_df], axis=1)

    # Encode top publishers
    for publisher in top_publishers:
        input_df['publisher_' + publisher] = 0  # Assuming none of the top publishers for this single input

    return input_df

# D. Use the model to predict sentiment & write result
prediction = model.predict(input_df)

if prediction == 1:
    st.write('We predict that this has a good rating and we recommend this book!')
else:
    st.write('We predict that book does not have a good rating and we do not recommend this book!')



#######################################################################################################################################


