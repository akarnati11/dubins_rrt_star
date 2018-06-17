from utils import getRandomStates, MAX_VAL, MIN_VAL
from rrt_star import getPath
import matplotlib.pyplot as plt
import numpy as np

WIN_MIN = MIN_VAL-2
WIN_MAX = MAX_VAL+2

def run():
	ax = plt.axes()
	arr_mag = 1

	start, goal = getRandomStates(2)

	treeList, path = getPath(start, goal)
	treeList = np.array(list(map(lambda a: a.state, treeList))).reshape(len(treeList), 3)
	# treeList = treeList.reshape((len(treeList), 3))
	path = np.array(path).reshape(len(path),3)

	ax.quiver(treeList[:,0], treeList[:,1], np.cos(treeList[:,2]) * arr_mag, np.sin(treeList[:,2]) * arr_mag,
			headwidth=0.5, headlength=0.75)
	ax.quiver(start[0], start[1], np.cos(start[2]) * arr_mag, np.sin(start[2]) * arr_mag, headwidth=0.5,
			headlength=0.75, color="b")
	ax.quiver(goal[0], goal[1], np.cos(goal[2]) * arr_mag, np.sin(goal[2]) * arr_mag, headwidth=0.5, headlength=0.75,
			color="r")


	plt.xlim((WIN_MIN, WIN_MAX))
	plt.ylim((WIN_MIN, WIN_MAX))
	plt.show()

	plt.close()
	ax = plt.axes()

	ax.quiver(path[:, 0], path[:, 1], np.cos(path[:, 2]) * arr_mag, np.sin(path[:, 2]) * arr_mag,
			headwidth=0.5, headlength=0.75)
	ax.quiver(start[0], start[1], np.cos(start[2]) * arr_mag, np.sin(start[2]) * arr_mag, headwidth=0.5,
			headlength=0.75, color="b")
	ax.quiver(goal[0], goal[1], np.cos(goal[2]) * arr_mag, np.sin(goal[2]) * arr_mag, headwidth=0.5, headlength=0.75,
			color="r")

	plt.xlim((MIN_VAL, MAX_VAL))
	plt.ylim((MIN_VAL, MAX_VAL))

	plt.show()
	# for i in range(len(control)):
	# 	curState = getNextState(curState, control[i])
	# 	if i % 10 == 0:
	# 		arr_mag = control[i,1]
	# 		ax.arrow(curState[0], curState[1], np.cos(curState[2])*arr_mag, np.sin(curState[2])*arr_mag, head_width=0.5, head_length=0.75)
	# plt.show()


if __name__ == "__main__":
	run()
