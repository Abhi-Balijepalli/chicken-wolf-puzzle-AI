# Author: Abhi Balijepalli
# Date: 4/18/2021
# Description: This file contains possible actions a algorithm mode can take.

def type1(state):
    if state[0][2] == 1:
        state[0][0] -= 1
        state[1][0] += 1
        state[0][2] -= 1
        state[1][2] += 1

    elif state[1][2] == 1:
        state[0][0] += 1
        state[1][0] -= 1
        state[0][2] += 1
        state[1][2] -= 1
    else:
        return None

def type2(state):
    if state[0][2] == 1:
        state[0][0] -= 2
        state[1][0] += 2
        state[0][2] -= 1
        state[1][2] += 1

    elif state[1][2] == 1:
        state[0][0] += 2
        state[1][0] -= 2
        state[0][2] += 1
        state[1][2] -= 1
    else:
        return None

def type3(state):
    if state[0][2] == 1:
        state[0][1] -= 1
        state[1][1] += 1
        state[0][2] -= 1
        state[1][2] += 1

    elif state[1][2] == 1:
        state[0][1] += 1
        state[1][1] -= 1
        state[0][2] += 1
        state[1][2] -= 1
    else:
        return None

def type4(state):
    if state[0][2] == 1:
        state[0][0] -= 1
        state[1][0] += 1
        state[0][1] -= 1
        state[1][1] += 1
        state[0][2] -= 1
        state[1][2] += 1

    elif state[1][2] == 1:
        state[0][0] += 1
        state[1][0] -= 1
        state[0][1] += 1
        state[1][1] -= 1
        state[0][2] += 1
        state[1][2] -= 1
    else:
        return None

def type5(state):
    if state[0][2] == 1:
        state[0][1] -= 2
        state[1][1] += 2
        state[0][2] -= 1
        state[1][2] += 1

    elif state[1][2] == 1:
        state[0][1] += 2
        state[1][1] -= 2
        state[0][2] += 1
        state[1][2] -= 1
    else:
        return None
