FROM python:3.11-slim

WORKDIR /app

COPY . .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir fastapi uvicorn chromadb sentence-transformers langgraph

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "support_assistant.api:app", "--host", "0.0.0.0", "--port", "8000"]