from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health_check():
    return {"status": "ok"}


# TODO: This end point is for passing query to the RAG system. We will implement the RAG system in the next steps.


@app.get("/echo")
def echo(q: str):
    return {"message": q}