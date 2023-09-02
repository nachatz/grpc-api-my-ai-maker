import grpc
import generated_code.api_pb2_grpc as api_pb2_grpc
import generated_code.api_pb2 as api_pb2


def run():
    print("Attemping to generate model ...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = api_pb2_grpc.FeaturePrinterStub(channel)
        response = stub.GeneratePythonCode(
            api_pb2.FeatureRequest(
                features=["Feature1", "Feature2"], types=["Type1", "Type2"]
            )
        )
    print("Client received: " + response.python_code)


if __name__ == "__main__":
    run()
