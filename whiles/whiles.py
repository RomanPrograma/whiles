begin = int(input("enter a begin  "))
end = int(input("enter an end  "))
for i in range(begin, end+1):
    if i %2 !=0:
        print(i)