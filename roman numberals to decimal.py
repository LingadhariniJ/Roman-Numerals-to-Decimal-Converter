def roman_to_decimal(roman_num):

#creating a dictionary
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    
#Iterating numerals in reverse order
    for char in reversed(roman_num):

#Calculating decimal equivalent
        current_value = roman_dict[char]

        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value

#Updating previous value
        prev_value = current_value

#Returning the total as the Decimal Equivalent
    return total

#Taking Input from the user
roman_input = input("Enter a Roman numeral: ")

# Convert and display the result
decimal_equivalent = roman_to_decimal(roman_input.upper())
print(f"Decimal equivalent: {decimal_equivalent}")
