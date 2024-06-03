from operator import itemgetter

a_list = [['xiangbo',13,'monkey'],['enze',12,'dog'],['yuan',12,'cat']]

sorted_a_list = sorted(a_list, key=itemgetter(1,0))

print(sorted_a_list)
