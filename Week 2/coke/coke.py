def main():
    total_inserted = 0

    while total_inserted < 50:
        coin = int(input("Insert Coin: "))

        if coin == 25 or coin == 10 or coin == 5:
            total_inserted += coin
        else:
            print("Invalid Coin.")

        amount_due = 50 - total_inserted
        if amount_due > 0:
            print(f"Amount Due: {amount_due}")

    change = total_inserted - 50
    print(f"Change Owed: {change}")

if __name__ == "__main__":
    main()
