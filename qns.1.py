# Write a Python script to merge two Python dictionaries.

info={'name':'Ajay singh','sec':'C','address':'GLA university'}
print('the dict before the merging:-',info)
merging_info={'contact no.':'9897*****9','btech':'CS'}
d=info.update(merging_info)
print('the dict after the merging',info)