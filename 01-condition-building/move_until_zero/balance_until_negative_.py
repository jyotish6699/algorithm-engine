"""Problem Statement — Monthly Expense Tracker

A student starts the month with an initial bank balance N.

Daily expenses are stored in an array.

Process expenses one-by-one in order.

After each expense:

subtract the expense from balance
print the day number and remaining balance

Stop processing immediately if the balance becomes negative.

Example
balance = 1000
expenses = [200, 150, 500, 300]
Expected Output
Day 1 -> Balance: 800
Day 2 -> Balance: 650
Day 3 -> Balance: 150
Day 4 -> Balance: -150"""

def expense_manage(bal, exp:list):
    for i in range(len(exp)):
        if bal < 0:
            break

        bal = bal - exp[i]
        print(f"Day {i+1} -> Balance: {bal}")


expense_manage(1000, [200, 150, 500, 300])


# time complexity ------
# O(n) -> because worst case all list element will visit
# space complexity ------
# O(1) -> because no extra variable is used only i is uses for full iteration.