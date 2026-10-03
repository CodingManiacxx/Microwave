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
        z=print(f''' .----------------.
                       I__________________I
                       ||\ ________ /|  _ |
                       || |:      :| |o(_)|
                       || |;-{i}-;| |o(_)|
                       || |________| | __ |
                       ||/__________\|[__]| 
                       "------------------" 
                       ''')
        time.sleep(1)

    print(f''' .----------------.
                       I________________________________________I
                       ||          \ ________ /            |  _ |
                       ||           |:      :|             |o(_)|
                       || |;-YOUR FOOD HAS BEEN COOKED-;| |o(_)|
                       ||           |________|             | __ |
                       ||          /__________\            |[__]| 
                       "----------------------------------------" 
                       ''')
else:
    print("Stopping..")


