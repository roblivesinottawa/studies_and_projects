healthiest = ['apples', 'lettuce', 'tomato', 'lean meat', 'banana', 'onion', 'avocado', 'burger']
junk = ['cookies', 'chips', 'burger']

healthy = []

for item in junk:
    if item in healthiest:
        healthy.append(item)

print(healthy)


# list comprehension
# junk = [item for item in junk if item in healthiest]
# print(junk)



# if int(len(healthiest)) > 5:
#     print('veggies are good')

# healthiest.append("pizza")
# print(healthiest)

# if "pizza" in healthiest:
#     print("I love it!")

# for food in healthiest:
#     print(healthiest)

# if "pizza" in healthiest:
#     healthiest.remove("pizza")

# print(healthiest)

# junk.append("pizza")
# print(junk)

# junk.remove("burger")
# print(junk)

