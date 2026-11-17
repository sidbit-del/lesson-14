
def greet_customer():
    print("Hello")
    print("welcome to the premium lemonade stand")

greet_customer()

price_per_cup=float(input("what was the cost per cup"))

amount_of_cups=float(input("how many cups did you buy"))

def calculate_total(price_per_cup,amount_of_cups):
    total_cost=price_per_cup*amount_of_cups
    return total_cost

total_cost=calculate_total(price_per_cup,amount_of_cups)

rounded_total=round(total_cost,2)
print(total_cost)

money_paid=float(input("how much money did the customer pay"))

def calculate_change(total_cost,money_paid):
    change=money_paid-total_cost
    return change

change=calculate_change(total_cost,money_paid)

rounded_change=round(change,2)
print(change)

def message(amount_of_cups):
    if amount_of_cups>5:
        print("wow huge order thank you for coming please come again")
    else:
        print("thanks for coming please come again")

message(amount_of_cups)

print("=====lemonade stand recipt=====")
print("price per cup:",price_per_cup)
print("cups bought:",amount_of_cups)
print("total_cost:",total_cost)
print("amount paid:",money_paid)
print("change due:",change)
print(message(amount_of_cups))
print("=================")