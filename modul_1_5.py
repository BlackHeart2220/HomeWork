immutable_var=tuple([1,2,'a','b'])
immutable_var2=1,2,'a','b'
immutable_var3=(1,2,'a','b')
immutable_list=([1,2,],'a', 'b', 'Modified')
print(immutable_list)
immutable_list[0][0] = 2
print(immutable_var2)
print(immutable_var3)
print(immutable_list)