""" ask age 5 times"""
#  age = int(input("Enter your age:"))
# while age >= 0:
#     age = int(input("Enter your age:"))
#
# for i in range(5):
#      age = int(input("Enter your age:"))
#      print(age)
#
#      #ctrl+shift+ UP or DOWN to move around copy/paste
#

""" using the len function on strings """

# s = "CP1404"

# for i in range(len(s)-1,-1, -1):
#     print(i, s[i)

# for i in range(-1, -(len(s)+1), -1):
#     print(s[i])
#
# subjects = []
# subject = input("subject: ")
# while subject != '':
#     subjects.append(subject)
#     subject = input("subject: ")
#     print(subjects)

# subjects = ['CP1404','CP1406','MA1000']
# for subject in subjects:
#     print(subject, end =" ")
#     if subject[:2] == "CP": # or if subject.startswith("CP1"):
#         print("Yeah!")
#     else:
#         print("Ohh..")


""" using find method """
# email = "bob.jones@jcu.edu.au"
#
# print(email[:email.find('@')])
# print(email[(email.find('@')+1):])
# print('.' in email)
# print('.b' in email)
# print('@' in email and '.' in email) # you can chain as many methods together

"""exceptions for input validation"""

valid_input = False
while not valid_input:
    try:
        age = int(input("Age: "))
        if age < 0:
            print("Invalid (must be greater than 0")
        else:
            valid_input = True
    except ValueError:  # or just  except:
        print("Invalid (not an integer)")
    print("Next year you will be", age + 1)
