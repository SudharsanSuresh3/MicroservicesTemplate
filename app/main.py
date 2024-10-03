# app/main.py

from fastapi import FastAPI
from nameko.standalone.rpc import ClusterRpcProxy
from config.conf import nameko_config

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "FastAPI and Nameko!"}

@app.get("/nameko/{name}")
async def call_nameko_service(name: str):
    with ClusterRpcProxy(nameko_config) as cluster_rpc:
        response = cluster_rpc.example_service.hello(name)
    return {"response": response}
