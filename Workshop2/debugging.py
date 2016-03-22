score = int(input("Enter score: "))
while score < 0 or score > 100:
    print("Invalid score")
    score = int(input("Enter score: "))
if score > 90 :
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")
