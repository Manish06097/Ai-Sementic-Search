import io
import os
import tempfile
from typing import List
import PyPDF2
from sentence_transformers import SentenceTransformer
import numpy as np
import pinecone
from tqdm.auto import tqdm
from nltk.corpus import wordnet
import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
import spacy

# Load spaCy's language model
nlp = spacy.load("en_core_web_sm")
def extract_entities(doc):
    entities = set()
    for ent in doc.ents:
        if ent.label_ in ["PERSON", "ORG", "GPE"]:
            entities.add(ent.text)
    return entities

def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return list(synonyms)

def expand_query(query: str):
    synonyms = get_synonyms(query)
    if synonyms:
        expanded_query = query + " " + " ".join(synonyms)
    else:
        expanded_query = query
    return expanded_query


model = SentenceTransformer('distiluse-base-multilingual-cased-v2',device='cuda')
documents = []
embeddings = []

# def extract_text(data: bytes, filename: str) -> str:
#     if filename.lower().endswith(".pdf"):
#         with tempfile.TemporaryFile() as temp:
#             temp.write(data)
#             temp.seek(0)
#             reader = PyPDF2.PdfFileReader(temp)
#             return " ".join([reader.getPage(i).extractText() for i in range(reader.getNumPages())])
#     else:
#         return data.decode("utf-8")

def process_data(text: str):
    
    global documents, embeddings,index
    doc = text.split('.')
    index_name = 'semantic-search-openai'
    
    
    

# initialize connection to pinecone (get API key at app.pinecone.io)
    pinecone.init(
        api_key="",
        environment="us-east1-gcp"  # find next to api key in console
    )
    
    
    # try:
    #     pinecone.delete_index("semantic-search-openai")
    # except:
    #     pass
    
    
    print(doc)
    # check if 'openai' index already exists (only create index if not)
    if index_name not in pinecone.list_indexes():
        pinecone.create_index(index_name, dimension=512,metric="cosine")
    # connect to index
    index = pinecone.Index(index_name)
    count = 0  # we'll use the count to create unique IDs
    batch_size = 32  # process everything in batches of 32
    
    for i in tqdm(range(0, len(doc), batch_size)):
        # set end position of batch
        i_end = min(i+batch_size, len(doc))
        # get batch of lines and IDs
        lines_batch = doc[i: i+batch_size]
        ids_batch = [str(n) for n in range(i, i_end)]
        # create embeddings
        embeds =model.encode(lines_batch)
        # prep metadata and upsert batch
        meta = [{'text': line} for line in lines_batch]
        to_upsert = zip(ids_batch, embeds.tolist(), meta)
        # upsert to Pinecone
        index.upsert(vectors=list(to_upsert))
        
        
        
        
        
        
        
        
        
        
    
    
    


def search(query: str, top_k: int = 10) -> List[str]:
    global embeddings
    
    index_name = 'semantic-search-openai'
    pinecone.init(
        api_key="",
        environment="us-east1-gcp"
    )
    index = pinecone.Index(index_name)
    expanded_query = expand_query(query)
    print(f"Original query: {query}")
    print(f"Expanded query: {expanded_query}")
    query = model.encode(expanded_query)
    res = index.query([query.tolist()], top_k=10, include_metadata=True)
    output = [i["metadata"]['text'].strip() for i in res['matches'] if i["metadata"]['text'].strip()]
    
    # Extract entities and their types
    results = []
    for text in output:
        doc = nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        results.append((text, entities))
    
    if len(results) < 5:
        results.append(('no more search got', []))

    return results[:5]