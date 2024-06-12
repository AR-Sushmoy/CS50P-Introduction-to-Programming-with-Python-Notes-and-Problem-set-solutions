def main():
    ask = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

    match ask:
        case "42":
            print("Yes")
        case "forty-two":
            print("Yes")
        case "forty two":
            print("Yes")
        case _:
            print("No")

main()
