import cv2 as cv

from Associativity import associativity
import util

def build_spanning_tree(pairs, assocMat, tree):
	print("\nStep 4 (spanning)")
	old_n = assocMat.n

	'''
	## Only add camera once
	checked = [False] * old_n
	checked[0] = True

	## Build rest of tree
	new_n = 1
	assocMat.walk()

	CHANGE = old_n ## NOTE; Indices are still relative to old_n

	## NOTE: Number of nodes (cameras) may be reduced if no edge from/to camera exists
	print("{} cameras reduced to {} cameras by spanning tree.".format(old_n, new_n))
	'''
	
	return old_n

if __name__ == "__main__":
	print("in 4_spanning_tree.py")