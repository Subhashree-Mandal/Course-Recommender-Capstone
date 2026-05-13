import streamlit as st
import pandas as pd
import tensorflow as tf

# 1. Load Data
@st.cache_data
def load_data():
    # Load your course list to map IDs to Titles
    courses_df = pd.read_csv('courses.csv') 
    return courses_df

courses = load_data()


# 2. Header
st.title("Course Recommender System")
st.markdown("Enter your User ID to get personalized course suggestions.")

# 3. User Input
user_id = st.number_input("Enter User ID", min_value=0, step=1)

# 4. Prediction Logic
if st.button('Predict'):
    # In a real app, you would load your model and predict here
    # For now, let's simulate a result from your best model
    st.subheader(f"Top Recommendations for User {user_id}")
    
    # Simulate extraction of latent features or direct prediction [cite: 246, 458]
    recommendations = courses.sample(5) # This is a placeholder for model.predict()
    
    for i, row in recommendations.iterrows():
        st.write(f"✅ **{row['TITLE']}**")
        st.caption(f"Course ID: {row['COURSE_ID']}")