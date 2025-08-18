v1= 5
while v1>1:
    print(v1)
    v1=v1-1
print ("1st While Loop Iteration Completed")

#Using break statement
#It will break the current loop iteration
v2 = 10
while v2>1:
    if v2==3:
        break
    print(v2)
    v2=v2-1
print ("2nd While Loop Iteration Completed")

#Using continue statement
#It will skip the current iteration and will move to continue the next iteration
v3=10
while v3>1:
    if v3==5:
        v3=v3-1
        continue
    print(v3)
    v3 = v3 - 1
print("3rd While Loop Iteration Completed")