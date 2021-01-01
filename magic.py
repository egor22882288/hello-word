import matplotlib.pyplot as plt

def func(x,k,b):
    return k*x+b
k= float(input("введите постоянный коофицент k="))
b = float(input("введите постоянный коофицент b="))
print("В каком диопазоне вывести таблицу")
x = float(input("от x=>>"))
xk = float(input("до x=>>")) 
print("В каком диопазоне вывести график")
x1 = float(input("от x=>>"))
x2 = float(input("до x=>>")) 



while x<=xk:
    y = func(k,x,b)
    print(x,"\t",y)
    x=x+1

y1=x1*k+b
y2=x2*k+b

plt.plot([x1,x2],[y1,y2])
plt.show()