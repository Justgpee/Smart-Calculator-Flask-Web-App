from flask import Flask

app = Flask(__name__)

books_data = {1 : "Python For Beginners" ,
              2: "Learning Flask" ,
              3 : "ML with Python"
}

@app.route('/')
def hello():
    return "Hello, World!"

@app.route("/author")
def author():
    return f"Author: Dave Nduka"

@app.route("/about")
def about():
    return "This is a simple Flask application for a calculator"

@app.route("/books/<int:book_id>")
def view_book(book_id):
    if book_id in books_data:
        return f"Book {book_id} : {books_data[book_id]}"
    else:
        return "Book not found"

if __name__ == '__main__':
    app.run(debug=True)