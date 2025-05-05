import streamlit as st
from scraper import  scrape_website

st.title("AI WebScrapper")

url= st.text_input("Enter the URL of the website you want to scrape:")

if st.button("Scrape"):
    if url:
        st.write(f"Scraping data from {url}...")
        
        data = scrape_website(url)
        print(data)
    else:
        st.error("Please enter a valid URL.")