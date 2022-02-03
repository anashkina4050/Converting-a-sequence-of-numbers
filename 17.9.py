# 2 15 44 6 71 28 57 33
sequence = input("Введите несколько чисел через пробел: ")
element = input("Введите любое число: ")

sequence_list = sequence.split(" ")
sequence_float_list = []

for i in sequence_list:
  try:
    sequence_float_list.append(float(i))
  except ValueError:
    print("Недопустимое значение", i)
    exit("Ошибка")

try:
  element_float = float(element)
except ValueError:
  print("Недопустимое значение", element)
  exit("Ошибка")

sequence_float_list.append(element_float)
sequence_float_list.sort(key=float)

def binary_search(array, part, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == part:
        return middle
    elif part < array[middle]:
        return binary_search(array, part, left, middle - 1)
    else:
        return binary_search(array, part, middle + 1, right)

element_index = binary_search(sequence_float_list, element_float, 0, len(sequence_float_list) - 1)

if element_index > 0 and sequence_float_list[element_index] > sequence_float_list[element_index - 1] and element_index < len(sequence_float_list) - 1 and sequence_float_list[element_index] <= sequence_float_list[element_index + 1]:
  print(sequence_float_list)
  print("Индекс:", element_index - 1)
else:
  print("Не найдено")