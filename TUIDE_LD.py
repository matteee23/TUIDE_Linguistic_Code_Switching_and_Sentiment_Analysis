from lingua import Language, LanguageDetectorBuilder
from collections import Counter
from transformers import pipeline

# Loading the lyrics of each song of the first mini album of TUIDE
with open('ABD_lyrics.txt', 'r', encoding='utf-8') as f:
    lyrics_1 = f.read()

with open('SUNKISS_lyrics.txt', 'r', encoding='utf-8') as f:
    lyrics_2 = f.read()

with open('Echo_lyrics.txt', 'r', encoding='utf-8') as f:
    lyrics_3 = f.read()

with open('Flip_Flop_Girl_lyrics.txt', 'r', encoding='utf-8') as f:
    lyrics_4 = f.read()

with open('GRLS_lyrics.txt', 'r', encoding='utf-8') as f:
    lyrics_5 = f.read()



# Defining the set of languages that could appear in the songs
languages = [Language.ENGLISH, Language.SPANISH, Language.FRENCH, Language.KOREAN, Language.JAPANESE]

# Defining the language detector and the sentiment-analysis model
detector = LanguageDetectorBuilder.from_languages(*languages).build()
sentiment_pipeline = pipeline(task="text-classification", model="cardiffnlp/twitter-xlm-roberta-base-sentiment",
    tokenizer="cardiffnlp/twitter-xlm-roberta-base-sentiment")

# Splitting the lyrics into lines
lines_1 = [row.strip() for row in lyrics_1.strip().split('\n') if row.strip()]
lines_2 = [row.strip() for row in lyrics_2.strip().split('\n') if row.strip()]
lines_3 = [row.strip() for row in lyrics_3.strip().split('\n') if row.strip()]
lines_4 = [row.strip() for row in lyrics_4.strip().split('\n') if row.strip()]
lines_5 = [row.strip() for row in lyrics_5.strip().split('\n') if row.strip()]

total_songs = [lines_1, lines_2, lines_3, lines_4, lines_5]
for i_song in total_songs:
    # For each line, determine the dominant language
    res_lan = []
    res_sentiment = []
    for line in i_song:
        lan = detector.detect_language_of(line)
        lan_name = lan.name if lan else "UNKNOWN"
        res_lan.append(lan_name)
        print(f"[{lan_name[:2]}] {line}")

        # Sentiment Analysis with XLM-RoBERTa
        sentiment_out = sentiment_pipeline(line)[0]
        label = sentiment_out['label']
        res_sentiment.append(label)  # Saving only the label 'positive', 'negative' or 'neutral'

    # Computing the percentual of the linguistic presence
    counter_lan = Counter(res_lan)
    tot_lines_i = len(i_song)

    print("\n--- Linguistic Presence ---")
    for lan, count in counter_lan.items():
        perc = (count / tot_lines_i) * 100
        print(f"{lan}: {perc:.1f}%")

    # Computing the percentual of the sentiment analysis
    counter_sent = Counter(res_sentiment)
    
    print("\n--- Sentiment Analysis ---")
    for sentiment_label, count in counter_sent.items():
        perc = (count / tot_lines_i) * 100
        print(f"{sentiment_label}: {perc:.1f}%")

