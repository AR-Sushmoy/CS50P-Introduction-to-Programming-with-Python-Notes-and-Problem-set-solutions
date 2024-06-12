def main():
    fine = 0;
    greet = input("Greeting: ").lower().strip()

    if greet == "hello":
        print(F"${fine}")
    elif greet[4] == "o":
        print(F"${fine}")
    elif greet[0] == "h":
        fine += 20
        print(F"${fine}")
    elif greet[0] != "h":
        fine += 100
        print(F"${fine}")
    
main()