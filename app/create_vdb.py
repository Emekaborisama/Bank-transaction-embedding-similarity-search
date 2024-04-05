import os
from pinecone import PodSpec
from config import pc,INDEX_NAME

pc.create_index(
    name=INDEX_NAME,
    dimension=512,
    metric="cosine",
    spec=PodSpec(
        environment="gcp-starter"
    )
)