# def sum_all_num(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total
#
#
# print(sum_all_num(1, 2, 3, 4, 5, 6))

# def fav_colors(**kwargs):
#     for person, color in kwargs.items():
#         print(f"{person}'s favorite color is {color}")
#
#
# fav_colors(trevor="blue", jason="green", derek="red")

# set_operations(operation="union", set1={1,2,3,4}, set2={3,4,5,6}, message="The union is"}
#                The union is {1, 2, 3, 4, 5, 6}
def set_operations(**kwargs):
    op_results = {"union": kwargs.get("set1") | kwargs.get("set2"),
                  "intersection": kwargs.get("set1") & kwargs.get("set2")}
    return kwargs.get("message", "The result is ") + str(op_results.get(kwargs.get("operation")))


sets = dict(set1={1, 2, 3, 4}, set2={3, 4, 5, 6}, operation="union", message="The union is ")
sets1 = dict(set1={1, 2, 3, 4}, set2={3, 4, 5, 6}, operation="intersection")
print(set_operations(**sets))
print(set_operations(**sets1))

