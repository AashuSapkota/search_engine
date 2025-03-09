import requests
import csv
import time

# Replace with your actual API key
API_KEY = '<place your api key>'

# Base URL for the New York Times Article Search API
BASE_URL = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'

def fetch_articles(query, category, api_key, num_results=100):
    """
    Fetch articles from the New York Times API based on a query and category.
    
    :param query: Search query (e.g., 'politics', 'health', 'business')
    :param category: Category to filter by (e.g., 'news_desk:("Politics")')
    :param api_key: Your NYT API key
    :param num_results: Number of results to fetch
    :return: List of articles
    """
    articles = []
    params = {
        'q': query,
        'fq': category,
        'api-key': api_key,
        'sort': 'newest',
        'page': 0
    }
    
    while len(articles) < num_results:
        try:
            response = requests.get(BASE_URL, params=params)
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.json()
            docs = data.get('response', {}).get('docs', [])
            
            # Filter out articles with 'Briefing' in title or snippet
            filtered_docs = [
                doc for doc in docs 
                if 'Briefing' not in doc.get('headline', {}).get('main', '') 
                and 'Briefing' not in doc.get('snippet', '')
            ]
            
            articles.extend(filtered_docs)
            params['page'] += 1
            if len(docs) == 0:
                break  # No more articles available
            print(f"Fetched {len(filtered_docs)} articles. Sleeping for 12 seconds...")
            time.sleep(12)  # Sleep for 12 seconds between requests
        except requests.exceptions.HTTPError as err:
            if response.status_code == 429:
                print("Rate limit exceeded. Waiting for 60 seconds...")
                time.sleep(60)  # Wait for 60 seconds before retrying
            else:
                print(f"HTTP Error: {err}")
                break
        except Exception as err:
            print(f"Error: {err}")
            break
    
    return articles[:num_results]

def save_articles_to_tsv(articles, category, filename='nyt_data.csv'):
    """
    Save fetched articles to a TSV file.
    
    :param articles: List of articles
    :param category: Category of the articles
    :param filename: Name of the output file
    """
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter='\t')
        for article in articles:
            title = article.get('headline', {}).get('main', 'No Title')
            snippet = article.get('snippet', 'No Snippet')
            url = article.get('web_url', 'No URL')
            writer.writerow([title, snippet, url, category])

def print_article_details(articles):
    """
    Print details of the fetched articles.
    
    :param articles: List of articles
    """
    for i, article in enumerate(articles, 1):
        print(f"Article {i}:")
        print(f"Title: {article.get('headline', {}).get('main', 'No Title')}")
        print(f"Publication Date: {article.get('pub_date', 'No Date')}")
        print(f"URL: {article.get('web_url', 'No URL')}")
        print(f"Snippet: {article.get('snippet', 'No Snippet')}")
        print("-" * 80)

def main():
    # Define the categories and queries
    categories = {
        'Politics': 'politics',
        'Business': 'business',
        'Health': 'health',
    }
    
    # Output file
    output_file = 'nyt_data.csv'
    
    # Write header to the file
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(['Title', 'Snippet', 'URL', 'Category'])
    
    # Fetch and save articles for each category
    for category, query in categories.items():
        print(f"Fetching {category} articles...")
        articles = fetch_articles(query, query, API_KEY, num_results=150)
        save_articles_to_tsv(articles, category, output_file)
        print(f"Saved {len(articles)} {category} articles to {output_file}")
        print("\n" + "=" * 80 + "\n")

if __name__ == "__main__":
    main()