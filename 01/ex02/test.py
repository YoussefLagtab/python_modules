from vector import Vector

v1 = Vector([[1.0], [3.0]]).T()
v2 = Vector([[4.0], [6.0]]).T()

print("v1.values   =", v1.values)
print("v1.shape    =", v1.shape)
print("v2.values   =", v2.values)
print("v2.shape    =", v2.shape)
print("T(v1)       =", v1.T().values)
print("T(v1).shape =", v1.T().shape)
print("v1 + v2     =", (v1 + v2).values)
print("v2 + v1     =", (v2 + v1).values)
print("v1 - v2     =", (v1 - v2).values)
print("2 * v1      =", (2 * v1).values)
print("v2 / 2      =", (v2 / 2.0).values)
# print("2 / v2==", (2.0 / v2).values)
print("v1.v2       =", v1.dot(v2))
