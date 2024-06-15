from colorama import init, Fore 

num = 0  
while num <= 100:
    print(Fore.YELLOW + f"{num}")
    num += 2 

while num <= 200: 
    print(Fore.RED + f"{num}")
    num += 2
else:
    print("num mayor a 200")


while num <= 300:
    print(num)
    num+= 2
    if num == 250: 
        print(Fore.MAGENTA + "Se detiene todo")
        break
print(num)

num = 0
#for loop 
for num in range(5,21):
    print(Fore.GREEN + f"{num}")
    num+= 2 

