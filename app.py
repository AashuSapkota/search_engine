import streamlit as st
from crawler import Crawler
from indexer import Indexer
from query_processor import QueryProcessor

# Constants
BASE_URL = "https://pureportal.coventry.ac.uk/"
DATA_FILE = "publications.json"
INDEX_FILE = "inverted_index.json"

# Initialize components
@st.cache_resource
def initialize_components():
    crawler = Crawler(BASE_URL, data_file=DATA_FILE)
    crawler.load_data()

    # Only crawl if no existing data is found
    if not crawler.publications:
        st.write("No existing data found. Starting crawl...")
        crawler.crawl_publications()

    indexer = Indexer(crawler.publications, index_file=INDEX_FILE)
    indexer.load_index()

    # Only build index if no existing index is found
    if not indexer.inverted_index:
        st.write("No existing index found. Building index...")
        indexer.build_index()

    query_processor = QueryProcessor(crawler.publications, indexer.inverted_index)
    return query_processor

# Streamlit app
def main():
    st.title("Coventry University Publications Search Engine")
    st.write("Search for publications by members of the School of Economics, Finance, and Accounting.")

    # Initialize components
    query_processor = initialize_components()

    # Search bar
    query = st.text_input("Enter your search query:")

    if query:
        # Perform search
        relevant_docs = query_processor.search(query)

        # Display results
        if relevant_docs:
            st.write(f"Found {len(relevant_docs)} relevant publications:")
            for doc_id, score in relevant_docs:
                pub = query_processor.publications[doc_id]

                st.write(f"### {pub['title']}")
                st.write(f"**Authors:** {', '.join(author['name'] for author in pub['authors'])}")
                st.write(f"**Year:** {pub['publication_year']}")
                st.write(f"**Publication Link:** [Click here]({pub['link']})")
                st.write(f"**Author Profile:** [Click here]({', '.join(author['link'] for author in pub['authors'])})")
                st.write(f"**Relevance Score:** {score:.4f}")
                st.write("---")
        else:
            st.write("No relevant publications found.")

if __name__ == "__main__":
    main()