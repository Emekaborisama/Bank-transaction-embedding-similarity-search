
from pinecone import Pinecone
import os
from openai import OpenAI


INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")
MODEL = os.getenv("EMBED_MODEL")
OPEN_API_KEY = os.getenv("OPEN_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(INDEX_NAME)
client = OpenAI(
    api_key=OPEN_API_KEY
) 