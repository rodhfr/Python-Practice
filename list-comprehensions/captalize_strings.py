fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

## Regular Logic:
# captalized_fruits = []
# for i in fruits:
#     current_fruit = i.capitalize()
#     captalized_fruits.append(current_fruit)
# print(captalized_fruits)

## List Comprehension:
captalized_fruits = [x.capitalize() for x in fruits]
print(captalized_fruits)


