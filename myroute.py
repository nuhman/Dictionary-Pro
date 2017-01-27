from flask import Flask,render_template,url_for, request
#from recmusic import *
from DictionaryPro import Dictionary

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test/')
def test():
    link = "<a href = '"+url_for('about')+"'> Home Page </a>"
    return "<h1> Hello follow me: "+link+" -<"

@app.route('/about/')
def about():
    return render_template('about.html')


#used to display 'add new questions page' if a get request. if post request, it tries to really 'add' it!
@app.route('/createques/', methods = ['GET','POST'])
def create():
    if request.method == "GET":
        return render_template('questions.html')
    elif request.method == "POST":
        question  = request.form['ques']
        answer =  request.form['answer']
        title =  request.form['title']
        return render_template('questionAdded.html',question = question , answer = answer)
    else:
        return "<h2>Bad Request</h2>"

#used to display the 'answer this question' page on get request , and on post , tries to submit answer
@app.route('/question/<title>', methods = ['GET','POST'])
def question(title):
    if request.method == "GET":
        question = "A question from DB appears here..."
        return render_template('answers.html',question = question)
    elif request.method == "POST":
        userans = request.form['userans']
        answer = "The real answer from DB comes here.."
        if userans == answer:
            return render_template('correct.html')
        else:
            return render_template('wrong.html',userans = userans , answer = answer)
    else:
        return "<h2>Bad Request</h2>"



@app.route('/music/', methods=['GET','POST'])
def music():
    if request.method == "GET":
        return render_template('music.html')
    elif request.method == "POST":
        x = []
        username = request.form['username']
        try:
            for i in users[username]:
                x.append(i)
            y = recommend(username , users)
            return render_template('musicprofile.html',myband=x , recmusic = y)
        except:
            return "<h3> Sorry! something went wrong! </h3>"
    else:
        return "<h3> Bad request </h3>"

		
@app.route('/ajax/',methods=['GET','POST'])
def ajax():
    if request.method == 'GET':
        return render_template('1ajax_client.html')
    elif request.method == 'POST':
        suggestions = request.form['planet_name']
        suggestions = suggestions.upper()
        return render_template('1ajax_client.html',suggestions = suggestions)
    else:
        return "<p>Bad req</p>"

@app.route('/dict/',methods=['GET','POST'])
def dict():
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
