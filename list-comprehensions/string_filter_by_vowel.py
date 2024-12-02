fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

## Regular logic: (easy) [slowest]
# vowels = 'aeiou'
# more_two_vowels = []
# count = 0
# for fruit in fruits:
#     for j in fruit:
#         if j in vowels:
#             count += 1
#     if (count > 1):
#         more_two_vowels.append(fruit)
#     count = 0
# print(more_two_vowels)


## Regular way function + list comprehension (medium) [less slower]
# def has_two_vowels(fruit):
#     string = fruit 
#     count = 0
#     vowels = 'aeiou'
#     for i in string:
#         if i in vowels:
#             count += 1
#     if count > 1:
#         return string
#     else: 
#         return ''
#         
# vowels = 'aeiou'
# more_two_vowels = [has_two_vowels(fruit) for fruit in fruits]
# print(more_two_vowels)


## List Comprehension Proper Way (HARD) [faster]
more_two_vowels = [fruit for fruit in fruits if (sum(1 for char in fruit if char in 'aeiou') > 2)]
print(more_two_vowels)








