def make_change(total_charge, payment):
    #find the difference
    difference = round(payment - total_charge, 2)
    print(difference)
    #split the difference into bills and coins
    # 1, 5, 10, 20, 50
    difference_as_string = str(difference)
    #split string into parts
    parts = difference_as_string.split('.')
    #define the bills and coins based on the parts
    bills = parts[0]
    #note to make the coins go to 2 decimal points
    coins = parts[1]
    return count_bills(bills), count_coins(coins)

    


def count_bills(payment_in_bills):
    payment_in_bills = int(payment_in_bills)
    hundreds = payment_in_bills // 100
    payment_in_bills %= 100
    # ^ same as "payment_in_bills = payment_in_bills % 100"
    fifties = payment_in_bills // 50 
    payment_in_bills %= 50
    twenties = payment_in_bills // 20
    payment_in_bills %= 20
    tens = payment_in_bills // 10
    payment_in_bills %= 10
    fives = payment_in_bills // 5
    payment_in_bills %= 5
    singles = payment_in_bills // 1
    payment_in_bills %= 1
    return(singles, fives, tens, twenties, fifties, hundreds)
    
    


def count_coins(payment_in_coins):
    payment_in_coins = int(payment_in_coins)
    quarters = payment_in_coins // 25
    payment_in_coins %= 25
    dimes = payment_in_coins // 10
    payment_in_coins %= 10
    nickels = payment_in_coins // 5
    payment_in_coins %= 5
    pennies = payment_in_coins // 1
    payment_in_coins %= 1
    return (pennies, nickels, dimes, quarters)


print(make_change(148.49, 200))

def value_of_change(change):
    total = sum(count_bills(change[0])) + sum(count_coins([1]))
    return round(total, 2)


change = (
    (1, 0, 0, 0, 1, 0), 
    (1, 0, 0, 2)
    )

result = value_of_change(change)
print(result)