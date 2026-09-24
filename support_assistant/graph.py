from typing import TypedDict
from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer
from langgraph.graph import StateGraph, END


BASE_DIR = Path(__file__).resolve().parent
CHROMA_PATH = BASE_DIR / "chroma_db"

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path=str(CHROMA_PATH))
collection = client.get_or_create_collection(name="zepto_policies")


class SupportState(TypedDict):
    question: str
    intent: str
    answer: str
    sources: list[str]


def classify_intent(state: SupportState):
    question = state["question"].lower()

    policy_keywords = [
        "order",
        "cancel",
        "refund",
        "delivery",
        "membership",
        "payment",
        "return",
        "policy",
        "zepto",
    ]

    if any(word in question for word in policy_keywords):
        return {"intent": "policy"}

    return {"intent": "general"}


def retrieve_and_answer(state: SupportState):
    question = state["question"]

    query_embedding = model.encode([question]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=3,
    )

    documents = results.get("documents", [[]])[0]
    ids = results.get("ids", [[]])[0]

    if documents:
        answer = documents[0]
    else:
        answer = "No relevant policy information was found."

    return {
        "answer": answer,
        "sources": ids,
    }


def direct_answer(state: SupportState):
    return {
        "answer": "I can help with Zepto support and policy-related questions.",
        "sources": [],
    }


def route_question(state: SupportState):
    if state["intent"] == "policy":
        return "retrieve"

    return "direct"


workflow = StateGraph(SupportState)

workflow.add_node("classify_intent", classify_intent)
workflow.add_node("retrieve", retrieve_and_answer)
workflow.add_node("direct", direct_answer)

workflow.set_entry_point("classify_intent")

workflow.add_conditional_edges(
    "classify_intent",
    route_question,
    {
        "retrieve": "retrieve",
        "direct": "direct",
    },
)

workflow.add_edge("retrieve", END)
workflow.add_edge("direct", END)

app = workflow.compile()


if __name__ == "__main__":
    question = input("Ask a support question: ")

    result = app.invoke(
        {
            "question": question,
            "intent": "",
            "answer": "",
            "sources": [],
        }
    )

    print("\nIntent:", result["intent"])
    print("Answer:", result["answer"])
    print("Sources:", result["sources"])