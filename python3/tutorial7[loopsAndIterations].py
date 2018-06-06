keys = [1,2,3,4,5]

# write  a for loop to iterate through to key and stop when find 3

for x in keys:
    if x==3:
        print("found")
        break
    print(x)
    # Break - stops the loop

# write a for loop to iterate through to key and skip the value 3

for x in keys:
    if x==3:
        continue
    print(x)
    # continue - skips the next condition

# loop within a loop

for x in keys:
    for letter in 'abc':
        print(x,letter)

# for loops for  certain iterations

for y in range(5):
    print('*')

#-----------------------------
#while loop
z= 5
while z > 0:
    print('z') 
    z -= 1


