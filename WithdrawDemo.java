import java.util.Scanner;

public class WithdrawDemo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double balance = 10000.0;

        System.out.println("Welcome to the withdrawal program.");
        System.out.printf("Current balance: $%.2f%n", balance);
        System.out.println("Tip: type exit to quit.");

        while (true) {
            System.out.print("\nEnter withdrawal amount: ");
            String userInput = scanner.nextLine().trim();

            if (userInput.equalsIgnoreCase("exit")) {
                System.out.printf("Program exited. Final balance: $%.2f%n", balance);
                break;
            }

            double amount;
            try {
                amount = Double.parseDouble(userInput);
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Enter a number, or type exit to quit.");
                continue;
            }

            if (amount <= 0) {
                System.out.println("Withdrawal amount cannot be less than or equal 0. Please try again.");
                continue;
            }

            if (amount > balance) {
                System.out.printf("Withdrawal amount is greater than the current balance: $%.2f%n", balance);
                System.out.println("Please enter a new amount, or type exit to quit.");
                continue;
            }

            balance -= amount;
            System.out.printf("Withdrawal successful. Amount: $%.2f. Remaining balance: $%.2f%n", amount, balance);

            if (balance == 0) {
                System.out.println("Balance is now 0. Type exit if you want to quit.");
                continue;
            }

            System.out.print("Do you want to continue? Type Y to continue, or exit to quit: ");
            String answer = scanner.nextLine().trim();

            if (answer.equalsIgnoreCase("exit")) {
                System.out.printf("Program exited. Final balance: $%.2f%n", balance);
                break;
            }

            if (!answer.equals("Y")) {
                System.out.printf("Input is not Y. Program ended. Final balance: $%.2f%n", balance);
                break;
            }
        }

        scanner.close();
    }
}
