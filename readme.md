# Semantic Search Engine

## Project Description

The aim of this project is to implement a semantic search engine using artificial intelligence. This search engine encodes user queries into vectors and searches for similarity within a body of text. The user can store all the text to be searched using a vector database like Pinecone. The search engine is designed to provide accurate and relevant search results.

### Components

- [x] **Vector Database**: The project uses Pinecone to store and index the text documents.
- [x] **Vectorization Algorithm**: The project uses the SentenceTransformer library and Open AI’s latest text embeddings to vectorize the search query and the text documents to be searched from.
- [x] **Similarity Search Algorithm**: The search engine utilizes Pinecone's similarity search to find the most similar documents to the user's query.
- [x] **User Interface**: You will need to develop a user interface that allows users to enter their queries and view the search results. The interface should be intuitive and easy to use.

### Optional Components

- [x] **Multi-lingual Support**: The search engine could support multiple languages, allowing users to search for documents in different languages.
- [x] **Synonym Expansion**: The search engine could include a synonym expansion feature that expands the user's query to include similar words and phrases.
- [x] **Document Ranking**: The search engine could rank the search results based on their relevance to the user's query.
- [x] **Entity Extraction**: The search engine could include an entity extraction feature that identifies and extracts entities like people, places, and organizations from the search results.
- [ ] **Integration with Third-Party Services**: The search engine could be integrated with third-party services like Google Drive or Dropbox to provide a more comprehensive search experience.
- [ ] **Customizable Search Index**: The search engine could allow users to choose what text they want to be searched from and create a customized search index.

Project/
├── app/

│   ├── __init__.py

│   ├── main.py

│   └── utils.py

├── js/

│   ├── main.js

│   └── ...

├── static/

│   ├── css/

│   │   └── style.css

│   └── ...

├── templates/

│   ├── Index.html

│   └── ...

├── requirements.txt
├── README.md
└── .gitignore

## How to Run the Code

1. Install the required libraries:
```
pip install -r requirements.txt

```
2.Clone this repository to your local machine:
```

git clone https://github.com/Manish06097/Ai-Sementic-Search
```
3.Install the required packages using pip:
```
cd semantic-search
pip install -r requirements.txt

```


3. Set up a Pinecone account and obtain your API key.

4. Replace the `api_key` in the code with your Pinecone API key.

5. Run fast api server 
``` 
uvicorn run  app.main:app --reload 
```
6. run Index.html file to get the UI Interface
