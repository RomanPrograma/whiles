begin = int(input("enter a begin  "))
end = int(input("enter an end  "))
if begin > end:
    begin,end=end,begin
for i in range(end, begin-1, -1 ):
    print(i)