print("task 1.1")
def get_keys_with_value_true(dict):
    true_keys = []
    for key, value in dict.items():
        try:
            if value == True:
                true_keys.append(key)
        except TypeError:
            continue
    return true_keys
example_dict = {"a": True, "b": False, "c": True}
print(get_keys_with_value_true(example_dict))

print("\ntask 1.2")
def get_unique_elements(list):
    unique_elements = []
    try:
        counts = {}
        for number in list:
            if number in counts:
                counts[number] += 1
            else:
                counts[number] = 1

        for number, count in counts.items():
            if count == 1:
                unique_elements.append(number)
    except Exception as e:
        print("An error occurred:", e)
    return unique_elements
print(get_unique_elements([1, 2, 3, 1, 2, 4]))

print("\ntask 1.3")
def get_date_in_format(date):
    formatted_date = ""
    try:
        parts = date.split('.')
        if len(parts) == 3:
            formatted_date = "{}.{}.{}".format(parts[2], parts[1], parts[0])
    except Exception as e:
        print("An error occurred:", e)
    return formatted_date
print(get_date_in_format("2023.10.23"))

print("\ntask 1.4")
def get_elements_with_no_more_than_two_occurrences(list):
    unique_elements = []
    try:
        counts = {}
        for number in list:
            if number in counts:
                counts[number] += 1
            else:
                counts[number] = 1

        for number, count in counts.items():
            if count <= 2:
                unique_elements.append(number)
    except Exception as e:
        print("An error occurred:", e)
    return unique_elements
print(get_elements_with_no_more_than_two_occurrences([1, 2, 3, 1, 2, 4]))

print("\ntask 1.5")
def get_words_from_string(string):
    try:
        words = string.split()
    except Exception as e:
        print("An error occurred:", e)
        words = []
    return words
print(get_words_from_string("This is a string with several words."))

print("\ntask 2.6")
def get_unique_elements_with_count(lst):
    elements_count = {}
    try:
        for element in lst:
            if element in elements_count:
                elements_count[element] += 1
            else:
                elements_count[element] = 1
    except Exception as e:
        print("An error occurred:", e)
    return elements_count
print(get_unique_elements_with_count([1, 2, 3, 1, 2, 4, 1, 2]))

print("\ntask 2.7")
def get_prime_numbers(n):
    prime_numbers = []
    number = 2
    while number <= n:
        is_prime = True
        divisor = 2
        while divisor < number:
            if number % divisor == 0:
                is_prime = False
                break
            divisor += 1
        if is_prime:
            prime_numbers.append(number)
        number += 1
    return prime_numbers
print(get_prime_numbers(100))

print("\ntask 2.8")
def get_prime_numbers_in_list(lst):
    prime_numbers = []
    try:
        for number in lst:
            if number > 1:
                is_prime = True
                for divisor in range(2, number):
                    if number % divisor == 0:
                        is_prime = False
                        break
                if is_prime:
                    prime_numbers.append(number)
    except Exception as e:
        print("An error occurred:", e)
    
    return prime_numbers
print(get_prime_numbers_in_list([2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))

print("\ntask 2.9")
from datetime import datetime

def get_difference_between_dates(date1_str, date2_str):
    try:
        date1 = datetime.strptime(date1_str, "%Y.%m.%d").date()
        date2 = datetime.strptime(date2_str, "%Y.%m.%d").date()

        difference = abs((date2 - date1).days)
        return difference
    except ValueError as e:
        return f"Error parsing dates: {e}"
print(get_difference_between_dates("2023.10.23", "2023.10.24"))

print("\ntask 3.10")
def get_decimal_number_from_binary_string(binary_string):
    try:
        decimal_number = int(binary_string, 2)
        return decimal_number
    except ValueError as e:
        return f"Error converting binary to decimal: {e}"
print(get_decimal_number_from_binary_string("10110011"))

print("\ntask 3.11")
def get_perfect_squares(numbers_list):
    perfect_squares = []
    try:
        for number in numbers_list:
            root = number**0.5
            if root.is_integer():
                perfect_squares.append(number)
    except Exception as e:
        print(f"An error occurred: {e}")
    return perfect_squares
print(get_perfect_squares([4, 25, 81, 10, 23]))

print("\ntask 3.12")
def sort_by_price(shopping_list):
    sorted_list = sorted(shopping_list, key=lambda item: item['price'])
    return sorted_list

shopping_list = [
    {"name": "Apple", "price": 100},
    {"name": "Banana", "price": 50},
    {"name": "Orange", "price": 20}
]
print(sort_by_price(shopping_list))

print("\ntask 3.13")
def get_words_starting_with_vowel(words):
    vowels = 'aeiou'
    result = []
    for word in words:
        if word[0].lower() in vowels:
            result.append(word)
    return result
print(get_words_starting_with_vowel(["apple", "banana", "orange", "bear", "cat"]))