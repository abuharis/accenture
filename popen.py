from subprocess import Popen, PIPE


#execute command

process = Popen(['ping','8.8.8.8','-n','2'],shell=True, stdout=PIPE,stderr=PIPE)
#read output

print (process.stdout.read())

#wait for termination

rc = process.wait()
print ("Exit code: ".format.rc())
