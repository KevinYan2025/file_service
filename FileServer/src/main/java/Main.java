import java.io.File;
import java.io.FileFilter;
import java.io.IOException;
import java.nio.file.*;
import java.nio.file.attribute.BasicFileAttributes;
import java.util.EnumSet;

public class Main {
        public static void main(String args[]) throws IOException {
            Path directory = Paths.get("/Users/zhixiangyan/Desktop/school/vip/learnGrpc");

            System.out.println(directory.getClass());
        }
}
