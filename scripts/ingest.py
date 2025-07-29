def get_db_connection():
    """
    Creates and returns a database connection to PostgreSQL
    Should handle connection parameters and error handling
    """
    pass

def init_vector_db():
    """
    Initializes the vector database
    Creates necessary tables and enables pgvector extension
    """
    pass

def load_documents():
    """
    Loads documents from the data directory
    Handles multiple file types
    """
    pass

def preprocess_documents():
    """
    Cleans and splits documents into chunks
    Returns list of processed chunks with metadata
    """
    pass

def create_embeddings():
    """
    Creates embeddings from text chunks
    Returns vectors ready for database insertion
    """
    pass

def store_vectors(conn, cursor):
    """
    Stores vectors in pgvector database
    Handles batch insertions and transaction management
    """
    pass

def close_db_connection(conn, cursor):
    """
    Safely closes database connections
    Handles commit/rollback decisions
    """
    pass

def main():
    """
    Orchestrates the pipeline with proper DB connection handling:
    connect -> init -> load -> process -> embed -> store -> close
    """
    pass

if __name__ == "__main__":
    main()




from langchain.document_loaders import DirectoryLoader
data_path="data/books"

def load_docs():
    loader=DirectoryLoader(data_path,glob="*.md")
    documents=loader.load()
    return documents





