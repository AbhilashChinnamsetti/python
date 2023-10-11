size=input("which pizza do u want(s/m/l)")
price=0
if size == 's' or size== 'S':
   price=100
elif size == 'm' or size=='M':
   price=200
else:
   price=300
add_pepperino=input("do you want pepperino(y/n)")
if add_pepperino=='y' or add_pepperino=='Y':
   if size=='s' or size=='S':
      price+=30
   else:
      price+=50
print(price)  
cheese=input("do you want xtra cheese?(y/n)")  
if cheese=='y':
   price+= 30
else:
   print("no cheese added") 
print(price)
