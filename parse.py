import pandas as pd
import re
from bs4 import BeautifulSoup
import os

def parse_critrolec1():
    
    directory = 'critrole/c1'
    critroledf = pd.DataFrame({"Index": [], "Episode_Num": [], "Episode_Name": [], "Arc_Num": [], "Arc_Name": [], "Speaker": [], "Line": []})
    
    for filename in os.listdir(directory):
        
        f = os.path.join(directory, filename)
    
        file = open(f, mode = 'r', encoding = 'utf-8-sig')
        lines = file.readlines()
        file.close()
        
        episode = ""
        episode_num = ""
        arc = ""
        arc_num = ""
        line_num = 1
        
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
                    arc = "Arc 1: Kraghammer and Vasselheim"
                elif 24 <= episode_num and episode_num <= 38:
                    arc_num = "A2"
                    arc = "Arc 2: The Briarwoods"
                elif 39 <= episode_num and episode_num <= 83:
                    arc_num = "A3"
                    arc = "Arc 3: The Chroma Conclave"
                elif 84 <= episode_num and episode_num <= 99:
                    arc_num = "A4"
                    arc = "Arc 4: Taryon Darrington"
                elif 100 <= episode_num and episode_num <= 115:
                    arc_num = "A5"
                    arc = "Arc 5: Vecna"
                
                row = {"Index": line_num, "Episode_Num": "E" + str(episode_num), "Episode_Name": episode, "Arc_Num": arc_num, "Arc_Name": arc, "Speaker": name, "Line": speech}
                line_num = line_num + 1
                critroledf = critroledf._append(row, ignore_index=True)
    
        print(episode_num)
        
    csv = 'c1.csv'
    critroledf.to_csv(csv, index=False)
    
def parse_critrolec2():
    
    directory = 'critrole/c2'
    critroledf = pd.DataFrame({"Index": [], "Episode_Num": [], "Episode_Name": [], "Arc_Num": [], "Arc_Name": [], "Speaker": [], "Line": []})
    
    for filename in os.listdir(directory):
        
        f = os.path.join(directory, filename)
    
        file = open(f, mode = 'r', encoding = 'utf-8-sig')
        lines = file.readlines()
        file.close()
        
        episode = ""
        episode_num = ""
        arc = ""
        arc_num = ""
        line_num = 1
        
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
                
                if 1 <= episode_num and episode_num <= 25:
                    arc_num = "A1"
                    arc = "Arc 1: Come Together"
                elif 26 <= episode_num and episode_num <= 47:
                    arc_num = "A2"
                    arc = "Arc 2: The Bad Guys"
                elif 48 <= episode_num and episode_num <= 69:
                    arc_num = "A3"
                    arc = "Arc 3: The Bright Queen's Favor"
                elif 70 <= episode_num and episode_num <= 91:
                    arc_num = "A4"
                    arc = "Arc 4: Swords and Angels"
                elif 92 <= episode_num and episode_num <= 112:
                    arc_num = "A5"
                    arc = "Arc 5: Family Ties"
                elif 113 <= episode_num and episode_num <= 141:
                    arc_num = "A6"
                    arc = "Arc 6: Weird Magic"
                
                row = {"Index": line_num, "Episode_Num": "E" + str(episode_num), "Episode_Name": episode, "Arc_Num": arc_num, "Arc_Name": arc, "Speaker": name, "Line": speech}
                line_num = line_num + 1
                critroledf = critroledf._append(row, ignore_index=True)
    
        print(episode_num)
        
    csv = 'c2.csv'
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

parse_critrolec2()
