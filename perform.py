import vfdt
import numpy as np

tree = vfdt.loadtree()
x = np.array([[-1.23,-1.56,-1.75,-0.28,0.60,2.22,0.85,0.21,-0.20,0.89,1.08,4.20,2.89,7.75,4.59,3.15,5.12,3.32,1.20,0.24,-0.56]])
p = tree.predict(x)
print(p) 