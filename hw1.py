class RomanConverter:
    def int_to_roman(self, num):
        
        roman_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        result = []
        for value, numeral in roman_map:
            count = num // value
            if count > 0:
                result.append(numeral * count)
                num -= value * count
            if num == 0:
                break

        return "".join(result)
user_input = int(input("enter a number from (1-3999): "))
converter = RomanConverter()
roman_value = converter.int_to_roman(user_input)
print(f"The Roman numeral for {user_input} is: {roman_value}")
