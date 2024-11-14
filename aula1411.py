import requests
import pandas as pd
import streamlit as st
import io # Import the io module

@st.cache_data  # Use caching to improve performance
def load_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = pd.read_csv(io.StringIO(response.content.decode('utf-8'))) # Decode the content and wrap it in StringIO
        return data
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return None


st.title('Localização das comunidades quilombolas (2022)')
df = load_data('https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv')

if df is not None:
    st.write(df) # Display the dataframe
    # Add more Streamlit elements to visualize or interact with the data here
