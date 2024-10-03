# microservices/service.py

from nameko.rpc import rpc

class ExampleService:
    name = "example_service"

    @rpc
    def hello(self, name: str):
        return f"Hello, {name} from Nameko!"
