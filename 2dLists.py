#!usr/bin/python
#Set size of number block (for this program we'll do multiplication tables)
w = 10
h = 10

#THREE WAYS TO MAKE A MULTI DIMENSIONAL LIST
print "---THREE WAYS TO MAKE A MULTI DIMENSIONAL LIST--"
print "--Method One--"

#Create an outer list
twoDListOne = []
for i in range(w):
    innerList = []  #Create an empty inner list
    for j in range(h):
        innerList.append(i*j) #Populate the inner list
    #Add the populated inner list to the outer list
    twoDListOne.append(innerList)
#Now we have a list of lists
#Would work great if we don't know the size, like in a while loop
#This way runs the fewest number of loops

for i in range(w):  #Print the contents of each list
    for j in range(h):  #Print with formatting
        if twoDListOne[i][j] < 10: print ' ' + str(twoDListOne[i][j]),
        else: print twoDListOne[i][j],
    print  #Prints a newline



print "--Method Two--"
#Two for..in inline loops. Initialize the outer list with inner lists
#The 0 is what will be added to each space
twoDListTwo = [[0 for i in range(w)] for j in range(h)]

#Populate the list of lists
for i in range(w):
    for j in range(h):
        twoDListTwo[i][j] = (i*j)

for i in range(w):  #Print the contents of each list
    for j in range(h):  #Print with formatting
        if twoDListTwo[i][j] < 10: print ' ' + str(twoDListTwo[i][j]),
        else: print twoDListTwo[i][j],
    print  #Prints a newline



print "--Method Three--"
#Multiple execution + for..in. Slightly less verbose.
twoDListThree = [[0]*w for i in range(h)]

#Populate the two dimensional lists
for i in range(1,w):
	for j in range(1,h):
		twoDListThree[i][j] = i*j

for i in range(w):  #Print the contents of each list
    for j in range(h):  #Print with formatting
        if twoDListThree[i][j] < 10: print ' ' + str(twoDListThree[i][j]),
        else: print twoDListThree[i][j],
    print  #Prints a newline
