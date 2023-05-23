from flask import Flask, render_template, request, redirect, url_for
import sqlite3 

app = Flask(__name__)

cafes = []

allbooks = []

db = sqlite3.connect("books-collection.db")
cursor = db.cursor()

#home page
@app.route('/')
def home():
    return render_template('index.html', loccafes=cafes)

#page for quotes from the books I've read.
@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route("/books")
def books():
       
    sql      = "SELECT * FROM books"
    cursor.execute(sql)
    records = cursor.fetchall()
    for i in records:
        #print(i)
        book={"ID": i[0], "Name": i[1], "Author": i[2], "Rating": i[3]}
        if book not in allbooks:
            allbooks.append(book)
        
    return render_template("books.html", books=allbooks) 

@app.route("/bookstable")
def bookstable():
       
    sql      = "SELECT * FROM books"
    cursor.execute(sql)
    records = cursor.fetchall()
    for i in records:
        #print(i)
        book={"ID": i[0], "Name": i[1], "Author": i[2], "Rating": i[3]}
        if book not in allbooks:
            allbooks.append(book)
        
    return render_template("bookstable.html", books=allbooks) 

@app.route("/gallery")
def gallery():
        
    return render_template("gallery.html")

@app.route("/infin")
def infin():

    return render_template("123infinquotes.html")

@app.route("/mmisfacts")
def mmisfacts():

    return render_template("mmisfacts.html")

@app.route("/cerebralmovies")
def cerebralmovies():

    return render_template("cerebralmovies.html")

@app.route("/podcasts")
def podcasts():

    return render_template("podcasts.html")

    

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple('localhost', 9000, app)
