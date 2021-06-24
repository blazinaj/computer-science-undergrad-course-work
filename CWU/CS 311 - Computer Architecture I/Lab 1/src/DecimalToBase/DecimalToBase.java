package DecimalToBase;

import java.util.Scanner;

/**
 * Converts a Decimal number to the equivalent number of any base
 */
public class DecimalToBase {

    /**
     * Maps integers 10-16 to the corresponding letter for base 16+ conversions
     * @param input - the integer to try and map for
     * @return - returns a string representing the mapped value
     */
    private static String getNumberMapping (Integer input) {
        switch (input) {
            case 10: return "A";
            case 11: return "B";
            case 12: return "C";
            case 13: return "D";
            case 14: return "E";
            case 15: return "F";
            case 16: return "G";
            default: return input.toString();
        }
    }

    /**
     * Converts an arbitrary number input to a different base
     * @param input - the input for conversion.
     * @param base - an integer between 2-9 for conversion
     * @return result - the converted number in string format
     */
    public static String handleConversion (String input, Integer base) {

        double quotient = Double.parseDouble(input);

        String remainders = "";

        while (quotient > 0) {

            double remainderDecimal = quotient % base;
            Integer remainderInt = (int) remainderDecimal;
            String mappedInt = getNumberMapping(remainderInt);
            remainders = mappedInt + remainders;
            quotient = (int)quotient / base;

        }

        return remainders;

    }

    /**
     * Formats the success message
     * @param result - the resulting integer to include in the success message
     * @return message - returns the success message to print in the console
     */
    private static String successMessage (String result, Integer base) {
        return "Base " + base + ": " + result;
    }

    public static void main (String[] args) {
        Scanner inputScanner = new Scanner(System.in);

        String input;

        do {
            System.out.print("Please enter a base 10 number: ");
            Integer scannerInput = inputScanner.nextInt();

            input = scannerInput.toString();

        } while (input.isEmpty());

        String hexResult = handleConversion(input, 16);
        String octalResult = handleConversion(input, 8);
        String binaryResult = handleConversion(input, 2);

        System.out.println(successMessage(binaryResult, 2));
        System.out.println(successMessage(octalResult, 8));
        System.out.println(successMessage(hexResult, 16));

        inputScanner.close();
    }
}
