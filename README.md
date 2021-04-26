# Author: Abhi Balijepalli

### About:
Implementing the Chicken and Wolves puzzle using Uniformed and Informed search. Given a start state and a goal state, you have to generate successors.

For example, the initial state
0,0,0
3,3,1
represents 3 chickens, 3 wolves and the boat being on the right bank of the river and nothing on the left bank.

Search Algorithms Used:
- Depth First Search
- Breadth First Search
- Iterative Deepening Depth First Search
- A-Star Search

### Information:
Algorithms: `bfs, dfs, iddfs, astar`

Start Files: `start1.txt, start2.txt, start3.txt`

Goal Files: `goal1.txt, goal2.txt, goal3.txt`

To Compile & Run
- `python3 app.py <startX.txt> <goalX.txt> <algo name> <output file>`
  - `python3 app.py start1.txt goal1.txt bfs output.txt`
