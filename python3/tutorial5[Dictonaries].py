"""
Example syntax for a dictonariy 

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

for key, value in student.items():
    print(key, value)


Methods()

getters() -
    Print(sudent.get('name'))
    - Will return valur in None if key don't exist

    Print(sudent.get('name','not found'))
    - will return not found if key name is not found

Add value seprately() -
    student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
    and 
    student['name'] = 'john'
    student['age'] =    '25'
    student [courses] = ['Maths','CompSci']

    these two will produce same result
 
update() -
    - student.update({'name'= 'jane', 'age' = '22'})
    - this will update key values together
    
Delete() -
    del student['age']
    - will delete the delete key 

pop() -
    x = student.pop('age')
    - will return the value of age in to var x

len() -
    len(students)
    - will print out length of the key 

print keys ()
    student.keys()
    - it will print out all the keys in student

print keys and values
    student.item()
    - will print keys and values

--------------------------------------------
Looping in dictonaries

 -For loop()
    for Key in student 
        print(Key)

        - will print keys in the student

    for Key in student.items
        print(Key, value)

        - will print keys and values

"""

car = {'name' : 'focus', 'year' : '2006' , 'condition' : 'good'}

print(car.keys())
