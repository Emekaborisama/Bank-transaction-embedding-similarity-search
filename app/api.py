from typing import Annotated
from fastapi import FastAPI, Form, Response
from app.sim_id import find_similar_names  # Import for name similarity function
from app.sim_desc import embedindex_query      # Import for description similarity function
from app.ingest import clean_text
from starlette.middleware.cors import CORSMiddleware
import json
from pydantic import BaseModel
from typing import Optional
class SimilarNamesResponse(BaseModel):
    result: list[dict]  # List of similar names

class SimilarDescriptionsResponse(BaseModel):
    result: list[dict] # List of dicts containing descriptions and similarity scores


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],      
    )

@app.post("/find_similar_names/")
async def get_similar_names(
    query_name: Annotated[str, Form()],
) -> dict:
    """
    This endpoint retrieves names similar to a given query name,
    optionally specifying a similarity threshold.

    Args:
        query_name (str): Required. The name for which to find similar names.
        threshold (float, optional): Default: 0.2. A value between 0 and 1
            (inclusive) that determines the minimum similarity score for a
            name to be considered similar. Names with higher similarity scores
            are closer to the query name.

    Returns:
        dict.
    """
    result=  find_similar_names(query_name)
    print(result)
    return SimilarNamesResponse(result= result)


@app.post("/find_similar_tx/")
async def get_similar_tx(query: Annotated[str, Form()]):
    """
    This endpoint finds descriptions similar to a provided query string.

    Args:
        query (str): Required. The query string for which to locate similar descriptions.

    Returns:
        dict.
    """
    clean_desc_result= clean_text(query)
    result_data=embedindex_query(clean_desc_result)['matches']
    extracted_data = [{
        "id": item["id"],
        "score": item["score"],
        "metadata": item["metadata"]} for item in result_data]

    return SimilarDescriptionsResponse(result=extracted_data)


