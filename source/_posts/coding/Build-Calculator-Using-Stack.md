---
title: Interview coding problems
mathjax: true
categories:
  - coding
date: 2019-08-15 09:55:30
---
Write a function that takes a string of arithmetic equation and return a scalar as the evaluation of the equation arithmetic supports 4 operators: `+`, `*`, `&`, `|`, where + and * are defined as usual, & and | are defined as pairwise max, min, respectively A & B = fmax(A, B), A | B = fmin(A, B)

<!-- more -->

# Pony

## 最小的三角形
```python
'''
二维平面上有N个点，每个点用二维坐标表示，找到三个点让他们组成三角形，使得其他所有的点都不在三角形内部，返回这样的三个点的坐标。
'''

###### 想了个Nlog（N）的，先对所有的点按照x轴坐标排序，然后连续的三个点就有可能是满足条件的点。但是需要判断一下多个点是否共线这种情况。
def func(points):
    points.sort(key=lambda x:x[0])
    for i in range(len(points)-2):
        j=i+1
        k=i+2
        xs=[p[0] for p in points[i:i+3]]
        ys=[p[1] for p in points[i:i+3]]
        if len(set(xs))==1:
            continue
        elif len(xs)==2:
            return points[i:i+3]
        if len(set(ys))==1 or (ys[1]-ys[0] )/(xs[1]-xs[0]) == (ys[2]-ys[0])/(xs[2]-xs[0]):
            continue
        else:
            return points[i:i+3]
    return []

# PS:面试官表示还有O(N)的做法，首先选三个不共线的点组成原始的三角形，然后依次扫描其他的点，如果他们是在三角形的外部则直接跳过，否则的话该点替换掉其中的一个点，最后所有的点都判断完毕之后得到的三角形上的三个点也满足题目要求。
```
## 众数数目最大
```python
'''
给定一个包含int数据的数组，和一个整数k。 每一次可以对数组中的一个数进行加一操作，最多可以做k次操作，k可以不用完。
希望能够使数组中相同的数字数目最多（也就是众数的数目最大），返回这个最大值

例如：
{1,2,4,4}  k=2 可以操作得到->{1,4,4,4}, 因此结果为3
'''


## 思路是先对数组排序，然后用一个左右指针表示的区间内的数字调整到区间内的最大值
# 如果区间内的和+k >= 区间最大值* 区间数目，则当前区间可以在不多于k次的操作下调整到相同的值，此时更新结果并，左移left指针
# 否则的话左移right指针
# 直到左指针小于0时终止循环。
def func(nums,k):
    nums.sort()

    pre_sum = [nums[0]]
    for i in range(1, len(nums)):
        cur_sum = pre_sum[-1] + nums[i]
        pre_sum.append(cur_sum)

    left = len(nums) - 1
    right = len(nums) - 1
    result = 1
    while left >= 0 and right >= 0:
        if right < result - 1:
            break
        t_sum = pre_sum[right] - pre_sum[left] + nums[left]  # why add nums[right]
        if t_sum + k >= (right - left + 1) * nums[right]:
            result = max(result, (right - left + 1))
            left -= 1
        else:
            right -= 1

    return result
```

## 安全区域数量

```python
'''
给定一个n*m的二维格点地图, 每个位置要么是字符’.’表示空地, 要么是’@’表示有敌人在这里. 规定给定一个d(1 <= d <= min(m, n)), 如果一个d*d的区域内没有任何敌人, 则认为这片区域是安全的.
问给定的地图中有多少个这样安全的区域.
'''

## 二维前缀和，将原始的地图转换成01矩阵，然后t_sum[i][j] 保存从（0,0） 到 （i，j）的矩形中所有元素的和
## 然后遍历二维矩阵 利用前缀和 计算以(i,j)作为左上角的d*d的区域内的元素和，如果是0，说明是安全区+1
## 总体时间复杂度 O(N*M)

def convert(data): # 转换成01矩阵
    n=len(data)
    m=len(data[0])
    matrix=[[0]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if data[i][j]=='@':
                matrix[i][j]=1
    return matrix


def func(matrix,d):
    n=len(matrix)
    m=len(matrix[0])

    t_sum=[[0]*m for i in range(n)]

    for j in range(m):
        t_sum[0][j]=t_sum[0][j-1]+matrix[0][j]

    for i in range(1,n):
        t_sum[i][0]=t_sum[i-1][0]+matrix[i][0]

    for i in range(1,n):
        for j in range(1,m):
            t_sum[i][j]=t_sum[i][j-1]+t_sum[i-1][j]-t_sum[i-1][j-1]+matrix[i][j]

    result=1
    for i in range(n):
        if i+d>=n:
            break
        for j in range(m):
            if j+d>=m:
                break
            ni=i+d
            nj=j+d
            if i==0 and j==0:
               	tmp=t_sum[ni][nj]
            elif i==0:
                tmp=t_sum[ni][nj]-t_sum[ni][j-1]
            elif j==0:
                tmp=t_sum[ni][nj] -t_sum[i-1][nj]
            else:
            	tmp=t_sum[ni][nj]-t_sum[ni][j-1]-t_sum[i-1][nj]+t_sum[i-1][j-1]

            if tmp==0:
                result+=1
    return result
```

