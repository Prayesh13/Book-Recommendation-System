import numpy as np
def book_lists(data):
    book_list = {"books": list(data.index)}
    return book_list

def recommended_books_data(user_input,similarity_scores,df,pt):
    index_books = np.where(pt.index == user_input)[0][0]
    distances = similarity_scores[index_books]
    similar_items = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:9]

    data = []
    for i in similar_items:
        item = []
        temp_df = df[df['Book-Title'] == pt.index[i[0]]].drop_duplicates(subset=['Book-Title'])
        item.append(temp_df['Book-Title'].values[0])
        item.append(temp_df['Book-Author'].values[0])
        item.append(temp_df['Image-URL-M'].values[0])
        item.append(temp_df['Year-Of-Publication'].values[0])

        data.append(item)

    return data
