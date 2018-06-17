import numpy as np

MIN_VAL = -10
MAX_VAL = 10
# MAX_TURN = np.pi/3
ACTIONS = [-1,0,1]
dt = .5
L = 1


def getRandomStates(num=1):
	s = 0.75*(MAX_VAL - MIN_VAL)*np.random.rand(num, 3) - abs(MIN_VAL)*.75
	s[:,2] = abs(s[:,2]) % 2*np.pi
	return s


def getNextState(pState, uR):
	nState = pState + dt*np.array([np.cos(pState[2]), np.sin(pState[2]), uR])
	if nState[2] < 0:
		nState[2] += 2*np.pi
	elif nState[2] > 0:
		nState[2] %= 2*np.pi
	return nState