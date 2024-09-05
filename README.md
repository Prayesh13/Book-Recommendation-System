# Book Recommendation System

This is a collaborative filtering-based book recommendation system built with Flask. The project uses a dataset containing information about books, user ratings, and user profiles to recommend books to users based on their preferences.

## Features
- **Popular Books**: Displays the top 50 most popular books based on ratings and votes.
- **Book Recommendations**: Recommends similar books based on a user's input.
- **Web Interface**: A simple and clean web interface built with Bootstrap for easy interaction.

## [Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset)
The project uses the following dataset files:
1. **Books**: Contains information about different books including titles, authors, and image URLs.
2. **Ratings**: Includes user ratings for various books.
3. **Users**: Contains information about users.

## How It Works
The recommendation system uses collaborative filtering to find books that are similar to a user-selected book. The similarity between books is calculated using precomputed similarity scores stored in a `similarity_scores.pkl` file. The app provides recommendations based on these scores.

### Steps:
1. The user inputs a book title.
2. The system retrieves the precomputed similarity scores for that book.
3. The system recommends the top 8 books with the highest similarity scores.

### Live Demo
You can try the Book Recommendation System live at [https://book-recommendation-system-ynnn.onrender.com](https://book-recommendation-system-ynnn.onrender.com).
