from fastapi import FastAPI
from route.route import bibliotec

app = FastAPI()



app.include_router(bibliotec)
