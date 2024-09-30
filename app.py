from flask import Flask,render_template,url_for,request
import joblib
import numpy as np

popular_df = joblib.load("model/popular.joblib")
books = joblib.load("model/books.joblib")
pt = joblib.load("model/pt.joblib")
similarity_scores = joblib.load("model/similarity_scores.joblib")

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

@app.route("/book_list")
def book_names():
    book_list = {"books" : list(pt.index)}
    return book_list

@app.route("/recommend")
def recommend_ui():
    book_list = book_names()['books']
    return render_template("recommend.html",
                           title="Recommendation System",
                           body_title="Recommended Books",blist=book_list)

@app.route("/recommend_books", methods=['GET','POST'])
def recommend():
    try:
        user_input = request.form.get("user_input")
        index_books = np.where(pt.index == user_input)[0][0]
        distances = similarity_scores[index_books]
        similar_items = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[0:9]

        data = []
        for i in similar_items:
            item = []
            temp_df = books[books['Book-Title'] == pt.index[i[0]]].drop_duplicates(subset=['Book-Title'])
            item.append(temp_df['Book-Title'].values[0])
            item.append(temp_df['Book-Author'].values[0])
            item.append(temp_df['Image-URL-M'].values[0])

            data.append(item)

        print(data)

        return render_template("recommend.html",title="Recommendation System",
                           body_title="Recommended Books",
                               data=data)

    except Exception as e:
        return render_template("recommend.html", error_message="Sorry, this book is not available in our dataset.",
                               title="Recommendation System",
                               body_title="Recommended Books")



if __name__ == "__main__":
    app.run(debug=True)