# utils/recommender.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_recommendations(movie_name, movies_df, top_n=5):
    """
    Returns top_n movie recommendations based on combined features (title + genres)
    """

    # Fill missing values
    movies_df['title'] = movies_df['title'].fillna('')
    movies_df['genres'] = movies_df['genres'].fillna('')

    # Combine title and genres into one text feature
    movies_df['combined_features'] = movies_df['title'] + ' ' + movies_df['genres']

    # Vectorize using TF-IDF
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(movies_df['combined_features'])

    # Compute cosine similarity
    similarity = cosine_similarity(tfidf_matrix)

    # Find movie index (supports partial matches)
    matches = movies_df[movies_df['title'].str.contains(movie_name, case=False, na=False)]
    if matches.empty:
        return []

    idx = matches.index[0]
    sim_scores = list(enumerate(similarity[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]

    recommended = movies_df.iloc[[i[0] for i in sim_scores]][['title']]
    scores = [round(similarity[idx][i[0]], 3) for i in sim_scores]

    # Combine titles with similarity scores
    recommendations = [
        {"title": title, "similarity": score}
        for title, score in zip(recommended['title'], scores)
    ]
    return recommendations
