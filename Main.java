import java.util.Scanner;

public class Main {
    String fname;
    int age = 29;
    String lname;
    
    public static void main(String[] args) {
        Main persona = new Main();
        Scanner scanner = new Scanner(System.in);

        // Ask for user input
        System.out.print("Enter your first name: ");
        persona.fname = scanner.nextLine();

        System.out.print("Enter your last name: ");
        persona.lname = scanner.nextLine();

        // Print out the user's name and age
        System.out.println("My name is: " + persona.fname + " " + persona.lname);
        System.out.println("My age is: " + persona.age);

        scanner.close();
    }
}
