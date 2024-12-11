import pandas as pd
import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer
from transformers import pipeline

class SimpleDataset:
    def __init__(self, tokenized_texts):
        self.tokenized_texts = tokenized_texts
    
    def __len__(self):
        return len(self.tokenized_texts["input_ids"])
    
    def __getitem__(self, idx):
        return {k: v[idx] for k, v in self.tokenized_texts.items()}
    
model_name = "j-hartmann/emotion-english-distilroberta-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
trainer = Trainer(model=model)

def prepare_data():
    
    df = pd.read_csv("data/c2E1.csv")
    df_P1 = df.loc[df['Section'] == 'Part One']
    df_P2 = df.loc[df['Section'] == 'Part Two']
    frames = [df_P1, df_P2]
    df_Show = pd.concat(frames)
    df_Dialogue = df_Show.loc[df['Category'] == 'Dialogue']
    df_Dialogue= df_Dialogue.drop(['Episode_Num', 'Episode_Name', 'Arc_Num', 'Arc_Name'], axis=1)
    df_Dialogue = df_Dialogue.rename(columns={'Line':'text'})
    
    pred_texts = df_Dialogue['text'].dropna().astype('str').tolist()
    
    return df_Dialogue, pred_texts

def predict_sentiment(pred_texts):
    
    tokenized_texts = tokenizer(pred_texts,truncation=True,padding=True)
    pred_dataset = SimpleDataset(tokenized_texts)
    
    predictions = trainer.predict(pred_dataset)
    
    preds = predictions.predictions.argmax(-1)
    labels = pd.Series(preds).map(model.config.id2label)
    scores = (np.exp(predictions[0])/np.exp(predictions[0]).sum(-1,keepdims=True)).max(1)
    temp = (np.exp(predictions[0])/np.exp(predictions[0]).sum(-1,keepdims=True))
    
    anger = []
    disgust = []
    fear = []
    joy = []
    neutral = []
    sadness = []
    surprise = []

    # extract scores (as many entries as exist in pred_texts)
    for i in range(len(pred_texts)):
        anger.append(temp[i][0])
        disgust.append(temp[i][1])
        fear.append(temp[i][2])
        joy.append(temp[i][3])
        neutral.append(temp[i][4])
        sadness.append(temp[i][5])
        surprise.append(temp[i][6])
    
    df = pd.DataFrame(list(zip(pred_texts,preds,labels,scores,  anger, disgust, fear, joy, neutral, sadness, surprise)), columns=['text','pred','label','score', 'anger', 'disgust', 'fear', 'joy', 'neutral', 'sadness', 'surprise'])
    return df

df_Dialogue, pred_texts = prepare_data()
df = predict_sentiment(pred_texts)

df_Results = pd.merge(df_Dialogue, df, on="text")
df_Results.to_csv('data/c2e1results.csv', index=False)