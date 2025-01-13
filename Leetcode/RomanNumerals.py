class Solution:
    def intToRoman(self, num: int) -> str:
        num_string = str(num)
        num_array = list(num_string)
        decimal_place = 10 ** (len(num_array) - 1)
        roman_numeral = []
        for digit in num_array:
            decimal_digit = int(digit)
            x = decimal_digit * decimal_place
            print(x)
            if decimal_place == 1000:
                for i in range(decimal_digit):
                    roman_numeral.append("M")  
            elif decimal_place == 100:
                if decimal_digit == 4:
                    roman_numeral.append("CD")
                    decimal_digit = decimal_digit - 4
                elif decimal_digit == 9:
                    roman_numeral.append("CM")
                    decimal_digit = decimal_digit - 9
                elif decimal_digit >= 5:
                    roman_numeral.append("D")
                    decimal_digit = decimal_digit - 5
                for i in range(decimal_digit):
                    roman_numeral.append("C")
            elif decimal_place == 10:
                if decimal_digit == 4:
                    roman_numeral.append("XL")
                    decimal_digit = decimal_digit - 4
                elif decimal_digit == 9:
                    roman_numeral.append("XC")
                    decimal_digit = decimal_digit - 9
                elif decimal_digit >= 5:
                    roman_numeral.append("L")
                    decimal_digit = decimal_digit - 5
                for i in range(decimal_digit):
                    roman_numeral.append("X")
            elif decimal_place == 1:
                if decimal_digit == 4:
                    roman_numeral.append("IV")
                    decimal_digit = decimal_digit - 4
                elif decimal_digit == 9:
                    roman_numeral.append("IX")
                    decimal_digit = decimal_digit - 9
                elif decimal_digit >= 5:
                    roman_numeral.append("V")
                    decimal_digit = decimal_digit - 5
                for i in range(decimal_digit):
                    roman_numeral.append("I")
            decimal_place = decimal_place / 10
        return "".join(roman_numeral)
if __name__== "__main__":
    s = Solution()
    s.intToRoman(1994)