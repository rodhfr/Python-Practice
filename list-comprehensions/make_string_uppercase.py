fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

## conventional logic: 
# uppercased_fruits = []
# for i in fruits:
#     current_fruit = i.upper()
#     uppercased_fruits.append(current_fruit)
# print(uppercased_fruits)

## list comprehension:
uppercased_fruits = [x.upper() for x in fruits]
print(uppercased_fruits)
