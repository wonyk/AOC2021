import java.util.*;
import java.io.*;

class dive_p2 {
    private static int depth = 0;
    private static int forward = 0;
    private static int aim = 0;

    public static void main(String[] args) {
        String file = "input.txt";

        try (Scanner scanner = new Scanner(new File(file))) {
            while (scanner.hasNext()) {
                String data = scanner.nextLine();
                parse(data);
            }

            System.out.printf("The final result: %d%n", depth * forward);

        } catch (FileNotFoundException e) {
            System.out.println("File not found!");
        }
    }

    /**
     * Break the string into the command on the left and the number on the right.
     * Then do the comparison and update the variables in the class. We assume there
     * is only the forward, up and down commands with no errors
     * 
     * @param data
     */
    private static void parse(String data) {
        String[] dataArr = data.split(" ");

        String command = dataArr[0];
        int num = Integer.parseInt(dataArr[1]);

        if (command.equals("forward")) {
            forward += num;
            depth += aim * num;
        } else if (command.equals("up")) {
            aim -= num;
        } else {
            aim += num;
        }
    }
}