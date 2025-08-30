import streamlit as st

# Set the app title
st.title("My First Streamlit App")

# Add a welcome message
st.write("Welcome to this simple Streamlit application!")

# Create a slider widget and display its value
number = st.slider("Select a number", 0, 100, 50)
st.write(f"You selected: {number}")