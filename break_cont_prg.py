#Break and continue
#break
print("Using break")
for i in range(0,10):
    if(i==5):
        break
    print(i)
print("out of loop")
print(i)
print('')
print("Using continue")
#continue
for i in range(0,10):
    if(i==5):
        continue
    print(i)
