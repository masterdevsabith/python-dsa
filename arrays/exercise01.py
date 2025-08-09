expenses = [2200, 2350, 2600, 2130, 2190]
#         jan    feb   mar   apr   may


# 1. In Feb, how many dollars you spent extra compare to January?
print(expenses[1]-expenses[0])


# 2. Find out your total expense in first quarter (first three months) of the year.
print(expenses[1]+expenses[2]+expenses[3])


# 3. Find out if you spent exactly 2000 dollars in any month
for i in range(len(expenses)):
    if expenses[i] == 2000:
        print(i)

        # above method is incorrect, correct method below

print(2000 in expenses)


# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# expenses.insert(5, 1980)   more correct method below one
expenses.append(1980)
print(expenses)


# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

expenses[3] = expenses[3]-200
print(expenses)
