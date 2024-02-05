import grpc
from fileService_pb2 import FileName
from fileService_pb2_grpc import FileServerStub

def run():
    # Create a gRPC channel
    channel = grpc.insecure_channel('localhost:8080')

    # Create a stub (client)
    stub = FileServerStub(channel)

    # Create a request
    file_name = FileName(fileName="1234.txt")

    # Call the RPC method and get the response
    file_content = stub.getFileContent(file_name)

    # Print the response
    print(file_content)

if __name__ == '__main__':
    n = 0
    for n in range (5000):
        n = n+1
        run()