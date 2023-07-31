# 简单的计算器脚本
num1 = float(input("请输入第一个数字: "))
operator = input("请输入运算符 (+, -, *, /): ")
num2 = float(input("请输入第二个数字: "))

result = 0

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("无效的运算符")

print("计算结果:", result)
