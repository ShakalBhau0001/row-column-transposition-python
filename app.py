import math


def get_column_order(key):
    sorted_key = sorted(list(key))
    order = []

    for char in key:
        order.append(sorted_key.index(char))
        sorted_key[sorted_key.index(char)] = None

    return order


def row_column_encrypt(text, key):
    text = text.replace(" ", "")
    cols = len(key)
    rows = math.ceil(len(text) / cols)

    # Padding text
    text += "X" * (rows * cols - len(text))

    matrix = []
    index = 0

    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(text[index])
            index += 1
        matrix.append(row)

    order = get_column_order(key)
    cipher = ""

    for num in sorted(range(cols), key=lambda x: order[x]):
        for r in range(rows):
            cipher += matrix[r][num]

    return cipher


def row_column_decrypt(cipher, key):
    cols = len(key)
    rows = math.ceil(len(cipher) / cols)

    order = get_column_order(key)
    matrix = [["" for _ in range(cols)] for _ in range(rows)]

    index = 0
    for num in sorted(range(cols), key=lambda x: order[x]):
        for r in range(rows):
            matrix[r][num] = cipher[index]
            index += 1

    return "".join("".join(row) for row in matrix)


print("\n--- Row-Column Transposition Cipher ---\n")

choice = input("Encrypt or Decrypt (E/D): ").upper()
message = input("Enter message: ")
key = input("Enter keyword: ")

if choice == "E":
    print("Encrypted message:", row_column_encrypt(message, key))
elif choice == "D":
    print("Decrypted message:", row_column_decrypt(message, key))
else:
    print("Invalid choice!")
