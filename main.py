import pandas as pd
import re
from bs4 import BeautifulSoup
import os

def parse_critrole():
    
    directory = 'critrole/c1'
    c1df = pd.DataFrame({"name": [], "line": [], "episode": [], "arc": []})
    
    for filename in os.listdir(directory):
        
        f = os.path.join(directory, filename)
    
        file = open(f, mode = 'r', encoding = 'utf-8-sig')
        lines = file.readlines()
        file.close()
        
        
        for line in lines:
            
            line = line.strip()
            if line.startswith("<h3>"):
                episode = find_episode(line)
            elif line.startswith("<dt>"):
                name = find_name(line)
            elif line.startswith("<dd"):
                # add name as first column
                speech = find_speech(line)
                row = {"name": name, "line": speech, "episode": episode}
                c1df = c1df._append(row, ignore_index=True)
            
                print(episode)
    
    csv = 'c1.csv'
    c1df.to_csv(csv, index=False)

def find_episode(input_text):
    soup = BeautifulSoup(input_text, 'html.parser')
    return soup.get_text()

def find_name(input_text):
    text = re.findall(r"[\w']+", input_text)
    return text[11]

def find_speech(input_text):
    soup = BeautifulSoup(input_text, 'html.parser')
    return soup.get_text()

parse_critrole()
