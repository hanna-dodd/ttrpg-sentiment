import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# standard vad scores for each emotion
vad_scores = {
    "anger": np.array([-0.43, 0.67, 0.34]),
    "joy": np.array([0.76, 0.48, 0.35]),
    "surprise": np.array([0.4, 0.67, -0.13]),
    "disgust": np.array([-0.6, 0.35, 0.11]),
    "fear": np.array([-0.64, 0.6, -0.43]),
    "sadness": np.array([-0.63, 0.27, -0.33]),
}

emotion_columns = ["anger", "joy", "surprise", "disgust", "fear", "sadness"]

def calculate_weighted_vad(row, vad_scores, emotion_columns):

    weighted_vad = np.zeros(3)

    for emotion in emotion_columns:
        weighted_vad += row[emotion] * vad_scores[emotion]

    return weighted_vad

file = 'c2e1results.csv'
df = pd.read_csv(file)

df["weighted_vad"] = df.apply(calculate_weighted_vad, axis=1, args=(vad_scores, emotion_columns))
df.to_csv('c2e1_weighted.csv', index=False)