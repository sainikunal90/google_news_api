Google News 


import requests
news_feed = requests.get('https://newsapi.org/v2/everything?q=bajaj auto&apiKey=#####API KEY#######sortBy=publishedAt').text

Note: Use Postman, that make testing easier and fun to use.


from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='')

top_headlines = newsapi.get_top_headlines(q='tata motors', category='business', language='en', country='in')

print(top_headlines)

###################################################

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer 
  
hotel_rev = ['Great place to be when you are in Bangalore.',
'The place was being renovated when I visited so the seating was limited.',
'Loved the ambience, loved the food',
'The food is delicious but not over the top.',
'Service - Little slow, probably because too many people.',
'The place is not easy to locate',
'Mushroom fried rice was tasty']

hotel_rev = ['sd,d','sdddw']
  
sid = SentimentIntensityAnalyzer()
for sentence in hotel_rev:
     print(sentence)
     ss = sid.polarity_scores(sentence)
     for k in ss:
         print(‘{0}: {1}, ‘.format(k, ss[k]), end=’’)
     print()

#######################################################################

sid = SentimentIntensityAnalyzer()
for sentence in hotel_rev:
     print(sentence)
     ss = sid.polarity_scores(sentence)
     for k in ss:
         print(k)
