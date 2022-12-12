# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


def rle_encode(data_str: str):
    encoding = ''
    prev_char = ''
    count = 1
    if not data_str: return ''

    for char in data_str:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            prev_char = char
            count = 1
        else:
            count += 1
    else:
        prev_char = char
        encoding += str(count) + prev_char
    return encoding

def rle_decode(data_str: str):
    decode = ''
    count = ''
    for char in data_str:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

my_string = input("Введите строку: ")
encode_str = rle_encode(my_string)
decode_str = rle_decode(encode_str)
print(f"Вы ввели строку: {my_string}")
print(f"После кодировки она выглядит так: {encode_str}")
print(f"После раскодировки так: {decode_str}, правильно?)")
