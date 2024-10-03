from flask import Flask , render_template

app = Flask(__name__)

tasklist= [["walk dog", True], ["wash dishes",False], ["take out trash", True]]
@app.route("/")
def home():
     return render_template("tasklist.html" , TaskList=tasklist)



app.run()