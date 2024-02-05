import io.grpc.Server;
import io.grpc.ServerBuilder;
import io.grpc.alts.AltsServerBuilder;
import io.grpc.stub.StreamObserver;
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.logging.Logger;

public class FileServer extends FileServerGrpc.FileServerImplBase {
    private int nthFileSend = 0;
    private static final Logger logger = Logger.getLogger(FileServer.class.getName());
    public static void main(String[] args) throws Exception{
        Server server = ServerBuilder.forPort(8080)
                .addService(new FileServer())
                .build();
        server.start();
        server.awaitTermination();
    }
    @Override
    public void getFileContent(FileName request, StreamObserver<FileContent> responseObserver) {
        responseObserver.onNext(searchFile(request));
        responseObserver.onCompleted();
        System.out.println("File send! - " + nthFileSend++);
    }
    private FileContent searchFile(FileName fileName) {
        try {
            File fileDirectory = new File("/Users/zhixiangyan/Desktop");
            if (fileDirectory.isDirectory()) {
                File[] files = fileDirectory.listFiles();
                if (files != null) {
                    for (File file : files) {
                        if (file.getName().equals(fileName.getFileName())) {
                            return FileContent.newBuilder()
                                    .setFileContent(Files.readString(Paths.get(file.toString())))
                                    .build();
                        }
                    }
                }
            }
        } catch (Exception e) {
            logger.warning(e.toString());
        }

        return null;
    }
}
