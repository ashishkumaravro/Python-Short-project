while True:
    try:
        monthly_income = int(input("Enter your monthly income to know your yearly income tax:  "))
        income = monthly_income * 12

        if income <= 300000:
            print(f"You don't have to pay any tk for your {income} tk yearly income!")
            print("Goverment is so kind for the poor as you 😃")
        elif income <= 400000:
            tax = income * 5 / 100
            print(f"You have to paly {tax} tk for your {income} tk yearly income!")
        elif income <= 700000:
            tax = income * 10 / 100
            print(f"You have to paly {tax} tk for your {income} tk yearly income!")
        elif income <= 1100000:
            tax = income * 15 / 100
            print(f"You have to paly {tax} tk for your {income} tk yearly income!")
        elif income <= 1600000:
            tax = income * 20 / 100
            print(f"You have to paly {tax} tk for your {income} tk yearly income!")


        else:
            tax = income * 25 / 100
            print(f"You have to pay {tax} tk for your {income} tk yearly income!")
        break

    except ValueError:
        print("Please Only enter the int value.")
