package tests;

import DecimalToBase.DecimalToBase;
import org.junit.jupiter.api.Test;

import java.util.Scanner;

import static DecimalToBase.DecimalToBase.handleConversion;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class DecimalToBaseTests {

    @Test
    void successfullyHandlesConversion () {

        assertEquals("10100111", handleConversion(167, 2));
        assertEquals("247", handleConversion(167, 8));
        assertEquals("A7", handleConversion(167, 16));

    }

}
