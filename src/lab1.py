def caesar_cipher(text, shift, language, direction):
    if language == "укр":
        alphabet_lower = "абвгґдеєжзийіїклмнопрстуфхцчшщьюя"
        alphabet_upper = alphabet_lower.upper()
    elif language == "англ":
        alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
        alphabet_upper = alphabet_lower.upper()
    else:
        print("Невідомий алфавіт.")
        return text

    result = ""
    for char in text:
        if char in alphabet_lower:
            alphabet = alphabet_lower
        elif char in alphabet_upper:
            alphabet = alphabet_upper
        else:
            result += char
            continue

        index = alphabet.index(char)
        if direction == "шифрування":
            new_index = (index + shift) % len(alphabet)
        elif direction == "дешифрування":
            new_index = (index - shift) % len(alphabet)
        else:
            print("Невідомий напрямок.")
            return text

        result += alphabet[new_index]

    return result


# --- Основна програма ---
direction = input("Введіть напрямок (шифрування/дешифрування): ").strip().lower()
language = input("Введіть мову алфавіту (укр/англ): ").strip().lower()
shift = int(input("Введіть крок зсуву (ціле число): "))
text = input("Введіть текст: ")

output = caesar_cipher(text, shift, language, direction)
print("Результат:", output)