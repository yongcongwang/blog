---
title: Basic Graph Theory
mathjax: true
date: 2021-03-18 16:31:51
---
A `Graph` consists of:
- `node`s(vertices) and
- `edge`s which connecting these `node`s.

<!-- more -->

Graphs are mathematical structures uesed to model pairwise relations between objects. 
![graph definition](/images/2021/graph/graph_def.png)

A distinction is made between:
- `undirected graph`: where edges link two nodes symmetrically;
- `directed graph`: where edges link two nodes asymmetrically.


# Breadth-first Search(BFS)
BFS is an algorithm for traversing or searching tree or graph data structures. It starts at the tree root(or some arbitrary node of a graph, sometimes referred as a `search key`), and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.

![bfs](/images/2021/graph/bfs.gif)
```C++
void bfs(int start) {
  // build graph
  deque<int> d{start};
  unordered_set<int> visited{start};
  while (!d.empty()) {
    int node = d.front();
    d.pop_front();
    for (auto next : graph[node]) {
      if (visited.count(next)) continue;
      visited.insert(next);
      d.push_back(next);
    }
  }
}
```

# Depth-first Search(DFS)
DFS is an algorithm for traversing or searching tree or graph data structure. The algorithm starts at the root node(selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking.

![dfs](/images/2021/graph/dfs.gif)
```C++
void dfs(Graph& graph, unordered_set<int>& visited, int root) {
  if (visited.count(root)) return;
  for (auto next : graph[root]) {
    dfs(graph, visited, next);
  }
}
```

# Shortest Path
In graph theory, the `shortest path problem` is the problem of finding a path between two nodes in a graph such that the sum of the weights of its constituent edges is minimized. The mainly used algorihtms are:
- Floyd
- Bellman-Ford
- Dijkstra

| Floyd | Bellman-Ford | Dijkstra |
| --- | --- | --- |
| Multiple-source Shortest Path | Singole-source Shortest Path | Single-source Shortest Path |
| Not negtive cycle graph | any graph | Not negtive edge graph |
| $O(N^3)$ | $O(NM)$ | $O(MlogM)$ |

## Floyd
Floyd algorithm compares all possible paths through the graph between each pair of vertices.
```C++
vector<vector<int>> floyd(Graph& graph, int node) {
  auto m = graph.size();
  vector distance(m + 1, vector<int>(m + 1, INT_MAX));
  for (int i = 1; i <= n; ++i) distance[i][i] = 0;
  for (int k = 1; k <= n; ++k) {
    for (int i = 1; i <= n; ++i) {
      for (int j = 1; j <= n; ++j) {
        distance[i][j] = min(distance[i][j], distance[i][k] + graph[k][j]);
      }
    }
  }

  return distance;  // RVO
}
```

## Bellman-Ford
Bellman-Ford is an algorithm that computes shortest paths from a single source node to all of the other nodes in a weighted digraph. It is capable of handling graphs in which some of the edge weights are negtive numbers.
```C++
int bellman_ford(Graph& graph, int src, int tar) {
  queue<int> q{src};
  unordered_set<int> visited{src};
  vector distance(graph.size() + 1, INT_MAX);
  distance[src] = 0;

  auto relax = [&](auto src, auto tar) -> bool {
    if (distance[src] + graph[src][tar] > distance[tar]) return false;
    distance[tar] = distance[src] + graph[src][tar];
    return true;
  };

  while (!q.empty()) {
    int node = q.top();
    q.pop();
    visited.erase(node);
    for (auto next : graph[node]) {
      if (relax(node, next) && !visited.count(next)) {
        visited.insert(next);
        q.push(next);
      }
    }
  }

  return distance[tar];
}
```

## Dijkstra
Dijkstra is an algorithm that computes shortest paths from a single source node to all of the other nodes in a weighted digraph. It is not able to handle graphs in which some of the edge weights are negtive numbers.
![dijkstra](/images/2021/graph/dijkstra.gif)

```C++
int dijkstra(Graph& graph, int src, int tar) {
  vector distance(graph.size() + 1, INT_MAX);
  distance[src] = 0;

  auto lt = [](auto& a, auto& b) { return a.second < b.second; };
  usint PII = pair<int, int>;
  priority_queue<PII, vector<PII>, decltype(lt)> q(lt);

  auto relax = [&](auto src, auto tar) -> bool {
    if (distance[src] + graph[src][tar] > distance[tar]) return false;
    distance[tar] = distance[src] + graph[src][tar];
    return true;
  };

  while (!q.empty()) {
    auto [node, val] = q.top();
    q.pop();

    for (auto next : graph[node]) {
      if (relax(node, next)) q.emplace_back(next, distance[next]);
    }
  }

  return distance[tar];
}
```

# Topological Sorting
A topological sort of a directed graph is a linear ordering of its nodes such that for every directed edge $(u, v)$, $u$ comes before $v$ in the ordering.

## BFS
```C++
vector<int> res{};
bool topo_sort(Graph& graph, vector<int>& in_degree) {
  queue<int> q{};
  for (int i = 0; i < in_degree.size(); ++i) {
    if (in_degree[i] == 0) q.push(i);
  }

  while (!q.empty()) {
    int node = q.top();
    q.pop();
    res.push(node);
    for (auto next : graph[node]) {
      in_degree[next]--;
      if (in_degree[next] == 0) q.push(next);
    }
  }

  return res.size() == in_degree.size();
}
```

## DFS
```C++
vector<int> color{};  // 0: white; 1: gray; 2: black
vector<int> topo{};

bool dfs(Graph& graph, int node) {
  color[node] = 1;
  for (auto next : graph[node]) {
    if (color[next] == 1) return false;
    if (color[next] == 0 && !dfs(graph, next)) return false;
  }
  color[node] = 2;
  topo.push_back(node);
  return true;
}

bool topo_sort(Graph& graph) {
  color.resize(graph.size(), 0);
  topo.clear();

  for (int i = 0; i < graph.size(); ++i) {
    if (color[i] == 0 && !dfs(graph, i)) return false;
  }
  reverse(topo.begin(), topo.end());
  return true;
}
```

# Minimum Spanning Tree(MST)
## Prim
## kruscal

# Strongly connected components
## Tarjan
## Kosaraju

# Oral Graph
## Fleury
# Hierholzer

# Union-Find
A `union-find` is a data structure that stores a collection of disjoint(non-overlapping) setting. Equivalently, it stores a partition of a set into disjoint subsets. It provides operations for adding new sets, merging sets and finding a representative member of a set.
```C++
class UnionFind {
 public:
  Union(int n) : size(n, 1) {
    for (int i = 0; i < n; ++i) parent.push_back(i);
  }

 public:
  int find(int x) {
    if (parent[x] != x) parent[x] = find(parent[x]);
    return parent[x];
  }

  bool unite(int x, int y) {
    int xx = find(x);
    int yy = find(y);
    if (xx == yy) return false;
    if (size[xx] > size[yy]) swap(xx, yy);
    parent[xx] = yy;
    size[yy] += size[xx];
    return true;
  }

 private:
  vector<int> parent{};
  vector<int> size{};
};
```


# Reference
- [10 Graph Algorithms Visually Explained](https://towardsdatascience.com/10-graph-algorithms-visually-explained-e57faa1336f3)
- [OI WIKI/Graph](https://oi-wiki.org/graph/)
