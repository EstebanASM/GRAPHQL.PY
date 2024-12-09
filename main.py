from fastapi import FastAPI
import strawberry
from strawberry.asgi import GraphQL
from typing import List

@strawberry.type
class Movie:
    title: str
    director: str

@strawberry.type
class Query:
    @strawberry.field
    def movies(self) -> List[Movie]:
        # Fetch movies from a data source (e.g., database)
        movies_data = [
            Movie(title="Titanic", director="James Cameron"),
            Movie(title="Parque Jurasico", director="Steven Spielberg"),
            Movie(title="Transformer: La venganza de los caidos", director="Bahía Michael"),
            Movie(title="El señor de los anillos", director="Peter Jackson"),
            Movie(title="Forrest Gump", director="Robert Zemeckis"),
        ]
        return movies_data

schema = strawberry.Schema(query=Query)

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Welcome to the GraphQL API, My name is Esteban Sillo"}

app.add_route("/graphql", GraphQL(schema, debug=True))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
