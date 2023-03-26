begin = int(input('enter begin  '))
end = int(input('enter end  '))
counter = 0
for i in range(begin, end+1):
    print(i)
print('\n')
for i in range(end, begin-1, -1):
    print(i)
print('\n')
for i in range(begin, end+1):
    if i %7 ==0:
        print(i)
print('\n')
for i in range(begin, end+1):
    if i %5 ==0:
        counter += 1
print(counter)
