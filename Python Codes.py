import time
print('''
                        .----------------.
                       I__________________I
                       ||\ ________ /|  _ |
                       || |:      :| |o(_)|
                       || |;-"""-;| |o(_)|
                       || |________| | __ |
                       ||/__________\|[__]| 
                       "------------------"
''')
x=input("""
Welcome to the MICROWAVE 
To start please say YES or NO:""")
if x=="YES":
    y=input("which food would you like to cook:")
    x=int(input("how long do you want to microwave it for (in seconds):"))
    print("cooking for",x,"seconds")
    for i in range(x, 0, -1):
        print(i)
        time.sleep(1)
    print("your food has been cooked")
else:
    print("Stopping..")