## 判断无向图是否为二叉树

```C++
bool Solve(int n, const vector<vector<int>>& edges) {
  if (n == 0) return true;

  vecotr<vector<int>> G(n);
  for (const auto& x : edges) {
      int& u = x[0], v = x[1];
    G[u].emplace_back(v);
    G[v].emplace_back(u);
  }

  vector<int> pre(n, 0);
  for (int i = 0; i < n; i++) {
      pre[i] = i;
  }

  function<int(int)> find = [&](int x) {
      return x == pre[x] ? x : pre[x] = find(pre[x]);
     };

  function<int(int, int)> unite = [&](int u, int v) {
      u = find(u); v = find(v);
    if (u == v) return 0;
    pre[u] = v;
    return 1;
  };

  bool ok = 1;

  function<void(int, int)> dfs = [&](int u, int p) {
    int tot = 0;
    for (int i = 0; i < G[u].size(); i++) {
        int& v = G[u][i];
      if (v == p) continue;
      if (!unite(u, v)) {
          ok = 0;
        break;
      }
      tot++;
      dfs(v, u);
    }
    if (tot > 2) {
        ok = 0;
    }
  };
  dfs(0, -1);

  int tot = 0;
  for (int i = 0; i < n; i++) {
      if (find(i) == i) tot++;
  }

  return ok && (tot == 1);
}

```
## n个时间段，让你计算最多多少段时间相互不重叠，证明算法正确性？贪心 10min
```C++
int Solve(vector<vector<int>>& seg) {
    int n = seg.size();
  if (n == 0) {
      return 0;
  }
    sort(seg.begin(), seg.end(), [&](const vector<int>& a, const vector<int>& b) {
      if (a[1] == b[1]) return a[0] < b[0];
    return a[1] < b[1];
  });
  int ret = 1;
  int ed = seg[0][1];
  for (int i = 1; i < n; i++) {
      if (seg[i][0] >= ed) {
        ed = seg[i][1];
      ret++;
    }
  }
  return ret;
}
```

## n个点（1E6） ，给k个点，求这k个点的LCA
```C++
int Solve(int n, int root, const vecotr<vector<int>>& G, const vector<int>& query) {
    // G[i][j] = v: i的第j条边是v。 G: G[i][j] == G[j][i]
  int m = query.size();
  unordered_set<int> qset(query.begin(), query.end());
  int lca = root, ldep = -1;
  function<int(int, int, int)> dfs = [&](int u, int p, int dep) {
    int tot = 0;
      for (int i = 0; i < G[u].size(); i++) {
        int v = G[u][i];
      if (v == p) continue;
      int tmp = dfs(v, u, dep + 1);
      if (ldep != -1) return INT_MAX;
      tot += tmp;
    }
    tot += (qset.find(u) != qset.end());
    if (tot == m && dep > ldep) {
        ldep = dep;
      lca = u;
    }
    return tot;
  };
  dfs(root, -1, 0);
  return lca;
}
```

