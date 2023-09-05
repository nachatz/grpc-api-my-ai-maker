import grpc
from generated_code import api_pb2_grpc as api_pb2_grpc
from generated_code import api_pb2 as api_pb2
from logger import Logger


def write_code_to_file(code_string, file_name):
    with open(file_name, "w") as file:
        file.write(code_string)


def run():
    Logger.info("Attemping to generate model ...")
    features = ["id", "name", "age", "label"]
    types = ["int", "string", "int", "int"]
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = api_pb2_grpc.FeaturePrinterStub(channel)
        response = stub.GeneratePythonCode(
            api_pb2.FeatureRequest(features=features, types=types)
        )
    Logger.info(f"Received response ... \n\n\n {response.python_code}")
    write_code_to_file(response.python_code, "./sample/main.py")


if __name__ == "__main__":
    Logger.initialize("logger")
    run()
