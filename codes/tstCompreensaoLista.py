# [expression for element in list if conditional]

# for element in list:
#     if conditional:
#         expression

var = []
var_1 = var[:]
var_2 = var[:]
var_3 = var[:]
var_4 = var[:]

###

for i in range(5):
    var.append("a")

print(var)

###

var_1 = ["b" for i in range(10)]

print(var_1)

####

var_2 = [True for i in range(5) if var[0] == "a"]

print(var_2)

###

var_3 = [[2 ** i for i in range(10)] for i in range(4)]

print(var_3)

###

var_4 = [[i + 1 for i in range(10) if i % 2 != 0] for i in range(len(var_3))]

print(var_4)

###
