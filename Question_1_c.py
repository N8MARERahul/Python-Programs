real=3
im=3
import cmath
import math
z=complex(real,im)
print("Imaginary Number = {} + {}i".format(real, im))
print("Modulus = ", (cmath.phase(z))*180)
print("Phase Angle = ", math.tan(im/real))