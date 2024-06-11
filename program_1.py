while True:
  print("1.Area of Circle")               
  print("2.Area of Rectangle")
  print("3.Area of Square")
  print("4.Area of Triangle")
  choice=int(input("Enter Your choice"))
  if choice==1:
    radius=int(input("Enter radius of Circle:"))
    print("Area of Circle",3.14*radius*radius)
  elif choice==2: 
    length=int(input("Enter Length of Rectangle:"))
    breadth=int(input("Enter Breadth of Rectangle:"))
    print("Area of Rectangle:",length*breadth)
  elif choice==3:
    side=int(input("Enter side of Square:"))
    print("Area:",side*side) 
  elif choice==4: 
    base=int(input("Input the base :"))
    height=int(input("Input the height:"))
    print("Area of Triangle:",height*base)
  elif choice==5:
    break
  else:
    print("wrong choice")
