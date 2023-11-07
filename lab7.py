import os

folder_path = r'C:\Lessons\3 course\Python'
file_name = 'text1.txt'
file_path = os.path.join(folder_path, file_name)

content = """Lorem ipsum dolor sit amet, consectetur Adipiscing elit.
Nullam nec purus at orci accumsan malesuada.
Duis aute irure Dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
The quick Brown fox jumps over the lazy Dog.
Fugiat nulla to the end of.
Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium.
Aenean faucibus finibus mi, at sodales elit sollicitudin ac.
Mauris efficitur neque vitae libero malesuada, et luctus sem convallis.
This line should Fail to comply.
Lorem ipsum dolor sit all consectetur adipiscing elit none

thisshouldbethelongestwordinthefile

I am a Boy.
But the real challenge will be finding a lorem that Ends with an f.
Throughout the text, none of the lines should start with a capital D unless intended for demonstration.

It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.

all the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet.
"""
with open(file_path, 'w') as file:
    file.write(content)

# 1.
def read_and_display(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            print(line, end='')

# 2.
import random
def read_random_line(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    random_line = random.choice(lines)
    print(random_line)

# 3.
def count_uppercase(file_name):
    uppercase_count = 0
    with open(file_name, 'r') as file:
        for line in file:
            for char in line:
                if char.isupper():
                    uppercase_count += 1
    return uppercase_count

# 4.
def count_lines_not_starting_with_d(file_name):
    count = 0
    with open(file_name, 'r') as file:
        for line in file:
            if not line.startswith('D'):
                count += 1
    return count

# 5.
def count_words_ending_with_f(file_name):
    count = 0
    with open(file_name, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if word.lower().endswith('f'):
                    count += 1
    return count

# 6.
def count_all_and_none(file_name):
    count_all, count_none = 0, 0
    with open(file_name, 'r') as file:
        for line in file:
            words = line.split()
            count_all += words.count("all")
            count_none += words.count("none")
    return count_all, count_none

# 7.
def word_frequency(file_name):
    freq = {}
    with open(file_name, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                freq[word] = freq.get(word, 0) + 1
    return freq

# 8.
def find_longest_word(file_name):
    longest_word = ''
    with open(file_name, 'r') as file:
        for line in file:
            words = line.split()
            longest_word_in_line = max(words, key=len, default='')
            if len(longest_word_in_line) > len(longest_word):
                longest_word = longest_word_in_line
    return longest_word


# 9.
def correct_content(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
    corrected_content = content.replace('B', 'J')
    print(corrected_content)

# 10.
def count_a_and_b(file_name):
    count_a, count_b = 0, 0
    with open(file_name, 'r') as file:
        for char in file.read():
            if char.lower() == 'a':
                count_a += 1
            elif char.lower() == 'b':
                count_b += 1
    return count_a, count_b

file_name = r'C:\Lessons\3 course\Python\text1.txt'

print("\nTask 1")
read_and_display(file_name)

print("\nTask 2")
read_random_line(file_name)

print("\nTask 3")
print(count_uppercase(file_name))

print("\nTask 4")
print(count_lines_not_starting_with_d(file_name))

print("\nTask 5")
print(count_words_ending_with_f(file_name))

print("\nTask 6")
all_count, none_count = count_all_and_none(file_name)
print(all_count, none_count)

print("\nTask 7")
freq = word_frequency(file_name)
for word, count in freq.items():
    print(f"{word}: {count}")

print("\nTask 8")
print(find_longest_word(file_name))

print("\nTask 9")
correct_content(file_name)

print("\nTask 10")
a_count, b_count = count_a_and_b(file_name)
print(f"a: {a_count}, b: {b_count}")
