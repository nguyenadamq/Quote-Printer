import random
f = open("quotes.txt")
lines = f.readlines()
count = 1
quotes = []
print("Appending quotes.")
for line in lines:
    quotes.append(line)
###Print out quotes from file
#for line in lines:
    #print("Quote " + str(count) + ": " + line)
    #count += 1
    #input("Press Enter to continue." + "\n")
    
#Random quote
print("Random quote: " + random.choice(quotes))

user = input("Do you want a random quote? (Y) or (N)")

if user.lower() == "y":
    while(user.lower() != "n"):
        print("\n" + random.choice(quotes))
        user = input("Do you want a random quote? (Y) or (N)")

print(user)
#Choose a quote
input("Press Enter to exit.")