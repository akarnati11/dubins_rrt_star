from utils import getRandomStates, getNextState, ACTIONS
import numpy as np

MAX_VERTS = 1000
NEIGHBORHOOD = 0.5
GOAL_THRESH = 0.5


class Tree:
	def __init__(self, p, s):
		self.parent = p
		self.state = s
		if p is not None:
			self.cost = p.cost + dist(p.state, self.state)
		else:
			self.cost = 0


def dist(x1, x2):
	# Better dist function?
	if x1.ndim == 1:
		return np.linalg.norm(x1-x2)
	return np.linalg.norm(x1-x2, axis=1)


def dist1(x1, x2):
	return np.linalg.norm(x1.flatten()[:2] - x2.flatten()[:2])


# For a list of trees compared to a state
def getNearest(tL, x, vol=None, dist=dist):
	tStates = np.array(list(map(lambda a: a.state, tL))).reshape(len(tL), 3)
	X = np.full_like(tStates, x)
	if vol is None:
		return tL[np.argmin(dist(tStates, X))]
	else:
		tLArray = np.array(tL).reshape(len(tL),1)
		return tLArray[dist(tStates, X) < vol].tolist()[0]


def steer(l, x, dist=dist):
	arr = np.array(l).reshape((len(ACTIONS),3))
	return l[np.argmin(dist(arr, np.full_like(arr, x)))]


def isGoal(t, goal):
	return dist(t.state, goal) < GOAL_THRESH


def getPath(start, goal):
	searchList = [Tree(None, start)]
	tClosest = None
	feas = False
	i = 0
	# while (tClosest is None or not isGoal(tClosest, goal)) and i < MAX_VERTS:
	while i < MAX_VERTS:
		xRand = getRandomStates()
		tNearest = getNearest(searchList, xRand)
		xNew = steer([getNextState(tNearest.state, a) for a in ACTIONS], xRand)

# 		Obstacle check
		tNear = getNearest(searchList, tNearest.state, NEIGHBORHOOD)
		tMin = tNearest

		# Choose parent
		for t in tNear:
# 			Obstacle check
			if t.cost + dist(t.state, xNew) < tMin.cost + dist(tMin.state, xNew):
				tMin = t
		tNew = Tree(tMin, xNew)

		searchList.append(tNew)
		tClosest = getNearest(searchList, goal)

		# Rewire
		if tMin in tNear:
			tNear.remove(tMin)
		for t in tNear:
			if t.cost > tNew.cost + dist(tNew.state, t.state):
				if t.parent is not None:
					t.parent = tNew
		if isGoal(tClosest, goal) and not feas:
			print("Feasible path found!")
			feas = True
		# elif feas and i % 100 == 0:
		# 	print("Current best path cost: {}".format(tClosest.cost))
		i += 1

	if i == MAX_VERTS:
		print("Max vertices ({}) reached".format(MAX_VERTS))
		print("Goal distance: {}".format(dist(tClosest.state, goal)))


	tClosest = getNearest(searchList, goal)
	path = []
	while tClosest is not None:
		path.insert(0, tClosest.state)
		tClosest = tClosest.parent

	return searchList, path






