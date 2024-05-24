"""
Practicing various numpy functions! Wahoo!
"""

import numpy as np

uniform_list = np.random.Generator.uniform(0.0,1.0,10)
print(uniform_list)
a = np.sum(uniform_list)
print(a)