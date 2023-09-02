import grpc
import generated_code.api_pb2_grpc as api_pb2_grpc
import generated_code.api_pb2 as api_pb2
from logger import Logger 

def run():
    Logger.info("Attemping to generate model ...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = api_pb2_grpc.FeaturePrinterStub(channel)
        response = stub.GeneratePythonCode(
            api_pb2.FeatureRequest(
                features=["Feature1", "Feature2"], types=["Type1", "Type2"]
            )
        )
    Logger.info(f"Received response ... \n {response.python_code}")


if __name__ == "__main__":
    Logger.initialize("logger")
    run()
