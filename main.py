from fastapi import FastAPI

from starlette.middleware.cors import CORSMiddleware

from api import include_routers

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


include_routers(app)