package BaseToDecimal;

import java.util.Scanner;

/**
 * Converts any number with base 2-9 to a base 10 decimal equivalent
 */
public class BaseToDecimal {

    /**
     * Checks if the base input number is between 2-9
     * @param baseInput - an integer between 2-9
     * @return boolean - true if this is a valid base, else false
     */
    public static boolean checkValidBase (Integer baseInput) {

        if (baseInput < 2 || baseInput > 9) {
            return false;
        }
        else {
            return true;
        }

    }

    /**
     * Checks if the input number meets criteria
     * @param inputInt - an integer
     * @return boolean - true if this is a valid base, else false
     */
    public static boolean checkValidInput (Integer inputInt) {

        // temp
       return true;

    }

    /**
     * Converts the input to a decimal
     * @param input - converts an integer string into a decimal
     * @return
     */
    public static Integer handleConversion (Integer input, Integer base) {

        Integer result = 0;

        int n = input.toString().length();
        String inputString = input.toString();

        int counter = 0;
        for (int i = n - 1; i >= 0; i--) {
            char diChar = inputString.charAt(counter);
            int diInt = Integer.parseInt("" + diChar);

            result = (result * base) + diInt;
            counter++;
        }

        return result;

    }

    /**
     * Formats the success message
     * @param result - the resulting integer to include in the success message
     * @return message - returns the success message to print in the console
     */
    private static String successMessage (Integer result) {
        return "The equivalent number in base 10 format is " + result;
    }

    /**
     * Generates the error message for an incorrect base entry
     * @return
     */
    private static String errorMessage () {
        return "Incorrect base system. Please enter a base from 2 - 9";
    }

    public static void main(String[] args) {
        Scanner inputScanner = new Scanner(System.in);

        int base = -1;

        do {
            System.out.print("Please enter a base from 2 - 9: ");
            int input = inputScanner.nextInt();

            if (checkValidBase(input)) {
                base = input;
            }
            else {
                System.out.println(errorMessage());
            }

        } while (base == -1);

        int inputInt = -1;

        do {
            System.out.print("Enter a base " + base + " number: ");
            int input = inputScanner.nextInt();

            if (checkValidInput(input)) {
                inputInt = input;
            }
            else {
                System.out.println(errorMessage());
            }

        } while (inputInt == -1);

        Integer result = handleConversion(inputInt, base);

        System.out.println(successMessage(result));

        inputScanner.close();

    }

}
