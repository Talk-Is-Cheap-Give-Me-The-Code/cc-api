from .auth.router import auth_router
from .round.router import round_router
from .tournament.router import tournament_router
from .user.router import user_router

from fastapi import FastAPI

app = FastAPI()

app.include_router(auth_router)
app.include_router(round_router)
app.include_router(tournament_router)
app.include_router(user_router)

@app.get("/")
def read_root():
    return {"Chess": "Coordinator"}