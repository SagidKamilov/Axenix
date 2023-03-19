from googletrans import Translator
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas
import numpy

# Предварительно нужно скачать ресурсы NLTK
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# Переводчик, если необходимо
def translator(messages: list, lang_from='auto', lang_to='en') -> list:
  translate = Translator()
  return [translate.translate(text=i, src=lang_from, dest=lang_to).text for i in messages]


# Анализ сообщений
def get_attitude(messages):
  texts = translator(messages=messages, lang_from='ru', lang_to='en')
  negative, positive, neutral = 0, 0, 0

  for text in texts:
    ss = sia.polarity_scores(text)
    if ss['compound'] > 0:
        positive += 1
    elif ss['compound'] < 0:
        negative += 1
    else:
        neutral += 1
  total = positive + negative + neutral
  negativity_percent = (negative / (positive + negative + neutral)) * 100

  return f"Процент негативных сообщений: {negativity_percent}%"



