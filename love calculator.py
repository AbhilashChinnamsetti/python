name1=input("enter the name of yours :")
name2=input("enter the name of your partner :")
final=(name1 + name2)
l=final.count("l")
o=final.count("o")
v=final.count("v")
e=final.count("e")
t=final.count("t")
r=final.count("r")
u=final.count("u")
e=final.count("e")
love=l+o+v+e
true=t+r+u+e
love_percentage=int(love)+int(true)
if  love_percentage<10 or love_percentage>90:
    print("top rated")
elif love_percentage<50 or love_percentage<40:
    print("good one")    
else:
    print(love_percentage)
print(love_percentage)