## N*M的矩阵，有障碍物。给起点和终点，问从起点到终点最少需要移除多少块障碍物
```C++
using pii = pair<int, int>;

const int dx[5] = {0, 0, 1, -1};
const int dy[5] = {1, -1, 0, 0};

int Solve(const vector<vector<int>>& G, int sx, int sy, int ex, int ey) {
    int n = G.size();
  if (n == 0) return 0;
  int m = G[0].size();
  vector<int> pre(n * m + 1, 0);
  int ret = 0;

  for (int i = 0; i < n * m; i++) {
      pre[i] = i;
  }

  function<int(int, int)> ok = [&](int x, int y) {
      return x >= 0 && x < n && y >= 0 && y < m;
  };

  function<int(int, int)> id = [&](int x, int y) {
      return x * m + y;
  };

  function<pair<int, int>(int)> di = [&](int pos) {
      int x = pos / m;
    int y = pos % m;
    return make_pair(x, y);
  };

    function<int(int)> find = [&](int x) {
      return x == pre[x] ? x : pre[x] = find(pre[x]);
  };

  function<void(int, int)> unite = [&](int x, int y) {
      pre[find(x)] = find(y);
  };

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
      if (G[i][j] == 1) continue;
      for (int k = 0; k < 4; k++) {
        int xx = i + dx[k];
        int yy = j + dy[k];
          if (!ok(xx, yy)) continue;
        if (G[xx][yy] == 0) unite(id(i, j), id(xx, yy));
      }
    }
  }

  vector<pii> graph[n * m];
  for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
      for (int k = 0; k < 4; k++) {
        int xx = i + dx[k];
        int yy = j + dy[k];
          if (!ok(xx, yy)) continue;
        if (find(id(i, j)) == find(id(xx, yy))) continue;
        graph[id(i, j)].emplace_back(1, id(xx, yy));
        graph[id(xx, yy)].emplace_back(1, id(i, j));
      }
    }
  }

    vector<int> dis(n * m, 1E5);
  priority_queue<pii, vector<pii>, greater<pii>> pq;
  dis[find(id(sx, sy))] = 0;
    pq.emplace(dis[find(id(sx, sy))], id(sx, sy));
    while (!pq.empty()) {
      pii cur = pq.top(); pq.pop();
    int w = cur.first, v = cur.second;
    for (int i = 0; i < graph[v].size(); i++) {
      int u = graph[v][i].second;
        int d = w + graph[v][i].first;
      if (dis[v] + d < dis[u]) {
          dis[u] = dis[v] + d;
        pq.emplace(dis[u], u);
      }
    }
  }
  return dis[find(id(ex, ey))];
}

```
## 在2-D plane, 检查一个点是否在一个三角形内（四个点给定）：
叉乘
## 计算2-D多边形面积：
从三角形到凸多边形，凹的没答也没问

## 给定一个deque（大小1e5），每次pop头部两个element，大的push_back，小的push_front，问第m次(1e18)操作结果：
最多deque.size()次操作后，构成一个环

## Transform a linkedlist
Input: A -> B -> … -> S, Output: A -> S -> B -> S-1 -> C -> S-2 …）：【Time O(N) / Space O(1)】；

## 经典的递归算法题、汉诺塔问题，要求展示移动的流程
给定n个盘子串在一个a棍子上，借助一个辅助的棍子b，要求全部移动到盘子c上。

规则：
（1）每次移动一个盘子
（2）盘子只能放在比它大的盘子上面
```C++
class Solution {
public:
  void mv(int n, vector<int>& A, vector<int>& B, vector<int>& C) {
    if (n == 1) {
      C.push_back(A.back());
      A.pop_back();
    } else {
      mv(n - 1, A, C, B);
      C.push_back(A.back());
      A.pop_back();
      mv(n - 1, B, A, C);
    }
  }
  void hanota(vector<int>& A, vector<int>& B, vector<int>& C) {
    mv(A.size(), A, B, C);
  }
};
```
## 给一个数组和阈值x，求区间里最大值和最小值的差不大于x的最大区间长度。
## 给会议的start和end，求能开最多的会，蠡口原题。
## 一个全是0和1的二维矩阵，判断其中所有的1能不能构成一个等腰直角三角形，需要将三角形里所有的位置填充满，包括三条边和里面。这题写了好久，不太会，后来面试官改简单了一点，直角顶点朝向左下。

## n位数的递增数有多少个，递增数是123,123456,34789这样的，1334不算。
## 如何在圆内随机取点，蠡口原题。
## 前序遍历和后序遍历能否确定二叉树。

## 字符串匹配 A串长n B串长为m 以A每个位置为起点长为m的子串 排序后与B串做精确匹配，问有多少次精确匹配

## 给定整数数组a,要求数组b，b[i]定义为a[i]左边离自己最近的比自己小的数字的下标：单调栈，如果用跳表时间复杂度和正确性证明

## 有n个数，能不能分成两部分，每部分数的和相同

## 树同构问题
(众所周知，树的重心不会超过两个 所以分别做树hash去check就能判树同构)

## 圆上等概率的选3个点 构成锐角三角形的概率 (现场推导)

## medianofnumberstreamnumber是double类型
