'''
dictionary is a muteable and a unordered set of collection enclosed with the square bracket[]
its have the each item is the pair of key and value.
Ex. of dict is info of a student.
'''
info={'name':'ajay' ,'roll no.':'03','section':'C','address':'GLA university'}
print(info,type(info))


#read operation
print(info['roll no.'])

#write operation
info['roll no.']=100
info['father']='Brijpal singh'

#dict empty
dct={}
dct=dict()  #initialized a empty dict

# initialize the dictionarywith items
my_info={'name':'ajay singh','sec':['c','D'],'roll no.':'03'}
print('name:-', my_info['name'])