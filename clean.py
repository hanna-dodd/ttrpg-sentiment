import pandas as pd
import re

def remove_arrows(line):
    
    line = re.sub(u'\u2192', '', line)

    return line

def clean_c2():
    
    df = pd.read_csv("c2.csv")

    df.Line = df.Line.apply(remove_arrows)
    df.loc[df.Speaker == 'ALLURA', "Speaker"] = 'MATT'
    df.loc[df.Speaker == 'GILMORE', "Speaker"] = 'MATT'
    df.loc[df.Speaker == 'SHERRI', "Speaker"] = 'MATT'
    df.loc[df.Speaker == 'HECTOR', "Speaker"] = 'MATT'
    df.loc[df.Speaker == 'KIMA', "Speaker"] = 'MATT'
    df.loc[df.Speaker == 'URIEL', "Speaker"] = 'MATT'
    df.loc[df.Speaker == 'KAYLEE', "Speaker"] = 'MATT'
    df.loc[df.Speaker == 'MALE', "Speaker"] = 'MATT'

    df.loc[df.Speaker == 'EVERYONE', "Speaker"] = 'ALL'

    df.loc[df.Speaker == 'VAX', "Speaker"] = 'LIAM'
    df.loc[df.Speaker == 'KEYLETH', "Speaker"] = 'MARISHA'
    df.loc[df.Speaker == 'TIBERIUS', "Speaker"] = 'ORION'
    df.loc[df.Speaker == 'PERCY', "Speaker"] = 'TALIESIN'
    df.loc[df.Speaker == 'VEX', "Speaker"] = 'LAURA'
    df.loc[df.Speaker == 'PIKE', "Speaker"] = 'ASHLEY'
    df.loc[df.Speaker == 'GROG', "Speaker"] = 'TRAVIS'
    df.loc[df.Speaker == 'SCANLAN', "Speaker"] = 'SAM'

    df.loc[df.Speaker == 'BRAIN', "Speaker"] = 'BRIAN'
    df.loc[df.Speaker == 'LARUA', "Speaker"] = 'LAURA'
    df.loc[df.Speaker == 'II', "Speaker"] = 'MATT'
    df.loc[df.Speaker == 'W', "Speaker"] = 'MATT'
    df.loc[df.Speaker == 'A', "Speaker"] = 'MATT'
    df.loc[df.Speaker == 'MAN', "Speaker"] = 'MATT'
    df.loc[df.Speaker == 'JROE', "Speaker"] = 'JORE'
    df.loc[df.Speaker == 'time', "Speaker"] = 'MATT'

    df = df[df['Episode_Num'] != 'E12']

    csv = "c2clean.csv"
    df.to_csv(csv, index=False)
    
clean_c2()