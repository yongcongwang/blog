---
title: General Path Planning Methods
mathjax: true
categories:
  - autonomous
date: 2021-02-21 15:23:25
---
Path-planning is an important primitive for autonomous mobile robots that lets robots find the shortest(or otherwise optimal) path between two points. Otherwise optimal paths could be paths that minimize the amount of turning, the amount of braking or whatever a specific application requires. Algorithms to find a shortest path are important not only in robotics, but also in network routing, video games and gene sequencing.

<!-- more -->

# Behavior Planning
The goal of `behavior planning` is to find a movable path in configuration space for `motion planning` to generate a smoother and cost lower trajectory.

Before planning process, we generally transform obstacles from workspace to configuration space which makes the planning task less complicated. In workspace, robot has shape and size which is hard for motion planning. After tranfomation, the robot becomes a point while obstacles are expended:
![configuration space](/images/2021/planning/configuration_space.png)

## Based on graph searching
A typical workflow of graph searching is:
- Maintain a `container` to store all the nodes `to be visited`
- The container is initialized with the start state
- Loop:
 - `Remove` a node from the container according to some pre-defined score function
 - `Expand`: obtain all `neighbors` of the node
 - `Push`: the neibors into the container
- End loop

Two frequently used methods to search the graph are:
- Breadth First Search(BFS), which use a `queue` to store the nodes to be discoved;
- Depth First Search(DFS), which use a `stack` to storee the nodes to be discovered.

### Greedy best first search
`BFS` and `DFS` pick the next node off the frontiers based on which was `first` on `last-in`, while the Greedy best first search picks the `best` node according to some rule, called `heuristic`. 
> A `heuristic` is a guess of how close you are to the target.
There are two commonly used distance to `guess` the distance to the target:
- Euclidean Distance, which assume that you can move in any direction;
- Manhattan Distance, which assume that you can only move in four direction: up/down/left/right.

The greedy best first search works fine with an empty map, but in a more complated map it may find the path which is not the global optimal.

### Dijkstra
Dijkstra expands the node with the `cheapest accumulated cost g(n)`. `g(n)` is the current best estimates of the accumulated cost from the start state to node `n`. And a node expaned is guaranteed to have the smallest cost from the start state.

The process of the algorithm is as:
- Maintain a `priority queue` to store all the nodes to be expanded
- The priority queue is initialized with the start state $X_s$
- Assign $g(X_x) = 0$ and $g(n) = infinite$ for all other nodes in graph
- Loop:
 - If the queue is empty, return False, brea;
 - Removee the node n with the lowest $g(n)$ from the priority queue
 - Mark node n as expanded
 - If the node n is the goal state, return True, break
 - For all unexpanded neighbors "m" of "n":
  - If $g(m) == infinite$
   - $g(m)=g(n) + C_{nm}$
   - Push node "m" into the queue
  - If $g(m) > g(n) + C_{nm}$
   - $g(m) = g(n) + C_{nm}$
- End Loop

#### Pros
- Complete and optimal

#### Cons
- Can only see the cost accumulated so far, thus exploring next state in all direction
- No information about goal location

### `A*`
The `A*` algorithm is a dijkstra with heuristic. The cost of `A*` is estimated with:
$$
f(n) = g(n) + h(n)
$$
where
- $g(n)$ is the accumulate cost which represents current best estimates of the accumulated cost from the start state to node "n"
- $h(n)$ is the heuristic cost which represents the estimated least cost from node n to goal state.

While expanding the node, `A*` expands the node with cheapest $f(n)$.

The only difference comparing to Dijkstra's algorithm is that `A*` removes the node "n" with lowest $f(n)$ from the priority queue.

#### Optimality
`A*` has optimality only if:
$$
h(n) <= h^{\*}(n)
$$
where $h^\*(n)$ is the true least cost to goal from node "n".
- if $h(n) << h^\*(n)$, then the solution is optimal, but the searching speed will be slow;
- if $h(n) > h^\*(n)$, the solution is not optimal, which means that the path found by `A*` is not the shortest;
- if $h(n) == h^\*(n)$ the solution is optimal and the speed is the fast.

#### Speed up `A*`

##### The best heuristic
Even if we have an optimal heuristic cost, there is still something to optimize. For example, if we use the $f(n) == g(n)$ as cost function, we can surely find the shortest path, but the speed is slow. The closer our heuristic cost is to the actual length from node to goal, the less steps we go through.

![heuristic](/images/2021/planning/heuristic.png)

##### Tie breaker
In a 2D path without any obstacles, many paths have the same $f(n)$ value. There is no differences among them making them explored by `A*` equally.
![tie](/images/2021/planning/tie.png)
We can change the $f(n)$ value slightly to break the tie:
- Interfere $h$ slightly: $h = h * (1.0 + p)$, where $p = \frac{mincost}{maxcost}$;
- while the $f$ is same, compare $h$;
- add deterministic random numbers to the heuristic or edge costs(A hash of the coordinates);
- prefer paths that are along the straight line from the starting point to the goal;
- other more...

### JPS(Jump Point Search)
Jump point search is a systematic approach to solve the tie problem of `A*`. The core idea of JPS is to find the symmetry and break them.
![jps](/images/2021/planning/jps.png)
JPS explores intelligently, becasue it always looks ahead and jump.

#### Look ahead rule
![look ahead](/images/2021/planning/ahead.png)

- Neighbor pruning:
 - gray node: inferior neighbors, when going to them, the path without x is cheaper, Discard.
 - white node: nutural neighbors.
 - we only need to consider natural neighbors when expand the search.
- Forced neighbors
 - There is obstacle adjacent to x.
 - Red nodes are forced neighbors.
 - A cheaper path from x's parent to them is blocked by obstacle.

#### Jumping rule
![jump](/images/2021/planning/jump.png)

- Recursively apply straight pruning rule and identify y as a jump point successor of x. This node is interesting because it has a neighbor z that can not reached optimally except by a path that visit x then y.
- Recursively apply the diagonal pruning rulea and identify y as a jump point successor of x.
- Before each diagonal step we first recurse straight. Only if both straight recursions fail to identify a jmp point do we step diagonally again.
- Node w, a forced neighbor of x, is expanded as normal.

#### Conclusion
- Most time, especially in complex environments, JPS is better, but far away from alway. For example, a large map with not many obstacles, JPS may be slower than `A*`.
- JPS reduces the number of nodes in `open list`, but increase the number of status query.
- JPS' limitation: only applicable to uniform grid map.

## Based on sampling

## Based on kinodynamic model

# Motion Planning

## Minimum snap trajectory generation

## Soft and hard constrained trajectory optimization

# MDP & MPC

# Reference
- [Motion Planning for Mobile Robots](https://www.shenlanxueyuan.com/course/268)

