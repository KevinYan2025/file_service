import grpc
from fileService_pb2 import FileRequest
from fileService_pb2_grpc import FileServerStub

def run():
    # Create a gRPC channel
    channel = grpc.insecure_channel('localhost:8080')

    # Create a stub (client)
    stub = FileServerStub(channel)

    # Create a request
    file_request = FileRequest(fileName="1234.txt")

    # Call the RPC method and get the response
    file_response = stub.getFile(file_request)

    # Print the response
    print(file_response)

if __name__ == '__main__':
    n = 0;
    for n in range (10000):
        n = n+1
        run()