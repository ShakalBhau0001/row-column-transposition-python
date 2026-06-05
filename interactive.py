from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
import math

console = Console()


def get_column_order(key):
    sorted_key = sorted(list(key))
    order = []

    for char in key:
        idx = sorted_key.index(char)
        order.append(idx)
        sorted_key[idx] = None

    return order


def row_column_encrypt(text, key):
    text = text.replace(" ", "")
    cols = len(key)
    rows = math.ceil(len(text) / cols)
    text += "X" * (rows * cols - len(text))
    matrix = []
    index = 0

    for _ in range(rows):
        row = []
        for _ in range(cols):
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


def main():
    console.clear()
    console.print(
        Panel.fit(
            "[bold cyan]📊 Row-Column Transposition Cipher[/bold cyan]",
            border_style="cyan",
        )
    )

    choice = Prompt.ask(
        "\n[bold yellow]Choose mode[/bold yellow]", choices=["E", "D"], default="E"
    )

    message = Prompt.ask("[bold yellow]Enter message[/bold yellow]")
    key = Prompt.ask("[bold yellow]Enter keyword[/bold yellow]")

    if not key.isalpha():
        console.print("[bold red]❌ Key must contain only letters![/bold red]")
        return

    if choice == "E":
        result = row_column_encrypt(message, key)
        title = "Encrypted Message"
        style = "bold green"

    else:
        result = row_column_decrypt(message, key)
        title = "Decrypted Message"
        style = "bold magenta"

    console.print(
        Panel(f"[{style}]{result}[/{style}]", title=f"✨ {title}", border_style="blue")
    )


if __name__ == "__main__":
    main()
