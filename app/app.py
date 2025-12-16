from fastapi import FastAPI, HTTPException

app = FastAPI()


text_post = {1: {"title": "First Post", "content": "This is the content of the first post."},
             2: {"title": "Second Post", "content": "This is the content of the second post."}}

@app.get("/posts")
def get_posts(limit: int ):
      if limit:
            return list(text_post.values())[:limit]
      return text_post


@app.get("/posts/{id}")
def get_post(id: int):
      if id not in text_post:
            raise HTTPException(status_code=404, detail="Post not found")
      return text_post.get(id)