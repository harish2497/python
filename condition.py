'''
decission making statements


if 
else
elif
nested if 
'''
  
'''
syntax:
if condition:
      statements
else:
      statements
      '''
# if True:
#      print(" I am if") 
# elif True:
#       print("I am elif")    
# else:
#         print("I am  else")

if False:
    print("outer if ")   
    if False:
        print("inner if")
    else:
        print("inner else")
        
else:       
       print("outer else") 

age=18
if age>18:
   print("you can vote") 
elif age==18:
    print("you can buddy")
else:
     print("wait")
