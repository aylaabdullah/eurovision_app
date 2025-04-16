import pandas as pd
from wordcloud import WordCloud, STOPWORDS
from collections import Counter
import matplotlib.pyplot as plt
import re
from nltk.corpus import stopwords
import nltk
import streamlit as st


st.title('✨ Let, Love, Know')

st.header('The 100 Most Sung Words in Eurovision History (1956–2023)')



# Download NLTK data (only needed first time)
nltk.download('stopwords')

df = pd.read_csv('contestants.csv')

def create_lyrics_wordcloud(df, lyrics_col='lyrics', max_words=100):
   
    # Combine all lyrics into one text
    all_lyrics = ' '.join(df[lyrics_col].dropna().astype(str))
    
    # Custom stopwords (excludes from wordcloud)
    custom_stopwords = set(stopwords.words('english')).union({
        'oh', 'ohh', 'yeah', 'yo', 'hey', 'ya', 'uh', 'hmm', 'mmm',
        'la', 'da', 'na', 'chorus', 'verse', 'intro', 'outro', 'repeat',
        'ooh', 'ah', 'ay', 'ha', 'hoo', 'est', 'que'
    })
    
    # Text cleaning
    def clean_lyrics(text):
        # Remove text in brackets (like [Verse 1])
        text = re.sub(r'\[.*?\]', '', text)
        # Remove punctuation and special characters
        text = re.sub(r'[^\w\s]', ' ', text.lower())
        # Remove numbers
        text = re.sub(r'\d+', '', text)
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    
    # Clean the lyrics using the clean_lyrics function
    cleaned_text = clean_lyrics(all_lyrics)
    words = [word for word in cleaned_text.split() 
             if word not in custom_stopwords and len(word) > 2]
    
    # Calculate word frequencies
    word_freq = Counter(words)
    
    # Create word cloud
    wc = WordCloud(
        width=2000,
        height=1000,
        background_color='white',
        colormap='inferno', 
        max_words=max_words,
        stopwords=custom_stopwords,
        contour_width=1,
        contour_color='steelblue'
    ).generate_from_frequencies(word_freq)
    
    # Display
    plt.figure(figsize=(25, 12))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)  

    return wc

# Generate the word cloud
wordcloud = create_lyrics_wordcloud(df)
