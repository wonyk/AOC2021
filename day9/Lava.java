import java.util.*;
import java.io.*;

class GridPos {
    private int row;
    private int col;

    public GridPos(int row, int col) {
        this.row = row;
        this.col = col;
    }

    @Override
    public boolean equals(Object obj) {
        if (!(obj instanceof GridPos)) {
            return false;
        }
        GridPos another = (GridPos) obj;
        return another.row == row && another.col == col;
    }

    @Override
    public int hashCode() {
        return Objects.hash(row, col);
    }
}

public class Lava {
    private static Set<GridPos> gridSet = new HashSet<>();
    private static int TOP_N = 3;

    public static List<String> getInputArr() {
        List<String> list = new ArrayList<>();
        try (Scanner sc = new Scanner(new File("input.txt"))) {
            // try (Scanner sc = new Scanner(new File("testinp.txt"))) {
            while (sc.hasNextLine()) {
                list.add(sc.nextLine());
            }
        } catch (FileNotFoundException e) {
            System.out.println("File not found!");
            throw new RuntimeException("File not found");
        }
        return list;
    }

    public static Integer[][] parseInput(List<String> list) {
        Integer[][] result = new Integer[list.size()][list.get(0).length()];
        for (int i = 0; i < list.size(); i++) {
            String s = list.get(i);
            for (int j = 0; j < s.length(); j++) {
                result[i][j] = Character.getNumericValue(s.charAt(j));
            }
        }
        return result;
    }

    public static boolean checkTopLarger(Integer[][] input, int row, int col) {
        return input[row - 1][col] > input[row][col];
    }

    public static boolean checkBotLarger(Integer[][] input, int row, int col) {
        return input[row + 1][col] > input[row][col];
    }

    public static boolean checkLeftLarger(Integer[][] input, int row, int col) {
        return input[row][col - 1] > input[row][col];
    }

    public static boolean checkRightLarger(Integer[][] input, int row, int col) {
        return input[row][col + 1] > input[row][col];
    }

    public static boolean check(Integer[][] input, int row, int col) {
        boolean result = true;
        if (row != 0) {
            result &= checkTopLarger(input, row, col);
        }
        if (col != 0) {
            result &= checkLeftLarger(input, row, col);
        }
        if (row != input.length - 1) {
            result &= checkBotLarger(input, row, col);
        }
        if (col != input[0].length - 1) {
            result &= checkRightLarger(input, row, col);
        }
        return result;
    }

    public static int getPartOneResult(Integer[][] input) {
        int sum = 0;
        for (int i = 0; i < input.length; i++) {
            for (int j = 0; j < input[i].length; j++) {
                if (check(input, i, j)) {
                    sum += (1 + input[i][j]);
                }
            }
        }
        return sum;
    }

    public static int getBasins(Integer[][] input, int row, int col) {
        // Edge case
        if (row < 0 || row >= input.length || col < 0 || col >= input[0].length) {
            return 0;
        }

        // Check if it has been counted before in some other basin
        GridPos pos = new GridPos(row, col);
        if (gridSet.contains(pos)) {
            return 0;
        }

        // If not, add to the visited list
        gridSet.add(pos);

        // Base case
        if (input[row][col] == 9) {
            return 0;
        }

        // Recursive
        return 1 + getBasins(input, row - 1, col) + getBasins(input, row + 1, col) + getBasins(input, row, col - 1)
                + getBasins(input, row, col + 1);

    }

    public static int getPartTwoResult(Integer[][] input) {
        int sum = 1;
        List<Integer> basinSizes = new ArrayList<>();

        for (int i = 0; i < input.length; i++) {
            for (int j = 0; j < input[i].length; j++) {
                GridPos pos = new GridPos(i, j);
                if (input[i][j] != 9 && !gridSet.contains(pos)) {
                    basinSizes.add(getBasins(input, i, j));
                }
            }
        }

        Integer[] basinArr = basinSizes.toArray(new Integer[0]);
        Arrays.sort(basinArr, Collections.reverseOrder());
        for (int i = 0; i < TOP_N; i++) {
            sum *= basinArr[i];
        }
        return sum;
    }

    public static void main(String[] args) {
        List<String> inputList = getInputArr();
        Integer[][] inputArr = parseInput(inputList);
        System.out.println("Part 1: " + getPartOneResult(inputArr));
        System.out.println("Part 2: " + getPartTwoResult(inputArr));
    }
}