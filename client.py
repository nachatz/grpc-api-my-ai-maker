import grpc
from generated_code import api_pb2_grpc as api_pb2_grpc
from generated_code import api_pb2 as api_pb2
from logger import Logger


def run():
    Logger.info("Attemping to generate model ...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = api_pb2_grpc.FeaturePrinterStub(channel)
        response = stub.GeneratePythonCode(
            api_pb2.FeatureRequest(
                features=["Feature1", "Feature2"], types=["string", "Type2"]
            )
        )
    Logger.info(f"Received response ... \n\n\n {response.python_code}")


if __name__ == "__main__":
    Logger.initialize("logger")
    run()
