#!/c/Python27/python

#Guess a number

import random
secret = random.randint(1,10)

print ("secret is : {}".format(secret))

while True:
    answer = raw_input("Guess a number between 1 and 10:")

    if int(answer) > secret:
        print ("Too High:(")
    elif int(answer) < secret:
        print ("Too Small")
    elif int(answer) == secret:
        print "You Win"

        break

