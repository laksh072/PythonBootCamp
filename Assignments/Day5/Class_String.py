def cal_new(num1, num2, action):
    if action == "+":
        return "Adding", num1 + num2
    elif action == "-":
        return "Subtracting", num1 - num2
    else:
        a = "Not Supported","null"
        print("Not Supported" , "null")
        print("Not Supported" + "null")
        return "Not Supported" + "null"

inp1 = input("Enter First action")
inp2 = input("Enter Second action")

result = cal_new(10, 5, '+')
print(f"Result of + : {result}")
print(result[0])
print(result[1])

result = cal_new(10, 5, '*')
print(f"Result of * : {result}")
print(result[0])
print(result[1])

