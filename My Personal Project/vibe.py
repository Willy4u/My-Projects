import numpy as np
S = np.array([int(x) for x in input().split()])
A = np.array([int(x) for x in input().split()])
B = np.array([int(x) for x in input().split()])


mean_S = S.mean()
mean_A = A.mean()
mean_B = B.mean()

g1 = 2 * mean_S * (1-mean_S)

g2 = 2 * mean_A * (1-mean_A)

g3 = 2 * mean_B * (1-mean_B)

H_S = len(S)
H_A = len(A)
H_B = len(B)

infog = g1 - (H_A/H_S) * g2 - (H_B/H_S) * g3

print(round(infog , 5))
