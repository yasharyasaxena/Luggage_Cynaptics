# import streamlit as st
from scrape import (
    scrape_website,
    extract_body_content,
    clean_body_content,
    split_dom_content,
)
from parse import parse_with_ollama
from groqParse import parse_with_groq
import json

# # Streamlit UI
# st.title("AI Web Scraper")
# url = st.text_input("Enter Website URL")

# # Step 1: Scrape the Website
# if st.button("Scrape Website"):
#     if url:
#         st.write("Scraping the website...")

#         # Scrape the website
#         dom_content = scrape_website(url)
#         body_content = extract_body_content(dom_content)
#         cleaned_content = clean_body_content(body_content)

#         # Store the DOM content in Streamlit session state
#         st.session_state.dom_content = cleaned_content

#         # Display the DOM content in an expandable text box
#         with st.expander("View DOM Content"):
#             st.text_area("DOM Content", cleaned_content, height=300)


# # Step 2: Ask Questions About the DOM Content
# if "dom_content" in st.session_state:
#     parse_description = st.text_area("Describe what you want to parse")

#     if st.button("Parse Content"):
#         if parse_description:
#             st.write("Parsing the content...")

#             # Parse the content with Ollama
#             dom_chunks = split_dom_content(st.session_state.dom_content)
#             parsed_result = parse_with_ollama(dom_chunks, parse_description)
#             st.write(parsed_result)
urls = [
    "https://www.goindigo.in/baggage/dangerous-goods-policy.html",
    "https://www.airindia.com/in/en/travel-information/baggage-guidelines/restricted-baggage.html",
    "https://www.emirates.com/in/english/before-you-fly/travel/dangerous-goods-policy/",
    "https://www.qatarairways.com/en-gb/baggage/restricted.html",
]

for url in urls:
    dom_content = scrape_website(url)
    body_content = extract_body_content(dom_content)
    cleaned_content = clean_body_content(body_content)
    dom_chunks = split_dom_content(cleaned_content)
    # parsed_result = parse_with_ollama(dom_chunks, "Extract information regarding the goods that are allowed in the cabin and checked baggage.")
    parsed_result = parse_with_groq(dom_chunks, "Extract information regarding the goods that are allowed in the cabin and checked baggage.")
    with open(f'{urls.index(url)}.json', 'w') as f:
        f.write(json.dumps(parsed_result, indent=4))
