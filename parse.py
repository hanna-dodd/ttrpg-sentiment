import pandas as pd
import re
from bs4 import BeautifulSoup
import os

def parse_critrole():
    
    directory = 'critrole/c3'
    critroledf = pd.DataFrame({"episode #": [], "episode": [], "name": [], "line": [], "arc #": [], "arc": []})
    
    for filename in os.listdir(directory):
        
        f = os.path.join(directory, filename)
    
        file = open(f, mode = 'r', encoding = 'utf-8-sig')
        lines = file.readlines()
        file.close()
        
        episode = ""
        episode_num = ""
        arc = ""
        arc_num = ""
        
        for line in lines:
            
            line = line.strip()
            if line.startswith("<h3>"):
                episode = episode + " " + find_episode(line)
            elif line.startswith("<dt>"):
                name = find_name(line)
            elif line.startswith("<dd"):
                # add name as first column
                speech = find_speech(line)
                episode_num = int((re.findall(r'\d+', episode))[1])
                
                if 1 <= episode_num and episode_num <= 23:
                    arc_num = "A1"
                    arc = "Arc 1: Jrusar"
                elif 24 <= episode_num and episode_num <= 51:
                    arc_num = "A2"
                    arc = "Arc 2: Ruidus Rising"
                    break
                elif 52 <= episode_num and episode_num <= 75:
                    arc_num = "A3"
                    arc = "Arc 3: Separations and Explorations"
                elif 76 <= episode_num and episode_num <= 98:
                    arc_num = "A4"
                    arc = "Arc 4: Ruidus to Aeor"
                elif 99 <= episode_num and episode_num <= 101:
                    arc_num = "A5"
                    arc = "Arc 5: Downfall"
                
                row = {"episode #": "E" + str(episode_num), "episode": episode, "name": name, "line": speech, "arc #": arc_num, "arc": arc}
                critroledf = critroledf._append(row, ignore_index=True)
    
        print(episode_num)
        
    csv = 'c3.csv'
    critroledf.to_csv(csv, index=False)

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
