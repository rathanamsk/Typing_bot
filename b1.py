n = int(input())
list1 = []
for i in range(n):
    get = input()
    list1.append(get)
print("AC x {}".format (list1.count("AC")))
print("WA x {}".format (list1.count("WA")))
print("TLE x {}".format (list1.count("TLE")))
print("RE x {}".format (list1.count("RE")))
