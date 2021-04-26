# Author: Abhi Balijepalli
# Date: 4/18/2021
# Description: Uniformed and Informed Search (bfs,dfs,iddfs, A-star search)

import sys
# need it for deepcopies of the queue
import copy
import actions as ACTION
from queue import PriorityQueue


def game_condition(board):
    if board[0][0] >= board[0][1] and board[1][0] >= board[1][1]:
        return True
    else:
        if board[0][0] == 0 or board[1][0] == 0:
            return True
        else:
            return False

def final(list, list_2):
    if list[0][2] != list_2[0][2]:
        return 1
    else:
        return 0
def balance(board):
    count = 0
    for i in range(0,2):
        for j in range(0,2):
            if board[i][j] < 0:
                count +=1
    if count > 0:
        return False
    else:
        return True

def heuristic(start,goal):
    cost = 0
    for i in range(0,3):
        cost += abs(goal[0][i] - start[0][i])
    return cost

def a_star(start,goal,visitedNodes,array,output):
    file = open(output,'a')
    visitedNodes.append(start)
    cost = heuristic(start,goal)
    pq = PriorityQueue()
    pq.put((cost,start))
    solution_node = 0
    curr = 0

    while pq:
        array = pq.get()
        p = array[1]
        curr+=1

        text = str(p)+"\n"
        file.write(text)
        if p != goal:
            for i in range (6):
                temp = copy.deepcopy(p)
                if i == 0:
                    ACTION.type1(temp)
                elif i == 1:
                    ACTION.type2(temp)
                elif i == 2:
                    ACTION.type3(temp)
                elif i == 4:
                    ACTION.type4(temp)
                elif i == 5:
                    ACTION.type5(temp)
                if game_condition(temp) and balance(temp):
                    if temp not in visitedNodes:
                        visitedNodes.append(temp)
                        before_calculation = curr + heuristic(temp,goal)
                        pq.put((before_calculation,temp))
                        solution_node += final(temp, visitedNodes[-2])
        else:
            output_to_file = "\n Steps: " + str(solution_node + 1) + "\n Nodes Expanded: " + str(curr) + '\n'
            print(output_to_file)
            file.write(output_to_file)
            file.close()
            return
    return "No Solution Found"

def iterative_deepening_dfs(start,goal,output):
    file = open(output,'a')
    node = 0
    deepth = 0
    solution_node = 0

    for limit in range(0, 10000):
        queue = []
        visited = []
        queue.insert(0, start)
        visited.append(start)

        while queue and len(queue) <= limit:
            p = queue.pop(0)
            node+=1
            txt = str(p) + "\n"
            file.write(txt)

            if p != goal:
                for i in range (6):
                    temp = copy.deepcopy(p)
                    if i == 0:
                        ACTION.type1(temp)
                    elif i == 1:
                        ACTION.type2(temp)
                    elif i == 2:
                        ACTION.type3(temp)
                    elif i == 4:
                        ACTION.type4(temp)
                    elif i == 5:
                        ACTION.type5(temp)

                    if game_condition(temp) and balance(temp):
                        if temp not in visited:
                            visited.append(temp)
                            queue.insert(0, temp)
                            solution_node += final(temp, visited[-2])
            else:
                output_to_file = "\n Steps: " + str(solution_node + 1) + "\n Nodes Expanded: " + str(node) + '\n'
                print(output_to_file)
                file.write(output_to_file)
                file.close()
                exit()
    return "No Solution Found"


def depth_first_search(start,goal,queue,visitedNodes,output):
    visitedNodes.append(start)
    queue.append(start)
    file = open(output,'a')
    solution_node = 0
    curr = 0

    while queue:
        p = queue.pop(0)
        curr+=1
        text = str(p)+"\n"
        file.write(text)
        if p != goal:
            for i in range (6):
                temp = copy.deepcopy(p)
                if i == 0:
                    ACTION.type1(temp)
                elif i == 1:
                    ACTION.type2(temp)
                elif i == 2:
                    ACTION.type3(temp)
                elif i == 4:
                    ACTION.type4(temp)
                elif i == 5:
                    ACTION.type5(temp)
                if game_condition(temp) and balance(temp):
                    if temp not in visitedNodes:
                        visitedNodes.append(temp)
                        queue.insert(0,temp)
                        solution_node += final(temp, visitedNodes[-2])
        else:
            output_to_file = "\n Steps: " + str(solution_node + 1) + "\n Nodes Expanded: " + str(curr) + '\n'
            print(output_to_file)
            file.write(output_to_file)
            file.close()
            exit()
    return "No Solution Found"

def breadth_first_search(start, goal, visitedNodes, queue, output):
    visitedNodes.append(start)
    queue.append(start)
    solution_node = 0
    curr = 0
    file = open(output,'a')
    while queue:
        p = queue.pop(0)
        curr+=1
        text = str(p)+"\n"
        file.write(text)
        if p != goal:
            for i in range (6):
                temp = copy.deepcopy(p)
                if i == 0:
                    ACTION.type1(temp)
                elif i == 1:
                    ACTION.type2(temp)
                elif i == 2:
                    ACTION.type3(temp)
                elif i == 4:
                    ACTION.type4(temp)
                elif i == 5:
                    ACTION.type5(temp)
                if game_condition(temp) and balance(temp):
                    if temp not in visitedNodes:
                        visitedNodes.append(temp)
                        queue.append(temp)
                        solution_node += final(temp, visitedNodes[-2])
        else:

            output_to_file = "\n Steps: " + str(solution_node + 1) + "\n Nodes Expanded: " + str(curr) + '\n'
            print(output_to_file)
            file.write(output_to_file)
            file.close()
            exit()
    return "No Solution Found"

def process_file(f):
    file = open(f, "r")
    arr = []

    for i in range(0,2):
        line = file.readline()[:-1]
        temp = []
        for x in line.split(','):
            temp.append(int(x))
        arr.append(temp)
    file.close()

    return arr

def main():
    start_file = process_file(sys.argv[1])
    goal_file = process_file(sys.argv[2])
    algo_mode = sys.argv[3]
    output = sys.argv[4]

    if algo_mode == "bfs":
        breadth_first_search(start_file, goal_file, [], [], output)
    elif algo_mode == "dfs":
        depth_first_search(start_file,goal_file,[],[],output)
    elif algo_mode == "iddfs":
        iterative_deepening_dfs(start_file,goal_file,output)
    elif algo_mode == "astar":
        a_star(start_file,goal_file,[],[],output)
    else:
        return "Error"

if __name__ == "__main__":
    main()
