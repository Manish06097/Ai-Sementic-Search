# Semantic Search Engine

## Project Description

The aim of this project is to implement a semantic search engine using artificial intelligence. This search engine encodes user queries into vectors and searches for similarity within a body of text. The user can store all the text to be searched using a vector database like Pinecone. The search engine is designed to provide accurate and relevant search results.

### Components

- [] **Vector Database**: The project uses Pinecone to store and index the text documents.
- [x] **Vectorization Algorithm**: The project uses the SentenceTransformer library and Open AI’s latest text embeddings to vectorize the search query and the text documents to be searched from.
- [x] **Similarity Search Algorithm**: The search engine utilizes Pinecone's similarity search to find the most similar documents to the user's query.

### Optional Components

- [ ] **Multi-lingual Support**: The search engine could support multiple languages, allowing users to search for documents in different languages.
- [ ] **Synonym Expansion**: The search engine could include a synonym expansion feature that expands the user's query to include similar words and phrases.
- [ ] **Document Ranking**: The search engine could rank the search results based on their relevance to the user's query.
- [ ] **Entity Extraction**: The search engine could include an entity extraction feature that identifies and extracts entities like people, places, and organizations from the search results.
- [ ] **Integration with Third-Party Services**: The search engine could be integrated with third-party services like Google Drive or Dropbox to provide a more comprehensive search experience.
- [ ] **Customizable Search Index**: The search engine could allow users to choose what text they want to be searched from and create a customized search index.

## How to Run the Code

1. Install the required libraries:
```pip install -r requirements.txt```

2. Set up a Pinecone account and obtain your API key.

3. Replace the `api_key` in the code with your Pinecone API key.

4. Process the data by calling the `process_data` function with your text data:
```python
process_data("your_text_data_here")
