# A vertical search engine comparable to Google Scholar, but specialized in retrieving just papers/books published by a member of Coventry University's School of Economics, Finance and Accounting

The system crawls the relevant web pages and retrieves information about all available publications. For each publication, it extracts available data (such as authors, publication year, and title) and the links to both the publication page and the author's profile (also called "pureportal" profile) page.

### **File Structure**
```
search_engine/
│
├── crawler.py          # Handles crawling and data extraction
├── indexer.py          # Builds and manages the inverted index
├── query_processor.py  # Processes user queries and displays results
├── utils.py            # Utility functions (e.g., text preprocessing)
├── selenium_setup      # Selenium web driver setup for web scraping
├── app.py              # Streamlit app, main script to run the search engine 
```

---

### **1. `crawler.py`**
This file contains the `Crawler` class, which handles crawling the Pure Portal and extracting publication data.

### **2. `indexer.py`**
This file contains the `Indexer` class, which builds and manages the inverted index.


### **3. `query_processor.py`**
This file contains the `QueryProcessor` class, which handles user queries and displays results.


### **4. `utils.py`**
This file contains utility functions like text preprocessing.


### **5. `selenium_setup.py`**
The file contains the import of necessary library and web driver setup for crawling.

### **6. `app.py`**
This is the main script that ties everything together.


### **How to Run**
To run the project, follow these steps:

1. **Clone the repository**:
   First, clone the project repository to your local machine using the following command:
   ```bash
   git clone https://github.com/AashuSapkota/search_engine.git
   ```

2. **Install the required dependencies**:
   Navigate to the project directory and install the necessary Python dependencies from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   Once the dependencies are installed, start the search engine by running the following command:
   ```bash
   streamlit run app.py
   ```


