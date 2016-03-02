# QR CGS Test
import qr_cgs as hw
import numpy as np

M = np.random.rand(3,3)
print("==== M =====")
print(M)
print("")
(Q,R) = hw.qr_cgs(M)
print("===== Q =====")
print(Q)
print("")
print("===== R =====")
print (R)
print("")
print("===== QR = M =====")
print(Q*R == M)
print("")
print("===== M - QR =====")
print(M - Q*R)
#print(Q*Q.H)
