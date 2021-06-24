package tests;
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;
import BaseToDecimal.BaseToDecimal;

public class BaseToDecimalTest {

    @Test
    void invalidBaseReturnsFalse () {

        BaseToDecimal testClass = new BaseToDecimal();

        int base1 = -1;
        int base2 = 0;
        int base3 = 1;
        int base4 = 10;
        int base5 = 100;

        assertEquals(false, testClass.checkValidBase(base1));
        assertEquals(false, testClass.checkValidBase(base2));
        assertEquals(false, testClass.checkValidBase(base3));
        assertEquals(false, testClass.checkValidBase(base4));
        assertEquals(false, testClass.checkValidBase(base5));
    }

    @Test
    void validBaseReturnsTrue () {

        BaseToDecimal testClass = new BaseToDecimal();

        int base1 = 2;
        int base2 = 3;
        int base3 = 4;
        int base4 = 5;
        int base5 = 6;
        int base6 = 7;
        int base7 = 8;
        int base8 = 9;

        assertEquals(true, testClass.checkValidBase(base1));
        assertEquals(true, testClass.checkValidBase(base2));
        assertEquals(true, testClass.checkValidBase(base3));
        assertEquals(true, testClass.checkValidBase(base4));
        assertEquals(true, testClass.checkValidBase(base5));
        assertEquals(true, testClass.checkValidBase(base6));
        assertEquals(true, testClass.checkValidBase(base7));
        assertEquals(true, testClass.checkValidBase(base8));
    }

    @Test
    void successfullyHandlesBase2Conversion () {

        BaseToDecimal testClass = new BaseToDecimal();

        assertEquals(1, testClass.handleConversion(1, 2));
        assertEquals(2, testClass.handleConversion(10, 2));
        assertEquals(5, testClass.handleConversion(101, 2));
        assertEquals(5, testClass.handleConversion(0101, 2));
        assertEquals(5, testClass.handleConversion(00101, 2));
        assertEquals(37, testClass.handleConversion(100101, 2));

    }

    @Test
    void successfullyHandlesBase8Conversion () {

        BaseToDecimal testClass = new BaseToDecimal();


        assertEquals(167, testClass.handleConversion(247, 8));
        assertEquals(64, testClass.handleConversion(100, 8));
        assertEquals(645, testClass.handleConversion(1205, 8));
        assertEquals(45, testClass.handleConversion(55, 8));
        assertEquals(34, testClass.handleConversion(42, 8));

    }
}