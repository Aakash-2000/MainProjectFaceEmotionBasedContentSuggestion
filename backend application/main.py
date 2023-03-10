
from flask import Flask,render_template
import requests
import json
from collections import Counter
import string

#global declaration
apiKey = '30660dc6c52e4f9d86d3c4938e815a49'
app = Flask(__name__)
stop_words = set(["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"])


#emotion map
emotion_map = {}
with open('emotions.txt','r') as file:
    for _ in file:
       word,emotion = _.replace('\n','').replace(',','').replace("'",'').strip().split(":")
       emotion_map[word] = emotion[1:]
# print(emotion_map)
#functions
def findEmotions(data):
    data = data.lower()
    #removing punctuation
    data = data.translate(str.maketrans('','',string.punctuation));
    tokenized_words = data.split()
    # print(tokenized_words)
    temp = []
    for word in tokenized_words:
        if word not in stop_words:
            if word in emotion_map:
                temp.append(emotion_map[word])
    return temp


#routes 
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/news/<query>',methods=["GET"])
def getNews(query):
    data = requests.get("https://newsapi.org/v2/everything?q="+str(query)+"&from=2023-02-19&language=en&sortBy=publishedAt&apiKey="+apiKey)
    data = json.loads(data.text)
    articles = data['articles']
    for article in articles:
        emotions = []
        emotions.extend(findEmotions(article['content']))
        emotions.extend(findEmotions(article['title']))
        emotions.extend(findEmotions(article['description']))
        article['emotions'] = Counter(emotions)
    return data

    
if __name__ == '__main__':
    app.run(debug=True)