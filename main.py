from fastapi import FastAPI
from route.route import biblioteca

app = FastAPI()



app.include_router(biblioteca)
