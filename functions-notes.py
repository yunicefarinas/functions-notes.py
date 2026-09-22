#function with no parameters and does not return a value
def printMessage():
    print("I am inside of a function and I don't return a value")
    print("All of my capabilities are performed inside the function only")

def returnMyMessage():
    return "I am a returning value"

#this function has two parameters and returns a value
def sumItUp(value1, value2):
    answer = value1 + value2
    return answer

#call a function by its name to activate it.
#printMessage()
#message = returnMyMessage()
#print(message)
var1 = 33
var2 = 34
myAnswer = sumItUp (var1, var2) #This calls the function with two arguments for the parameters for the func.
print(myAnswer)

#Function can have as many parameter as it wants. Each parameter is separated by a comma.

