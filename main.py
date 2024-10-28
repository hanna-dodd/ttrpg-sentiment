import pandas as pd
import re
from bs4 import BeautifulSoup

def parse_critrole():
    
    file = open('critrole/cr1-1.html', mode = 'r', encoding = 'utf-8-sig')
    lines = file.readlines()
    file.close()
    
    df = pd.DataFrame({"name": [], "line": []})
    
    for line in lines:
        
        line = line.strip()
        
        if line.startswith("<dt>"):
            name = find_name(line)
        elif line.startswith("<dd"):
            # add name as first column
            speech = find_speech(line)
            row = {"name": name, "line": speech}
            df = df._append(row, ignore_index=True)
    
    df.to_csv("cr1-1.csv", index=False)


def find_name(input_text):
    text = re.findall(r"[\w']+", input_text)
    return text[11]

def find_speech(input_text):
    soup = BeautifulSoup(input_text, 'html.parser')
    return soup.get_text()

parse_critrole()
