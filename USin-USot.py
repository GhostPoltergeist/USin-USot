import time
#USin-USot

#>>: redirecting: USin
print("""
██╗   ██╗ ██████╗  ██╗  ███╗  ██╗          ██╗   ██╗ ██████╗   █████╗   ████████╗
██║   ██║██╔════╝  ██║  ████╗ ██║          ██║   ██║██╔════╝  ██╔══██╗  ╚══██╔══╝
██║   ██║╚█████╗   ██║  ██╔██╗██║  █████╗  ██║   ██║╚█████╗   ██║  ██║     ██║
██║   ██║ ╚═══██╗  ██║  ██║╚████║  ╚════╝  ██║   ██║ ╚═══██╗  ██║  ██║     ██║
╚██████╔╝██████╔╝  ██║  ██║ ╚███║          ╚██████╔╝██████╔╝  ╚█████╔╝     ██║
 ╚═════╝ ╚═════╝   ╚═╝  ╚═╝  ╚══╝           ╚═════╝ ╚═════╝    ╚════╝      ╚═╝
""")
n1 = str(input("Customer's ID name: "))
n2 = int(input("Customer's ID number: "))
print("Hello Our Dear Customer: " + n1)
print("Clarification Number has been Hold: " + str(n2))
time.sleep(3)
n3 = 40
n4 = int(input("[FOR CLARIFICATION]Room Number: "))
n5 = int(input("[Payment:$40]Your Cash: "))
n6 = (n5 - n3)
n7 = float(n6)
time.sleep(5)

#>>: redirecting: USot
#>>: PROCEED USot >>: Operators>>: Decrease>>: ConvertFloat>>: >>:Sleep >>: EXIT>>: FINISH

print("Your Change Is: " + str(n7))






