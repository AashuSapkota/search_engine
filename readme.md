## **Projects**
This project consists of two tasks aimed at developing tools for document retrieval and classification:

### Task 1: Search Engine
The goal is to design and implement a vertical search engine tailored to retrieve academic papers and books specifically authored by members of Coventry University’s School of Economics, Finance, and Accounting. 
### Task 2: Subject Classification
This task involves creating a document classification system that can categorize texts into three distinct topics: Politics, Business, and Health. 

#### **File Structure**
```
├── crawler.py          # Handles crawling and data extraction
├── indexer.py          # Builds and manages the inverted index
├── query_processor.py  # Processes user queries and displays results
├── utils.py            # Utility functions (e.g., text preprocessing)
├── selenium_setup.py   # Selenium web driver setup for web scraping
├── data_extractor.py   # Extract data from [New York Times Developer APIs](https://developer.nytimes.com/docs/articlesearch-product/1/overview).
├── model_train.py      # Trains the Multinomial NB with the available dataset
├── app.py              # Streamlit app, main script to run the search engine and text classification based on three Categories: Politics, Business and Health
```
### **1. Search Engine for Coventry University’s School of Economics, Finance, and Accounting**
A vertical search engine comparable to Google Scholar, but specialized in retrieving papers and books published by members of Coventry University's School of Economics, Finance, and Accounting. The system crawls the relevant web pages and retrieves information about all available publications. For each publication, it extracts available data (such as authors, publication year, and title) and the links to both the publication page and the author's profile ("pureportal" profile) page.


---

### **2. Text Classification: Politics, Business, and Health**
A text classification system that categorizes articles into three categories: Politics, Business, and Health. The system uses data extracted from [The New York Times](https://www.nytimes.com/) via the [New York Times Developer APIs](https://developer.nytimes.com/docs/articlesearch-product/1/overview).


#### **Machine Learning Model:**
- **Algorithm Used**: Multinomial Naïve Bayes (Multinomial NB)
- **Why Multinomial NB?**
  - Effective for text classification tasks where the feature vectors represent term frequency (TF) or term frequency-inverse document frequency (TF-IDF).
  - Assumes that features follow a multinomial distribution, making it well-suited for categorizing documents based on word frequency.
  - Computationally efficient and requires minimal training data.



#### **How to Run**
1. **Clone the repository**:
   ```bash
   git clone https://github.com/AashuSapkota/search_engine.git
   ```
2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Extract data to train model**:
   Updated the api key with your's key
   ```bash
   python data_extractor.py
   ```

4. **Run the application**:
   ```bash
   streamlit run app.py
   ```
