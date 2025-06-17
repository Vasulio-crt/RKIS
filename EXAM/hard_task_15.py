def caesar_cipher(text, shift, language="ru"):
    result = str()
    language = language.lower()
    match language:
        case "ru":
            for c in text:
                if c.isalpha():
                    start = ord('а') if c.islower() else ord('А')
                    new_char_code = ((ord(c) - start + shift) % 33) + start
                    result += chr(new_char_code)
                else:
                    result += c
            return result
        case "en":
            for c in text:
                if c.isalpha():
                    start = ord('a') if c.islower() else ord('A')
                    new_char_code = ((ord(c) - start + shift) % 26) + start
                    result += chr(new_char_code)
                else:
                    result += c
            return result

text = input("Введите текст: ")
shift = int(input("Введите сдвиг: "))
print(caesar_cipher(text, shift))