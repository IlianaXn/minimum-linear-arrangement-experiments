# minimum-linear-arrangement-experiments
In general, the Minimum Linear Arrangement problem is defined as follows.
Given a graph G(V,E) where E with |E|=m and V with |V|=n are the sets of edges and vertices respectively, a permutation π (or a linear ordering of the vertices or an one-dimensional layout) is defined as <img src="https://render.githubusercontent.com/render/math?math={\color{black}\pi: V \rightarrow \{1,2,...,n\}}">. The Minimum Linear Arrangement problem requires to find the permutation π s.t. the below objective function is minimized:

<img src="https://render.githubusercontent.com/render/math?math={\color{black}\sum_{(i,j)\in E}{|\pi(i)-\pi(j)|}}">

It's been proven that this problem is NP-complete for the general case. The solution is trivial when $G$ is a complete graph, since every arrangement is optimal. However, when $G$ is a rooted or undirected tree, complete bipartite, hypercube, rectangular or square mesh, etc, there exist algorithms of polynomial time.

In this repo, we have so far implemented the following heuristics:
* Spectral sequencing [^ref1]
* Random and Normal layouts [^ref2]
* Local Search with 3 different definitions of 'neighborhood' [^ref2]:
  -  Two layouts are neighbors if one can move from
one to another by flipping the labels of any pair of nodes in
the graph. (version 2)
  -  Two layouts are neighbors if one can move from
one to another by flipping the labels of two adjacent nodes in
the graph. (version 2b)
  -  Two layouts are neighbors if one can move from
one to another by rotating the labels of any triplet of nodes in
the graph. (version 3)

We compare the results of the aforementioned heuristics with the optimal solution by executing the algorithm of Chung [^ref3] as provided by the [Linear Arrangement Library](https://cqllab.upc.edu/lal/).

For now, our experiments use the network of American football games between Division IA colleges during regular season Fall 2000, as compiled by M. Girvan and M. Newman. The nodes have values that indicate to which conferences they belong (``football.gml``). However, in order to obtain an undirected tree we extract the minimum spanning tree of the above graph. Our final graph has 115 nodes and 114 edges (``football.txt``). Some results are presented in the ``results.txt`` file.

[^ref1]:  M. Juvan, B. Mohar, "Optimal linear labelings and eigenvalues of graphs", Discr. Appl. Math. 36, 1992.
[^ref2]:  Jordi Petit, "Experiments on the minimum linear arrangement problem". ACM J. Exp. Algorithmics 8, Article 2.3, 2003.
[^ref3]:  F.R.K. Chung, "An optimal linear arrangements of trees", Computers \& Mathematics with Applications,10,43-60, 1984.
