# flow of eexecution with function
#def sum(x,y):
 #   s=x+y
  #  return s
#num1=int(input('enter number='))    #add two number
#num2=int(input('enter another='))
#print(sum(num1,num2))


#local and global variable

p=20                           #global variable
def display():
    a=10                       #local variable
    print('local variable=',a)
    print('global variable=',p)
display()
print('global variable=',p)
