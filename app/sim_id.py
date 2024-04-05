import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from app.load_data import users_data



vectorizer = CountVectorizer(analyzer='char').fit(users_data['id'])
name_vectors = vectorizer.transform(users_data['id'])

# Function to find closest name(s) with adjustable threshold
def find_similar_names(query_name, threshold=0.1):
    """
    Finds similar names in the user data based on cosine similarity.

    Args:
        query_name (str): The name to find similar names for.
        threshold (float, optional): The threshold for similarity. Defaults to 0.1.

    Returns:
        dict: A dictionary containing the list of similar users and total number of matches.
    """
    # Transform the query to the same vector space
    query_vector = vectorizer.transform([query_name])
    # Calculate cosine similarities against all names
    similarities = cosine_similarity(query_vector, name_vectors)[0]

    # Filter out results below the threshold and prepare output
    similar_indices = [i for i, score in enumerate(similarities) if score > threshold]
    
    
    if not similar_indices:
        return {"users": [], "total_number_of_matches": 0}

    results = [{"id": users_data.iloc[i]['id'], "match_metric": similarities[i]} for i in similar_indices]

    return [{
    "users": results,
    "total_number_of_matches": len(results)
    }]
