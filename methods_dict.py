# clear()
# it is used to remove all the elements of the dictionary

info={'name':'Ajay singh','sec':'C','address':'GLA university'}
print(info,type(info))
info.clear()
print(info,type(info))


# copy()
# copy is uesd to return shallow copy of a dictionary

info={'name':'Ajay singh','sec':'C','address':'GLA university'}
print('the info of the student is ',info)
d = info.copy()
print('d is printed here after the use of the copy method', d)


# keys and items
#it is uesd to find the keys and items presents in the dictonary

info={'name':'Ajay singh','sec':'C','address':'GLA university'}
print(info)
d=info.keys()
v=info.items()
print(d,v)

# pop  &  popitem
# delete or remove the elements (keys and items also)

info={'name':'Ajay singh','sec':'C','address':'GLA university'}
print('The info of the student is :-',info)
d=info.pop('address')
print('The use of the pop methods(After):-',d)

# pop items
# its is also used to remove the last elements automatically

info={'name':'Ajay singh','sec':'C','address':'GLA university'}
print('The info of the student is :-',info)
d=info.popitem()
print('The use of the pop item method:-',d)
print('after use of the pop item',info)

# update
# it is used to add the elements in the dictionary

info={'name':'Ajay singh','sec':'C','address':'GLA university'}
print('The info of the student is(before updating) :-',info)
update_info=('phone no.':'9897200299','father,s name:-':'mr.Brijpal singh')
d=info.update(update_info)
print('after the updating the student info:-',d)

# from keys
# creates the dictionary from the given sequence.

info={'name':'Ajay singh','sec':'C','address':'GLA university'}
print('The old informations of the student:-',info)
l={}.fromkeys(info,'ok tested')
print('the updated data of the student is:-',l)

# get
# return the value of the key

info={'name':'Ajay singh','sec':'C','address':'GLA university'}
print('The old informations of the student:-',info)
d=info['name']
d=info.get('name','NA')
print(d)

