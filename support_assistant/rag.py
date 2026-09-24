from pathlib import Path
import chromadb
from sentence_transformers import SentenceTransformer

# Paths
BASE_DIR = Path(__file__).parent
POLICY_DIR = BASE_DIR / "policies"

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create persistent ChromaDB
client = chromadb.PersistentClient(path=str(BASE_DIR / "chroma_db"))

collection = client.get_or_create_collection(
    name="zepto_policies"
)

print("RAG setup successful!")

# Load policy documents into ChromaDB
documents = []
ids = []

for file_path in sorted(POLICY_DIR.glob("*.txt")):
    text = file_path.read_text(encoding="utf-8")
    documents.append(text)
    ids.append(file_path.stem)

if documents:
    embeddings = model.encode(documents).tolist()

    collection.upsert(
        ids=ids,
        documents=documents,
        embeddings=embeddings
    )

    print(f"Loaded {len(documents)} policy documents into ChromaDB")
else:
    print("No policy documents found")

 # Retrieve relevant policy documents
def retrieve_policy(query, n_results=3):
    query_embedding = model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=n_results
    )

    documents = results["documents"][0]
    return documents