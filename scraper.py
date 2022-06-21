from bs4 import BeautifulSoup
import requests

url = input('Please input the url of a wiki article: ')
page = requests.get(url)


def get_citations_needed_count():
    """
    :return: an integer
    
    Counts the number of citations needed tags for a specific url.
    """
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all(class_ = 'Template-Fact')
    citations_count = len(results)
    
    return f'This url needs {citations_count} citations'


def get_citations_needed_report():
    """
    :return: a string with each paragraph needing a citation
    
    Returns a string for each paragraph needing a citation.
    """
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all(class_ = 'Template-Fact')
    
    for item in results:
        return item.parent.text

