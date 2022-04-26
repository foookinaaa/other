import joblib
from sklearn import datasets # for target names


class NewsGroupsClf(object):
    def __init__(self):
        self.vectorizer = joblib.load('text_vectorizer.pkl')
        self.model = joblib.load('text_classif_model.pkl')
        self.target_names = datasets.fetch_20newsgroups(subset='test').target_names
        
    def predict_news(self, text):
        vectorized_text = self.vectorizer.transform([text])
        return self.model.predict(vectorized_text)[0]
    
    def get_name(self, label):
        return self.target_names[label]
    
    def get_topic(self, text):
        prediction = self.predict_news(text)
        return self.get_name(prediction)
        