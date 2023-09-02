import grpc
import generated_code.api_pb2_grpc as api_pb2_grpc
import generated_code.api_pb2 as api_pb2
from concurrent import futures
from logger import Logger


class FeaturePrinterServicer(api_pb2_grpc.FeaturePrinterServicer):
    def GeneratePythonCode(self, request, context):
        python_code = self.generate_python_code(request.features, request.types)
        Logger.info(f"Generated: \n{python_code}")
        return api_pb2.PythonCodeResponse(python_code=python_code)

    def generate_python_code(self, features, types):
        Logger.info(f"Generating python3 code for: \n {features}")

        typed_features = zip(features, types)
        code = "def main():\n"

        for feature, feature_type in typed_features:
            code += f"    print('{feature}: {feature_type}')\n"

        code += "\nif __name__ == '__main__':\n"
        code += "    main()"

        return code


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
