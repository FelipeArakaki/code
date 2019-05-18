import java.util.Scanner;

public class delimitadores {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for (int c = 0; c < n; c++) {

            String s = sc.next();
            int e = s.length();
            int aux = e / 2, d = 0;

            while (d < aux) {
                if (s.charAt(d) == '(' && s.charAt(e - d - 1) == ')'
                 || s.charAt(d) == '[' && s.charAt(e - d - 1) == ']'
                 || s.charAt(d) == '{' && s.charAt(e - d - 1) == '}') {
                    //System.out.printf("%c %c", s.charAt(d), s.charAt(e - d - 1));
                    d++;
                } else {
                    break;
                }
            }
            System.out.println((d == aux) ? "SIM" : "NAO");
        }
    }
}
