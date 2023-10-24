def can_construct(s1, s2):
    s1_char_count = {}
    s2_char_count = {}
    
    # Подсчитываем количество появлений каждой буквы в строке s1
    for char in s1:
        if char in s1_char_count:
            s1_char_count[char] += 1
        else:
            s1_char_count[char] = 1
    
    # Подсчитываем количество появлений каждой буквы в строке s2
    for char in s2:
        if char in s2_char_count:
            s2_char_count[char] += 1
        else:
            s2_char_count[char] = 1
    
    # Проверяем, что каждая буква из s1 может быть получена из s2
    for char in s1_char_count:
        if char not in s2_char_count or s1_char_count[char] > s2_char_count[char]:
            return False
    
    # Если все проверки пройдены, то возвращаем True
    return True

# Пример использования
s1 = "aabcpo"
s2 = "aabcjoipj"
print(can_construct(s1, s2))
