my_dict={"Denis":1985,"Olga":1964,"Petr":2000}
print(my_dict.get("Denis"))
print(my_dict.get("Balda"))
my_dict.update({"Angelina":1998,
                "Robert":1981})
del my_dict["Petr"]
print(my_dict)
a=my_dict.pop("Olga")
print(my_dict)
print(a)
my_set={1,2,3,4,1,2,3,4,"apple",'new',(5,6)}
print(my_set)
my_set.update({"banan",
                "Komod"})
print(my_set)
print(my_set.discard(1))