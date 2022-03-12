import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('stopwords')
# for the pictures
import re
import pickle


class SpamDetection :

  # text preprocessing
    def text_preprocessing(self, message) :
  # removing a numbers from the message
        pattern = r'[0-9]'
        message = re.sub(pattern, ' ', message)

    # removing special character and punctuations and every other things from the message.
        message = re.sub('[^A-Za-z0-9]+', ' ', message)

    #applying a stop word 
        message = [word for word in word_tokenize(message)]
        words = [word.lower() for word in message if not word in stopwords.words('english')]
        message = ' '.join(words)
        return message

    def word_embedding(self) :    
        with open('/home/kali/SpamDetection/spamdetection_countvectorizer.pickle', 'rb') as file :
            countvectorizer = pickle.load(file)
            return countvectorizer
    
    def model_creation(self) :
        with open('/home/kali/SpamDetection/spamdetection_randomforest.pickle', 'rb') as file :
            randomforest_model = pickle.load(file)
        return randomforest_model

    def prediction(self, message) :
        randomforest = self.model_creation()
        countvectorizer = self.word_embedding()
        
        message = self.text_preprocessing(message)
        test_data = countvectorizer.transform([message]).toarray()
        prediction = randomforest.predict(test_data)
        return 1 if prediction == 1 else 0
    
