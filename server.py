import grpc
import generated_code.api_pb2_grpc as api_pb2_grpc
import generated_code.api_pb2 as api_pb2
from services.python.generator import GeneratorService
from concurrent import futures
from logger import Logger


class FeaturePrinterServicer(api_pb2_grpc.FeaturePrinterServicer):
    def __init__(self):
        super().__init__()
        self.code_generator = GeneratorService()

    def GeneratePythonCode(self, request, context):
        python_code = self.code_generator.generate_python_code(
            request.features, request.types
        )
        Logger.info(f"Generated: \n{python_code}")
        return api_pb2.PythonCodeResponse(python_code=python_code)


def serve():
    Logger.initialize("logger")
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    api_pb2_grpc.add_FeaturePrinterServicer_to_server(FeaturePrinterServicer(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    Logger.info(f"Server successfully started on port: {port}")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
