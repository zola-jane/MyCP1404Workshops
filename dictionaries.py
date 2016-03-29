# phonebook = {"Bob": "123456","Jane": "755519"}
#
# # print phonebook
# # print(phonebook["Jane"])
# # phonebook["Jane"] = "47" + phonebook["Jane"]      #adding 47 to phone number
# # print(phonebook["Jane"])
#
# phonebook["T-mart"] = "123456"      # adding item into dictionary
#
# for name in phonebook:
#     print(name)       # prints out the key
#     phonebook[name]="47" + phonebook[name]
#     print(name, "-", phonebook[name])
#
# print("Bob" in phonebook)       # check if name is in phonebook
# print("47123456" in phonebook.values())
# print(phonebook.items())
# print(sorted(list(phonebook.items())))
#
# for name in sorted(list(phonebook.keys())):
#     print(name, "-", phonebook[name])
#
# #  changing T mart to Mr. T
# phonebook["Mr. T"] = phonebook["T-mart"]
# del phonebook["T-mart"]
# #  or using pop is easier
# phonebook["Mr. T"] = phonebook.pop("T-mart")
#

# """
# list of words and how often they appear
# """
# words = "bob is hi no is bob".split()
# word_count = {}
#
# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
# print(word_count)

"""
prompt th e user for a name and age  and add these to the dictionary
"""

ages_dict = {"Bill": 24, "Jane": 34, "Jack": 56}

name = input("Name:")
age = int(input("Age:"))

ages_dict[name] = age

for name, age in ages_dict.items():
    print("{:<10s} - {:>5d}".format(name, age))
