from flask import Flask,render_template,url_for, request
from DictionaryPro import Dictionary

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "GET":
        return render_template('dictionary.html')
    elif request.method == "POST":
        word = request.form['word']
        try:
            a = Dictionary(word)
            b = a.display()
            if b is None:
                return render_template('404.html')
            return render_template('dict_action.html',word = word,names = b[0],meanings=b[1],
                                   examples = b[2],synonyms = b[3][0],antonyms = b[3][1])
        except:
            return "<h2>Sorry</h2>"
    else:
        return "<h1>BAD</h3>"
