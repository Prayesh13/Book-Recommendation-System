from flask import Flask,render_template,url_for,request
import pickle
import numpy as np

popular_df = pickle.load(open("model/popular.pkl",'rb'))
books = pickle.load(open("model/books.pkl",'rb'))
pt = pickle.load(open("model/pt.pkl",'rb'))
similarity_scores = pickle.load(open("model/similarity_scores.pkl",'rb'))

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
                           body_title="Recommended Books")

@app.route("/recommend_books", methods=['GET','POST'])
def recommend():
    try:
        user_input = request.form.get("user_input")
        index_books = np.where(pt.index == user_input)[0][0]
        distances = similarity_scores[index_books]
        similar_items = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:9]

        data = []
        for i in similar_items:
            item = []
            temp_df = books[books['Book-Title'] == pt.index[i[0]]]
            item.append(temp_df.drop_duplicates(subset=['Book-Title'])['Book-Title'].values[0])
            item.append(temp_df.drop_duplicates(subset=['Book-Title'])['Book-Author'].values[0])
            item.append(temp_df.drop_duplicates(subset=['Book-Title'])['Image-URL-M'].values[0])

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