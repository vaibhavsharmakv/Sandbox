""" Strings
 \""" - we use three \""" when adding a multiple line of strings

--------------------------------------------
- Function in Strings

- length of the string -> 
    len(String)

- Ouput specific character at index i ->
    -  print(String[i])
    -  print(String[i:j])

- Methods()
    - var.lower() -> turns string into lower case
    - var.count('x') -> search for number of x in the string
    - var.find('x') -> find the index for x in the string
    - var.replace('x','y') -> replaces x with y in the string 

- F string
    - syntax {
        f'My name is {name}, my age next year is {age+1}, my anniversary is {anniversary:%A, %B %d, %Y}.'
    }

- dir(string)
    - will show all the atributes and methods available

- help for strings 
    - help(str) - show all the methods available on string
    - help(str.lower) - tell us what .lower method do specifically         

"""

x = "hello"
z = x.count('l')



