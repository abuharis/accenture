#!/c/Python27/python

#print name from keyboard

print "What is your name?"
input = raw_input()
print ("Hello %s" %input)

#Choose action from dictionary

dic = {'action 2':'Practice with SDx','action 3':'sleep','action 1':'read book'}
action = (raw_input("Please choose your action: {}".format(dic)))
print ("I'll {} later".format(dic[action]))



