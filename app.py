from flask import Flask, render_template, request, redirect, url_for, jsonify
import re
from flask_mysqldb import MySQL
from datetime import datetime

# Configure application
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'dashboard'

mysql = MySQL(app)

#####################
@app.route('/signup', methods=['POST'])
def signup():
    email = request.form['email']
    password = request.form['password']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, password))
    mysql.connection.commit()
    cur.close()

    return redirect(url_for('login'))
#####################

@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Extract the username and password from the login form
        email = request.form['email']
        password = request.form['password']

        # Query the database for the user with the given username and password
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
        user = cur.fetchone()
        cur.close()

        # If the user exists, redirect to the welcome page
        if user:
            return redirect(url_for('welcome'))

    # Render the login form
    return render_template('login.html')

###################

@app.route("/welcome", methods=['GET'])
def welcome():
    return render_template('welcome.html')

################### EASY WORD MODE LEVEL 1

@app.route("/dashboard", methods=['GET'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    correct_words = ['if', 'long', 'about', 'got', 'six', 'never', 'seven', 'eight', 'today', 'myself', 'much', 'keep', 'try', 'start', 'ten', 'bring', 'drink', 'only', 'better', 'hold', 'warm', 'full', 'done','light','pick','hurt','cut','kind','fall','carry','small','own','show','hot','far','draw','clean','grow','together','shall','laugh','would','very','your','its', 'around','dont','right','green','them','call','sleep','five','wash','or','before','been','off','cold','tell','work','first','does','goes','write','always','made','gave', 'us','buy','those','use','fast','pull','both','sit','which','read','why','found','because','best','upon','these','sing','wish','many','take','every','again']

    spoken_text = request.json.get('spoken_text')

    # Analyze the spoken text for mispronounced words
    mispronounced_words = analyze_speech(spoken_text, correct_words)

    # Return the mispronounced words as JSON
    return jsonify(mispronounced_words=mispronounced_words)

def analyze_speech(spoken_text, correct_words):
    # Split the spoken text into words
    spoken_words = re.findall(r'\b\w+\b', spoken_text.lower())

    # Compare the spoken words with the correct words and find mispronounced words
    mispronounced_words = [word for word in spoken_words if word not in correct_words]

    # Store the mispronounced words and time in the database
    if len(mispronounced_words) > 0:
        cur = mysql.connection.cursor()
        for word in mispronounced_words:
            current_time = datetime.now()
            insert_query = "INSERT INTO mispronunciations (word, mispronounced_at) VALUES (%s, %s)"
            data = (word, current_time)
            cur.execute(insert_query, data)
        mysql.connection.commit()
        cur.close()

    return mispronounced_words

################################ HARD WORD MODE LEVEL 1

@app.route("/dashboard4", methods=['GET'])
def dashboard4():
    return render_template('dashboard4.html')

@app.route('/analyze4', methods=['POST'])
def analyze4():
    correct_words = ['empty','emptied','parties','families','mystery','mysteries','discovery','married','carried','religion','folklore','custom','syllable','fluent', 'permission','confession','vision','please','action','quotation','hunting','nation','combination', 'question','attention','geography','physical','divided','exact','agreed','whether','answer','shower','sequence','explorer','establish','independence','passed','total','central','final','simple','chuckle','giggle','middle','signal', 'handle','candle','uncle','infer','prior','knowledge','modify','clarify','federal','state','interaction', 'climate','natural','tools','comprehend','formally','rapidly','dangerously','tenderly','lovely','nicely','identity','culture','society','accurate','precise', 'comfortable','honorably','erasable','available','portable','laughable','irritably','feeling','capable','disposable''reusable','tube','government','tribal','derive','general', 'advantage','history']

    spoken_text = request.json.get('spoken_text')

    # Analyze the spoken text for mispronounced words
    mispronounced_words = analyze_speech4(spoken_text, correct_words)

    # Return the mispronounced words as JSON
    return jsonify(mispronounced_words=mispronounced_words)

def analyze_speech4(spoken_text, correct_words):
    # Split the spoken text into words
    spoken_words = re.findall(r'\b\w+\b', spoken_text.lower())

    # Compare the spoken words with the correct words and find mispronounced words
    mispronounced_words = [word for word in spoken_words if word not in correct_words]

    # Store the mispronounced words and time in the database
    if len(mispronounced_words) > 0:
        cur = mysql.connection.cursor()
        for word in mispronounced_words:
            current_time = datetime.now()
            insert_query = "INSERT INTO mispronunciations (word, mispronounced_at) VALUES (%s, %s)"
            data = (word, current_time)
            cur.execute(insert_query, data)
        mysql.connection.commit()
        cur.close()

    return mispronounced_words

################################ 
################################ EASY STORY MODE LEVEL 1

@app.route("/sedashboard1", methods=['GET'])
def sedashboard1():
    return render_template('sedashboard1.html')

@app.route('/analyze1', methods=['POST'])
def analyze1():
    correct_words = ['lets', 'have', 'some', 'fun', 'this', 'summer', 'says', 'leo', 'lets', 'swim', 'in', 'the', 'river', 'says', 'lina',
      'lets', 'get', 'some', 'star', 'apples', 'from', 'the', 'tree', 'says', 'leo', 'lets', 'pick', 'flowers', 'says', 'lina',
      'that', 'is', 'so', 'much', 'fun', 'says', 'mama', 'but', 'can', 'you', 'help', 'me', 'dust', 'the', 'shelves', 'too',
      'yes', 'we', 'can', 'mama', 'they', 'say',
      'helping', 'can', 'be', 'fun', 'too']

    spoken_text = request.json.get('spoken_text')

    # Analyze the spoken text for mispronounced words
    mispronounced_words = analyze_speech1(spoken_text, correct_words)

    # Return the mispronounced words as JSON
    return jsonify(mispronounced_words=mispronounced_words)

def analyze_speech1(spoken_text, correct_words):
    # Split the spoken text into words
    spoken_words = re.findall(r'\b\w+\b', spoken_text.lower())

    # Compare the spoken words with the correct words and find mispronounced words
    mispronounced_words = [word for word in spoken_words if word not in correct_words]

    # Store the mispronounced words and time in the database
    if len(mispronounced_words) > 0:
        cur = mysql.connection.cursor()
        for word in mispronounced_words:
            current_time = datetime.now()
            insert_query = "INSERT INTO mispronunciations (word, mispronounced_at) VALUES (%s, %s)"
            data = (word, current_time)
            cur.execute(insert_query, data)
        mysql.connection.commit()
        cur.close()

    return mispronounced_words

################################ 
################################ EASY STORY MODE LEVEL 2

@app.route("/sedashboard2", methods=['GET'])
def sedashboard2():
    return render_template('sedashboard2.html')

@app.route('/analyze2', methods=['POST'])
def analyze2():
    correct_words = ['nina', 'and', 'ria', 'are', 'looking', 'out', 'the', 'window',
                     'i', 'do', 'not', 'like', 'getting', 'wet', 'in', 'the', 'rain', 'says', 'nina', 'what', 'can', 'we', 'do', 'asks', 'ria',
                     'okay', 'let’s', 'play', 'tag', 'you’re', 'it', 'says', 'nina',
                     'nina', 'runs', 'from', 'ria', 'and', 'bumps', 'a', 'lamp', 'oh', 'no', 'says', 'nina'
                     'we', 'must', 'not', 'play', 'tag', 'in', 'the', 'house']

    spoken_text = request.json.get('spoken_text')

    # Analyze the spoken text for mispronounced words
    mispronounced_words = analyze_speech2(spoken_text, correct_words)

    # Return the mispronounced words as JSON
    return jsonify(mispronounced_words=mispronounced_words)

def analyze_speech2(spoken_text, correct_words):
    # Split the spoken text into words
    spoken_words = re.findall(r'\b\w+\b', spoken_text.lower())

    # Compare the spoken words with the correct words and find mispronounced words
    mispronounced_words = [word for word in spoken_words if word not in correct_words]

    # Store the mispronounced words and time in the database
    if len(mispronounced_words) > 0:
        cur = mysql.connection.cursor()
        for word in mispronounced_words:
            current_time = datetime.now()
            insert_query = "INSERT INTO mispronunciations (word, mispronounced_at) VALUES (%s, %s)"
            data = (word, current_time)
            cur.execute(insert_query, data)
        mysql.connection.commit()
        cur.close()

    return mispronounced_words

################################ 
################################ EASY STORY MODE LEVEL 3

@app.route("/sedashboard3", methods=['GET'])
def sedashboard3():
    return render_template('sedashboard3.html')

@app.route('/analyze3', methods=['POST'])
def analyze3():
    correct_words = ['ben', 'has', 'his', 'own', 'store',
      'do', 'you', 'sell', 'eggs', 'asks', 'mel',
      'yes', 'come', 'in', 'says', 'ben',
      'do', 'you', 'sell', 'milk', 'asks', 'Dante',
      'yes', 'come', 'in', 'says', 'ben',
      'do', 'you', 'sell', 'hats', 'asks', 'lala',
      'no', 'we', 'do', 'not', 'sell', 'hats', 'says', 'ben',
      'but', 'you', 'can', 'come', 'in', 'and', 'have', 'a', 'look',
      'lala', 'goes', 'in', 'she', 'gets', 'a', 'banana']

    spoken_text = request.json.get('spoken_text')

    # Analyze the spoken text for mispronounced words
    mispronounced_words = analyze_speech3(spoken_text, correct_words)

    # Return the mispronounced words as JSON
    return jsonify(mispronounced_words=mispronounced_words)

def analyze_speech3(spoken_text, correct_words):
    # Split the spoken text into words
    spoken_words = re.findall(r'\b\w+\b', spoken_text.lower())

    # Compare the spoken words with the correct words and find mispronounced words
    mispronounced_words = [word for word in spoken_words if word not in correct_words]

    # Store the mispronounced words and time in the database
    if len(mispronounced_words) > 0:
        cur = mysql.connection.cursor()
        for word in mispronounced_words:
            current_time = datetime.now()
            insert_query = "INSERT INTO mispronunciations (word, mispronounced_at) VALUES (%s, %s)"
            data = (word, current_time)
            cur.execute(insert_query, data)
        mysql.connection.commit()
        cur.close()

    return mispronounced_words

################################ 
################################ EASY STORY MODE LEVEL 4

@app.route("/sedashboard5", methods=['GET'])
def sedashboard5():
    return render_template('sedashboard5.html')

@app.route('/analyze5', methods=['POST'])
def analyze5():
    correct_words = ['mara', 'sat', 'by', 'the', 'school', 'gate',
      'it', 'was', 'the', 'end', 'of', 'the', 'day',
      'mara', 'looked', 'at', 'her', 'watch', 
      'where', 'is', 'ate', 'mila', 'she', 'asked', 
      'mara', 'looked', 'at', 'her', 'watch', 'again',
      'at', 'last', 'mila', 'has', 'come', 'to', 'pick', 'her', 'up', 
      'let’s', 'go', 'home', 'mama', 'said', 'it’s', 'time', 'for', 'dinner', 'says', 'mila',
      'i', 'am', 'glad', 'you', 'are', 'here', 'says', 'mara']

    spoken_text = request.json.get('spoken_text')

    # Analyze the spoken text for mispronounced words
    mispronounced_words = analyze_speech5(spoken_text, correct_words)

    # Return the mispronounced words as JSON
    return jsonify(mispronounced_words=mispronounced_words)

def analyze_speech5(spoken_text, correct_words):
    # Split the spoken text into words
    spoken_words = re.findall(r'\b\w+\b', spoken_text.lower())

    # Compare the spoken words with the correct words and find mispronounced words
    mispronounced_words = [word for word in spoken_words if word not in correct_words]

    # Store the mispronounced words and time in the database
    if len(mispronounced_words) > 0:
        cur = mysql.connection.cursor()
        for word in mispronounced_words:
            current_time = datetime.now()
            insert_query = "INSERT INTO mispronunciations (word, mispronounced_at) VALUES (%s, %s)"
            data = (word, current_time)
            cur.execute(insert_query, data)
        mysql.connection.commit()
        cur.close()

    return mispronounced_words

################################
################################ HARD STORY MODE LEVEL 1

@app.route("/sedashboard6", methods=['GET'])
def sedashboard6():
    return render_template('sedashboard6.html')

@app.route('/analyze6', methods=['POST'])
def analyze6():
    correct_words = ['duck', 'hen', 'and', 'bird', 'are', 'in', 'the', 'garden',
      'i', 'see', 'a', 'big', 'round', 'egg', 'on', 'the', 'grass', 'says', 'bird', 'it', 'is', 'not', 'my', 'egg', 'says', 'hen',
      'my', 'egg', 'is', 'in', 'the', 'nest',
      'it', 'is', 'not', 'my', 'egg', 'says', 'duck',
      'my', 'eggs', 'just', 'hatched', 'it', 'is', 'not', 'an', 'egg', 'says', 'ben',
      'it’s', 'my', 'rubber', 'ball']

    spoken_text = request.json.get('spoken_text')

    # Analyze the spoken text for mispronounced words
    mispronounced_words = analyze_speech6(spoken_text, correct_words)

    # Return the mispronounced words as JSON
    return jsonify(mispronounced_words=mispronounced_words)

def analyze_speech6(spoken_text, correct_words):
    # Split the spoken text into words
    spoken_words = re.findall(r'\b\w+\b', spoken_text.lower())

    # Compare the spoken words with the correct words and find mispronounced words
    mispronounced_words = [word for word in spoken_words if word not in correct_words]

    # Store the mispronounced words and time in the database
    if len(mispronounced_words) > 0:
        cur = mysql.connection.cursor()
        for word in mispronounced_words:
            current_time = datetime.now()
            insert_query = "INSERT INTO mispronunciations (word, mispronounced_at) VALUES (%s, %s)"
            data = (word, current_time)
            cur.execute(insert_query, data)
        mysql.connection.commit()
        cur.close()

    return mispronounced_words

################################
# ################################ HARD STORY MODE LEVEL 2

@app.route("/sedashboard7", methods=['GET'])
def sedashboard7():
    return render_template('sedashboard7.html')

@app.route('/analyze7', methods=['POST'])
def analyze7():
    correct_words = ['dan', 'and', 'pepe', 'will', 'play', 'but', 'the', 'sun', 'is', 'hot', 'says', 'pepe', 'let', 'us', 'get', 'our', 'caps', 'says', 'dan',
      'my', 'cap', 'is', 'not', 'on', 'my', 'bed', 'says', 'pepe',
      'my', 'cap', 'is', 'not', 'in', 'my', 'bag', 'says', 'dan', 'look', 'boys', 'our', 'cat', 'has', 'kittens', 'says', 'mama',
      'mik-mik', 'has', 'four', 'kittens', 'says', 'dan', 'yay', 'the', 'kittens', 'nap', 'in', 'our', 'caps']

    spoken_text = request.json.get('spoken_text')

    # Analyze the spoken text for mispronounced words
    mispronounced_words = analyze_speech7(spoken_text, correct_words)

    # Return the mispronounced words as JSON
    return jsonify(mispronounced_words=mispronounced_words)

def analyze_speech7(spoken_text, correct_words):
    # Split the spoken text into words
    spoken_words = re.findall(r'\b\w+\b', spoken_text.lower())

    # Compare the spoken words with the correct words and find mispronounced words
    mispronounced_words = [word for word in spoken_words if word not in correct_words]

    # Store the mispronounced words and time in the database
    if len(mispronounced_words) > 0:
        cur = mysql.connection.cursor()
        for word in mispronounced_words:
            current_time = datetime.now()
            insert_query = "INSERT INTO mispronunciations (word, mispronounced_at) VALUES (%s, %s)"
            data = (word, current_time)
            cur.execute(insert_query, data)
        mysql.connection.commit()
        cur.close()

    return mispronounced_words

################################
################################ HARD STORY MODE LEVEL 3

@app.route("/sedashboard8", methods=['GET'])
def sedashboard8():
    return render_template('sedashboard8.html')

@app.route('/analyze8', methods=['POST'])
def analyze8():
    correct_words = ['Come', 'with', 'me', 'says', 'dan', 
      'where', 'will', 'we', 'go', 'mina', 'asks', 'we', 'will', 'go', 'to', 'a', 'happy', 'place', 'that', 'has', 'lots', 'of', 'balloons',

      'we', 'will', 'play', 'dance', 'and', 'run',
      'we', 'will', 'have', 'so', 'much', 'fun',
      'we', 'will', 'eat', 'orange', 'cake', 'that', 'our', 'mom', 'and', 'dad', 'baked'
      
      'and', 'then', 'we', 'will', 'sing',
      'happy', 'birthday', 'dear', 'benny']

    spoken_text = request.json.get('spoken_text')

    # Analyze the spoken text for mispronounced words
    mispronounced_words = analyze_speech8(spoken_text, correct_words)

    # Return the mispronounced words as JSON
    return jsonify(mispronounced_words=mispronounced_words)

def analyze_speech8(spoken_text, correct_words):
    # Split the spoken text into words
    spoken_words = re.findall(r'\b\w+\b', spoken_text.lower())

    # Compare the spoken words with the correct words and find mispronounced words
    mispronounced_words = [word for word in spoken_words if word not in correct_words]

    # Store the mispronounced words and time in the database
    if len(mispronounced_words) > 0:
        cur = mysql.connection.cursor()
        for word in mispronounced_words:
            current_time = datetime.now()
            insert_query = "INSERT INTO mispronunciations (word, mispronounced_at) VALUES (%s, %s)"
            data = (word, current_time)
            cur.execute(insert_query, data)
        mysql.connection.commit()
        cur.close()

    return mispronounced_words

################################
################################ HARD STORY MODE LEVEL 4

@app.route("/sedashboard9", methods=['GET'])
def sedashboard9():
    return render_template('sedashboard9.html')

@app.route('/analyze9', methods=['POST'])
def analyze9():
    correct_words = ['today', 'sam', 'and', 'ria', 'will', 'go', 'to', 'the', 'park',
      'what', 'will', 'they', 'do', 'there',
      'they', 'will', 'sit', 'on', 'the', 'grass',
      'and', 'look', 'at', 'some', 'bugs',
      'they', 'will', 'look', 'at', 'the', 'holes',
      'that', 'the', 'worms', 'have', 'just', 'dug',
      'that', 'is', 'where', 'they', 'will', 'stay', 'on', 'this', 'warm', 'summer', 'day',
      'but', 'they', 'must', 'leave', 'the', 'park', 'before', 'it', 'gets', 'dark']

    spoken_text = request.json.get('spoken_text')

    # Analyze the spoken text for mispronounced words
    mispronounced_words = analyze_speech9(spoken_text, correct_words)

    # Return the mispronounced words as JSON
    return jsonify(mispronounced_words=mispronounced_words)

def analyze_speech9(spoken_text, correct_words):
    # Split the spoken text into words
    spoken_words = re.findall(r'\b\w+\b', spoken_text.lower())

    # Compare the spoken words with the correct words and find mispronounced words
    mispronounced_words = [word for word in spoken_words if word not in correct_words]

    # Store the mispronounced words and time in the database
    if len(mispronounced_words) > 0:
        cur = mysql.connection.cursor()
        for word in mispronounced_words:
            current_time = datetime.now()
            insert_query = "INSERT INTO mispronunciations (word, mispronounced_at) VALUES (%s, %s)"
            data = (word, current_time)
            cur.execute(insert_query, data)
        mysql.connection.commit()
        cur.close()

    return mispronounced_words

################################
@app.route('/mispronunciations')
def mispronunciations():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM mispronunciations")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
