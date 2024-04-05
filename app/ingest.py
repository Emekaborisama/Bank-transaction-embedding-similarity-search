import os
from pinecone import PodSpec
try:
    from load_data import tx
    from config import pc,INDEX_NAME, client, MODEL, index
except:
    from app.load_data import tx
    from app.config import pc,INDEX_NAME, client, MODEL, index
import re


batch_size = 32
count = 0




def remove_punctuation(text):
    # Define the regex pattern to match punctuation
    pattern = r'[^\w\s]'
    # Use the sub() function to replace punctuation with an empty string
    clean_text = re.sub(pattern, '', text)
    return clean_text




def remove_whitespace(text):
    pattern = r'\s{2,}'
    clean_text = re.sub(pattern, ' ', text)
    return(clean_text)


def remove_n_gram(text, len_text=2):
    text = text.split()
    result = [x for x in text if len(x)>=len_text]
    return " ".join(result)


def clean_text(text):
    if len(text)<=1 or text == None:
        text = None
        return text
    # normal text
    text = text.lower()

    pattern = 'ref .*cntr'
    rex_result = re.sub(pattern, '', text)
    # remove punctuation
    remove_punc = remove_punctuation(rex_result)
    remove_ws = remove_whitespace(remove_punc)
    return remove_ws

if __name__ == '__main__':
    tx['description'] = tx['description'].apply(clean_text)
    tx = tx[tx['description'] != '']
    # convert to embedding with ID and meta data.
    for x in range(0, len(tx),batch_size):
        i_end = min(x+batch_size, len(tx['description']))
        print(i_end)
        lines_batch = tx['description'][x: x+batch_size]
        ids_batch = [str(n) for n in range(x, i_end)]
        remove_null = [x for x in list(lines_batch) if len(x)>=2]
        res = client.embeddings.create(input=remove_null, model=MODEL, dimensions=512)
        embeds = [record.embedding for record in res.data]
        meta = [{'text': line} for line in lines_batch]
        to_upsert = zip(ids_batch, embeds, meta)
        print(to_upsert)
        index.upsert(vectors=list(to_upsert))