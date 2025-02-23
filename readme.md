# A vertical search engine comparable to Google Scholar, but specialized in retrieving just papers/books published by a member of Coventry University's School of Economics, Finance and Accounting: 

### **File Structure**
```
search_engine/
│
├── crawler.py          # Handles crawling and data extraction
├── indexer.py          # Builds and manages the inverted index
├── query_processor.py  # Processes user queries and displays results
├── utils.py            # Utility functions (e.g., text preprocessing)
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


### **5. `app.py`**
This is the main script that ties everything together.


### **How to Run**
Run `app.py` to start the search engine:
   ```bash
   streamlit run app.py
   ```

---
