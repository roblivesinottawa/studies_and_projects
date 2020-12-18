# Bob, Ann, Jane, and Rick want to order pizza - each will eat 4 slices.
# the pizza place nearby has only 6-slice pizzas
# what is the minimum number of pizzas needed

total_slices = 4 * 4
number_pizzas = (total_slices + 5) // 6
slices_left = number_pizzas * 6 - total_slices

print(f"number of pizzas needed is {number_pizzas}, there'll be {slices_left} remaining slices.")