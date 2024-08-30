print("TenrecScript shell")
print("created by Andrew Ekenes")
print()
while True:
    code = input()
    if "log" in code:
        print(">"+code.replace("log", ""))
    else:
        print("Syntax error!")