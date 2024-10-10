import pandas as pd

file = open('naddpod/c3-e1.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.readlines()
file.close()

# for line in lines:
    
    # remove empty lines
    # split by the colon
    # create data frame with speaker name and line (potentially any given speech tags for the line?)