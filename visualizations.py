import os
import re
import pandas as pd
import numpy as np
import plotly.graph_objects as go

def import_data():
    
    df = pd.read_csv("c2e1results.csv")
    
    index = df['Index'].tolist()
    emotion_labels = df["label"].tolist()
    
    return index, emotion_labels
    

def plot_emotions(index, emotion_labels):
    
    heatmap_data = []
    for label in emotion_labels:
        heatmap_data.append(label)
        
    custom_colorscale = [
        [0.0, "#FFFFFF"],
        [0.2, "#CCCCCC"],
        [0.4, "#999999"],
        [0.6, "#666666"],
        [0.8, "#333333"],
        [1.0, "#000000"],
    ]

    # Create the heatmap.
    fig = go.Figure(
        data=go.Heatmap(
            z=heatmap_data,
            x=index,
            y=emotion_labels,
            colorscale=custom_colorscale,
            colorbar=dict(title="Emotion Score"),
        )
    )

    # Layout and labels.
    fig.update_layout(
        title={
            "text": "Title",
            "x": 0.5,
            "xanchor": "center",
            "yanchor": "top",
            "font": dict(size=28, family="Arial", weight="bold"),
        },
        xaxis=dict(
            title="Time (minutes)",
            title_font=dict(size=18, family="Arial", weight="bold"),
            tickangle=45,
            tickfont=dict(size=12, family="Arial"),
            # Adjust the interval for x-axis ticks (every 5 minutes).
            dtick=5,
        ),
        yaxis=dict(
            title="Emotion",
            title_font=dict(size=18, family="Arial", weight="bold"),
            tickfont=dict(size=12, family="Arial"),
        ),
        height=1237.5,
        width=2200,
        margin=dict(l=50, r=50, t=100, b=150),
        annotations=[
            {
                "x": 1,
                "y": -0.15,
                "xref": "paper",
                "yref": "paper",
                "showarrow": False,
                "font": dict(size=12, color="gray"),
                "align": "right",
            }
        ],
    )

    # Save as an HTML file.
    fig.savefig("fig.png")
    print(f"Graph saved as fig.png")

    # Show the interactive chart in the browser.
    fig.show()



index, labels = import_data()

plot_emotions(index, labels)