import html2text
import pandas as pd
from bs4 import BeautifulSoup


with open('test/cr2-1.html', 'r') as file:
    html_content = file.read()
    
# html = open('test/cr2-1.html','r')
# html_file_path = 'test/cr2-1.html'

# Read HTML file using read_html() function
# df = read_html_with_beautiful_soup(html_file_path)

# html = #import file here
text = html2text.html2text(html_content)

print(text)

