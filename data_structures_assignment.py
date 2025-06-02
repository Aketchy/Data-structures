set1 = [3, 1, 7, 9]
set2 = [2, 4, 1, 9, 3]

sum_distinct = 0

for x in set1:
    if x not in set2:
        sum_distinct += x

for x in set2:
    if x not in set1:
        sum_distinct += x

print("Sum of distinct elements:", sum_distinct)





def dot_product(v1, v2):
    ps = 0
    for i in range(len(v1)):
        ps += v1[i] * v2[i]
    return ps

# Example vectors
v1 = [1, 2, -3]
v2 = [3, -2, 1]

result = dot_product(v1, v2)

if result == 0:
    print("Vectors are orthogonal")
else:
    print("Vectors are not orthogonal")

