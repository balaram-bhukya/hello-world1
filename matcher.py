import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import re, string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


# @app.route('/spell_check/prob', methods=['GET'])
# def get_prob():
#     city=request.args.get('city')
#     city=city.lower()
#     return((correction(city))) if city in WORDS else jsonify(list(known(edits2(city))))
        

def clean_text(words):
        stop_word=set(stopwords.words('english'))
        words=list(word.lower() for word in words if not word in stop_word)
        words=[word for word in words if len(word)>1 ]
        words=[WordNetLemmatizer().lemmatize(word) for word in words]

        return words

def mapper(lines,intents):

    words = []
    
    lines = re.sub("[^a-zA-Z]"," ",lines)
    lines = lines.replace('Speaker', '')
    lines = lines.strip()
    lines = lines.split()

    lines = clean_text(lines)
    words.extend(lines)


    matched =[]

    for key, value in intents.items():
        t=list(set(words) & set(value))
        matched.append((key, len(t)))
        
    # print (matched)

    return {
        "result": sorted(matched, key=lambda x: x[1], reverse=True)
    }

# mapper(lines,intents)
