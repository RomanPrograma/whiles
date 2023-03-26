begin = int(input("enter a begin  "))
end = int(input("enter an end  "))
if begin > end:
   end,begin=begin,end
for i in range(begin, end+1,  ):
    print(i)