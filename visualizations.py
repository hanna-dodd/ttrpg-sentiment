import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from collections import defaultdict

file = 'data/c2e1_weighted.csv'
df = pd.read_csv(file)

emotion_columns = ["anger", "joy", "surprise", "disgust", "fear", "sadness"]
main_cast = ["JESTER", "FJORD", "BEAU", "YASHA", "MOLLY", "CALEB", "NOTT"]

def categorical_emotions():
    
    emotion_data = df.groupby("Scene")[emotion_columns].mean()

    emotion_data = emotion_data.sort_index()

    plt.figure(figsize=(12, 6))
    sns.heatmap(
        emotion_data.T,
        cmap=sns.color_palette("rocket_r", as_cmap=True),
        annot=True,
        cbar_kws={"label": "Average Emotion Probability"},
        linewidths=0.5
    )

    plt.xlabel("Scene")
    plt.ylabel("Emotion")
    plt.title("Emotions by Scene (Episode 1)")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("figures/heatmap_categorical.png")
    
def vad_plots():
    
    for member in main_cast:
        
        data = df[df["Character"] == member]
        
        vad_values = np.array(data["weighted_vad"].tolist())
        valence = vad_values[:, 0]
        arousal = vad_values[:, 1]
        dominance = vad_values[:, 2]

        plt.figure(figsize=(10, 6))
        sns.kdeplot(valence, label="Valence", color="blue", fill=True, alpha=0.4)
        sns.kdeplot(arousal, label="Arousal", color="green", fill=True, alpha=0.4)
        sns.kdeplot(dominance, label="Dominance", color="red", fill=True, alpha=0.4)

        plt.xlabel("Score")
        plt.yticks(ticks=[1, 2, 3, 4, 5, 6])
        plt.ylabel("Density")
        plt.title("Distribution of Valence, Arousal, and Dominance (" + member + ")")
        plt.legend()
        plt.grid(alpha=0.3)
        plt.tight_layout()

        plt.savefig("figures/" + member + "_VAD.png")

def directed_sentiment():
    
    main_cast_data = df[df["Character"].isin(main_cast)]
    
    directed_sentiment = defaultdict(lambda: defaultdict(list))
    
    for i in range(1, len(main_cast_data)):
        
        current_speaker = main_cast_data.iloc[i]["Character"]
        previous_speaker = main_cast_data.iloc[i - 1]["Character"]
        
        if current_speaker in main_cast and previous_speaker in main_cast and current_speaker != previous_speaker:
            
            valence = main_cast_data.iloc[i]["weighted_vad"][0]
            directed_sentiment[previous_speaker][current_speaker].append(valence)
    
    directed_sentiment_avg = {
        from_char: {
            to_char: np.mean(sentiments)
            for to_char, sentiments in to_dict.items()
        }
        for from_char, to_dict in directed_sentiment.items()
    }
    
    sentiment_df = pd.DataFrame(0, index=main_cast, columns=main_cast)
    
    for from_char, to_dict in directed_sentiment_avg.items():
        for to_char, avg_sentiment in to_dict.items():
            sentiment_df.at[from_char, to_char] = avg_sentiment
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(
        sentiment_df,
        annot=True, 
        cmap="coolwarm",
        cbar_kws={"ticks": [-0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5], "label": "Average Sentiment (Valence)"},
        xticklabels=main_cast,
        yticklabels=main_cast
    )
    
    plt.title("Directed Sentiment Between Main Cast (Episode 1)")
    plt.xlabel("To")
    plt.ylabel("From")
    plt.tight_layout()
    plt.savefig("figures/directed_sentiment.png")