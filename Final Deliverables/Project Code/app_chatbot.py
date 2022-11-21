#IMPORTING LIBRARIES
from flask import Flask, render_template

#CREATING FLASK APPLICATION AND LOADING
app = Flask(__name__)

#ROUTING TO THE HTML PAGE
@app.route('/')
def chatbot():
    return render_template('bot.html')

#MAIN FUNCTION - Runs the application in localhost
if __name__ == '__main__':
    app.run()
