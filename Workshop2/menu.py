name = input("Enter name: ")

print("(H)ello \n(G)oodbye \n(Q)uit")

choice = input()
while choice != 'Q':
    if choice == 'H':
        print("Hello", name)
    elif choice == 'G':
        print("Goodbye", name)
    else:
        print("Invalid choice")
    print("(H)ello \n(G)oodbye \n(Q)uit")
    choice = input()
print("Finished")