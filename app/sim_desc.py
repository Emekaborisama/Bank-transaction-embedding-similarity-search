from app.config import pc,INDEX_NAME, client, MODEL,index



def embedindex_query(text:str):

    """
    This function searches for similar descriptions to a given text query using a pre-built index.

    Args:
        text (str): The text query for which to find similar descriptions.

    Raises:
        ValueError: If the length of the text is less than or equal to 1.

    Returns:
        dict: The search results containing information about similar descriptions,
                including potentially:
                - retrieved vectors
                - metadata associated with similar descriptions (if `include_metadata` is True)
                - similarity scores (depending on the underlying index implementation)
            The exact structure of the dictionary depends on the specific implementation
            of the used index and search library.
    """
    if len(text)<=1:
        raise ValueError("len of text is less than 1")
    embed = client.embeddings.create(input=[text], model=MODEL, dimensions=512).data[0].embedding
    
    result = index.query(vector = [embed], top_k=5, include_metadata=True)

    return result
