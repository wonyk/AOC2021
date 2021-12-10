import java.util.*;
import java.io.*;

public class Syntax {
    private static String[] inputArr;
    private static List<Stack<Character>> incompleteList = new ArrayList<>();

    private static Map<Character, Integer> scoringTableP1 = new HashMap<>();
    private static Map<Character, Integer> scoringTableP2 = new HashMap<>();
    private static Map<Character, Character> bracketPairs = new HashMap<>();

    private static void getRawInput() {
        List<String> inputStr = new ArrayList<>();

        try (Scanner sc = new Scanner(new File("input.txt"))) {
            while (sc.hasNextLine()) {
                inputStr.add(sc.nextLine());
            }
        } catch (FileNotFoundException e) {
            System.out.println("File not found!");
            throw new RuntimeException("File not found!");
        }

        inputArr = inputStr.toArray(new String[0]);
    }

    private static void initializeScoringTables() {
        scoringTableP1.put(')', 3);
        scoringTableP1.put(']', 57);
        scoringTableP1.put('}', 1197);
        scoringTableP1.put('>', 25137);

        scoringTableP2.put('(', 1);
        scoringTableP2.put('[', 2);
        scoringTableP2.put('{', 3);
        scoringTableP2.put('<', 4);
    }

    private static void initializeBracketPairs() {
        bracketPairs.put(')', '(');
        bracketPairs.put(']', '[');
        bracketPairs.put('}', '{');
        bracketPairs.put('>', '<');
    }

    private static int checkCorruptScore(int idx) {
        String line = inputArr[idx];
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < line.length(); i++) {
            Character c = line.charAt(i);
            // Check if closing bracket
            Character openingBracket = bracketPairs.get(c);
            if (openingBracket != null) {
                if (stack.size() == 0) {
                    // should not happen
                    return 0;
                }
                Character last = stack.pop();
                if (last != openingBracket) {
                    return scoringTableP1.get(c);
                }
            } else {
                // Else, it is opening, add to the stack
                stack.add(c);
            }
        }
        // Incomplete, add to list. Assume that no lines are good.
        incompleteList.add(stack);
        return 0;
    }

    private static long getLineScore(int idx) {
        Stack<Character> stack = incompleteList.get(idx);
        long result = 0;
        while (stack.size() != 0) {
            result *= 5;
            result += scoringTableP2.get(stack.pop());
        }
        return result;
    }

    private static int getPartOneAnswer() {
        int score = 0;
        for (int i = 0; i < inputArr.length; i++) {
            score += checkCorruptScore(i);
        }
        return score;
    }

    private static Long getPartTwoAnswer() {
        List<Long> allScores = new ArrayList<>();
        for (int i = 0; i < incompleteList.size(); i++) {
            allScores.add(getLineScore(i));
        }
        Collections.sort(allScores);
        return allScores.get(allScores.size() / 2);
    }

    public static void main(String[] args) {
        getRawInput();
        initializeScoringTables();
        initializeBracketPairs();

        System.out.println("Part 1: " + getPartOneAnswer());
        System.out.println("Part 2: " + getPartTwoAnswer());
    }
}