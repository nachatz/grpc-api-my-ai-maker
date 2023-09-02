import grpc
import generated_code.api_pb2_grpc as api_pb2_grpc
import generated_code.api_pb2 as api_pb2
from concurrent import futures


class FeaturePrinterServicer(api_pb2_grpc.FeaturePrinterServicer):
    def GeneratePythonCode(self, request, context):
        python_code = self.generate_python_code(request.features, request.types)
        return api_pb2.PythonCodeResponse(python_code=python_code)

    def generate_python_code(self, features, types):
        code = "def main():\n"

        for feature, feature_type in zip(features, types):
            code += f"    print('{feature}: {feature_type}')\n"

        code += "\nif __name__ == '__main__':\n"
        code += "    main()"

        return code


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    api_pb2_grpc.add_FeaturePrinterServicer_to_server(FeaturePrinterServicer(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
