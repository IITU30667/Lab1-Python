print("task 1")
try:
    input_str = input()
    result_tuple = tuple(input_str)
    print(result_tuple)
except Exception as e:
    print(e)

print("\ntask 2")
try:
    input_tuple = eval(input())
    result_str = ''.join(input_tuple)
    print(result_str)
except Exception as e:
    print(e)

print("\ntask 3")
try:
    tuple_A = eval(input())
    tuple_B = eval(input())

    half_length_A = len(tuple_A) // 2
    half_length_B = len(tuple_B) - len(tuple_B) // 2

    result_tuple = tuple_A[:half_length_A] + tuple_B[half_length_B:]
    print(result_tuple)
except Exception as e:
    print(e)

print("\ntask 4")
try:
    input_tuple = eval(input())
    unique_elements = set(input_tuple)

    occurrence_list = []
    for element in unique_elements:
        count = input_tuple.count(element)
        occurrence_list.append((element, count))

    occurrence_tuple = tuple(occurrence_list)
    print(occurrence_tuple)
except Exception as e:
    print(e)

print("\ntask 5")
try:
    input_tuple = eval(input())

    int_list = []
    float_list = []
    str_list = []

    for item in input_tuple:
        if isinstance(item, int):
            int_list.append(item)
        elif isinstance(item, float):
            float_list.append(item)
        elif isinstance(item, str):
            str_list.append(item)

    int_tuple = tuple(int_list)
    float_tuple = tuple(float_list)
    str_tuple = tuple(str_list)

    print(int_tuple)
    print(float_tuple)
    print(str_tuple)
except Exception as e:
    print(e)

