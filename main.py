import streamlit as st
from scraper import  scrape_website, extract_body_content, clean_body_content, split_dom_content
from parse import parse_with_ollama

st.title("AI WebScrapper")

url= st.text_input("Enter the URL of the website you want to scrape:")

if st.button("Scrape"):
    if url:
        st.write(f"Scraping data from {url}...")
        
        data = scrape_website(url)
        print(data)
        body_content = extract_body_content(data)
        cleaned_content = clean_body_content(body_content)

        st.session_state.dom_content = cleaned_content

        with st.expander("View DOM Content"):
            st.text_area("DOM Content", cleaned_content, height=400)

    else:
        st.error("Please enter a valid URL.")

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse?")

    if st.button("Parse content"):
        if parse_description:
            st.write("parsing content...")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            results = parse_with_ollama(dom_chunks, parse_description)
            st.write(results)   