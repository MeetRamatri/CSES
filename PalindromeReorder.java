import java.util.*;

public class PalindromeReorder {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        int[] charCount = new int[26];
        for (char c : s.toCharArray()) {
            charCount[c - 'A']++;
        }
        int odd = 0;
        for (int count : charCount) {
            if (count % 2 != 0) {
                odd++;
            }
        }
        if (odd > 1) {
            System.out.println("NO SOLUTION");
            return;
        }
        
        StringBuilder left = new StringBuilder();
        StringBuilder middle = new StringBuilder();
        
        for (int i = 0; i < 26; i++) {
            char c = (char) (i + 'A');
            if (charCount[i] % 2 == 0) {
                for (int j = 0; j < charCount[i] / 2; j++) {
                    left.append(c);
                }
            } else {
                for (int j = 0; j < charCount[i] / 2; j++) {
                    left.append(c);
                }
                middle.append(c);
            }
        }
        String right = left.reverse().toString();
        System.out.println(left.reverse().toString() + middle.toString() + right);
    }
}
