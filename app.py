from flask import Flask,render_template,url_for,request,redirect
from books_data import book_lists,recommended_books_data
import joblib
import numpy as np

popular_df = joblib.load("model/popular.joblib")
books = joblib.load("model/books.joblib")
pt = joblib.load("model/pt.joblib")
similarity_scores = joblib.load("model/similarity_scores.joblib")

books_list = book_lists(pt)['books']

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    return render_template('index.html',
                           title="Book Recommendation System",
                           book_name =popular_df['Book-Title'].to_list(),
                           author_name = popular_df['Book-Author'].to_list(),
                           votes = popular_df['num_ratings'].to_list(),
                           rating = popular_df['avg_rating'].to_list(),
                           image = popular_df['Image-URL-M'].to_list(),
                           body_title = 'Top 50 Books')


@app.route("/recommend")
def recommend_ui():
    return render_template("recommend.html",
                           title="Recommendation System",
                           body_title="Recommended Books",blist=books_list)

@app.route("/recommend_books", methods=['GET','POST'])
def recommend():
    if request.method == 'GET':
        # Redirect to the recommend page if accessed via GET
        return redirect(url_for('recommend_ui'))


    try:
        user_input = request.form.get("user_input")

        if user_input not in books_list:
            return render_template("recommend.html",
                                   error_message="Sorry, this book is not available in our dataset.",
                                   title="Recommendation System",
                                   body_title="Recommended Books",
                                   blist=books_list)

        data = recommended_books_data(
            user_input=user_input,
            similarity_scores=similarity_scores,
            df=books,
            pt=pt)

        return render_template("recommend.html",title="Recommendation System",
                           body_title="Recommended Books",
                               data=data,
                               uinput = user_input,
                               blist=books_list)

    except Exception as e:
        return render_template("recommend.html", error_message="Sorry, this book is not available in our dataset.",
                               title="Recommendation System",
                               body_title="Recommended Books",
                               blist=books_list)



if __name__ == "__main__":
    app.run(debug=True)