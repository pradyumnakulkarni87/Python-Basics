#converssion of list of tuples to dictionary
l= [('x',1),('x',2),('y',1),('y',3),("z",3)]
d= {}
for a,b in l:
    d.setdefault(a,[]).append(b)
print(d)

# l= [(10,20,30),(40,50,60),(70,80,90)]
# lt =[]
# for i in l:
#     #l[i]
#     l1= list(i)
#     l1.append(100)
#     #print(l1)
#     lt.append(tuple(l1))
# print(lt)