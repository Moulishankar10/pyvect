# SUBMODULE FOR AREA FUNCTIONS

# TO USE THE FUNCTIONS IN THIS SUBMODULES:
# >>> vectoralg.area

# IMPORTING REQUIRED MODULES
import numpy as np

# FUNCTIONS

# triangle_adj() - Returns the area of a triangle where the two adjacent sides of the triangle are given.
# Syntax: vectoralg.area.triangle_adj(vector_1,vector_2)
# vector_1 - First adjacent side , vector_2 - Second adjacent side
# Return type: float
def triangle_adj(x,y):
    return abs(0.5*np.linalg.norm(np.cross(x,y)))

# triangle_pos() - Returns the area of the triangle based on the given three positional vectors.
# Syntax: vectoralg.area.triangle_pos(p1,p2,p3)
# p1,p2,p3 - positional vectors of the triangle.
# Return type: float
def triangle_pos(a,b,c):
    return abs(0.5*np.linalg.norm(np.cross(a,b)+np.cross(b,c)+np.cross(c,a)))

# quad() - Returns the area of a quadrilateral based on the diagonal vectors.
# Syntax: vectoalg.area.quad(diagonal_1,diagonal_2)
# diagonal_1 - Primary diagonal of the quadrilateral, diagonal_2 - Secondary diagonal of the quadrilateral.
# Return type: float
def quad(d1,d2):
    return abs(0.5*np.linalg.norm(np.cross(d1,d2)))