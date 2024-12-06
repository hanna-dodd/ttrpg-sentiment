import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

file = 'c2e1_weighted.csv'
df = pd.read_csv(file)

emotion_columns = ["anger", "joy", "surprise", "disgust", "fear", "sadness"]

def categorical_emotions():
    
    emotion_data = df.groupby("Scene")[emotion_columns].mean()  # Average probabilities per scene

    emotion_data = emotion_data.sort_index()

    # Plot the heatmap
    plt.figure(figsize=(12, 6))
    sns.heatmap(
        emotion_data.T,  # Transpose to make emotions the y-axis
        cmap=sns.color_palette("rocket_r", as_cmap=True),
        annot=True,      # Show values in cells
        cbar_kws={"label": "Average Emotion Probability"},
        linewidths=0.5
    )

    # Add labels and title
    plt.xlabel("Scene")
    plt.ylabel("Emotion")
    plt.title("Emotions by Scene in Episode 1")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Show the plot
    plt.savefig("figures/heatmap_categorical.png")
    
def vad_plots():
    
    return

categorical_emotions()