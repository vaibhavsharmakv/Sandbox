"""
Will read data from i.txt
will writee all the data to w.txt
"""


with open ('i.txt','r') as f:
    with open('w.txt','w') as wf:
        for x in f :
            wf.write(x)

        