
## Link Analysis

#### Web Graph
Webpages have hyperlinks that redirect to other pages on the web. The Web's this hyperlink structure can be represented as a __directed graph__, where each node represents a Web page and each edge represents a link.

Hyperlinks directed into a page are referred as **inlinks**, whole those originating from a page are called **outlinks**. The Web graph has been intensively studied over recent years, and it has been empirically shown to be far from strongly connected.

Theoretical models have shown that, in the large, the Web graph can be modeled in terms of degree distribution which follows a *power law*:


In a seminal study, authors mapped a large Web crawl, showing that , unlike what was wstimated by previous studies, the Web is not structured as clusters of sites forming a well-connected sphere. Instead , the Web graph resembles a vow-tie shape.


- **Core**, accounts for around 30% of the pages, which is made by large strongly connected components (SCCs)
- The left **IN** bow contains upstream nodes, i.e., pages that allow users to reach the core but that have not yet been linked to; typically new or unpopular webpages.
- The right **OUT** bow contains downstream nodes, i.e., pages that can be reached from the core but do not link back to it; corporate or commercial websites containing internal links only.
- **Tendrils**, contain nodes that are linked by an upstream or downstream nodes, but can neither reach nor be reached from the core.
- Rest are the disconnected components, small group of nodes not connected to the bow tie.


## Link-Based Ranking

In addition to being the structural backbone of the simple yet successful user navigation paradigm of the Web, hyperlinks can also be viewed as evidences of endorsement, or recommendation; under this assumption, a page with more recommendations (incoming links) can be considered more important than a page with less incoming links. However, for a recommendation to be relevant, the recommender should possess some sort of authority. Likewise, for a recommender to be authoritative, it must be considered a relevant source of recommendation.

We can distinguish ranking systems into query-independant and query-dependant systems.

- **Query-Independant Systems** aim at ranking the entire Web, typically only based on the authoritativeness of the considered results. The authoritativeness is computed **offline**. The most popular example of such systems is **PageRank**.
- **Query-dependant Systems** work on a reduced set of resources, typically the ones that have been identified as related to the submitted query. They can be computed **online** at query time. The most popular example of such systems is **HITS**.


### PageRank

The PageRank method focuses only on the authority dimension of a page and, in its simpler version, considers a Web page important if it is pointed to by another important page, thus assigning a single popularity score to it, the PageRank score.

This score is query independent, that is, its value is determined offline and it remains constant regardless of the query.

- $A$ is the $n*n$ weighted adjacency matrix, where $A_{ij} = 0$ if there is no link between the pages, otherwise $A_{ij} = \frac{1}{n_j}$, $n_j$ being s the number of $x_j ’$s outgoing links.
- $x$, is a column matrix where $x_i$ is the page rank of the page $i$.
$$x_i = \sum_{j\in L_i}  \frac{x_j}{n_j}$$
- On solving the system of equations, we get $$ Ax = x$$

#### Random Page Surfer Model
As the importance of a Web page can be associated with the number of incoming links it has, $A_{ij}$ can be viewed as the probability of going from page j to page i, and the process of finding the PageRank vector as a random walk on the Web graph. 

Here, we start with equal probabilities of visiting a page and calculate the probability of visiting a page after k steps which will be equal to $A^kx$

The iterative process described above is known as the power iteration method, a simple iterative method for finding the dominant eigenvalue and eigenvector of a matrix, and it can be used to obtain the final PageRank vector.
$$x^* = \lim_{k \to \infty} A^kx$$

If the web graph is SCC, then this value will converge. However, strong connectivity is almost impossible to reach because of two phenomenon: _dangling nodes_ and _disconnected graph_.

- Due to presence of dangling nodes, the matrix $A$ may not be _column stochastic_ i.e. the sum of all the columns is not 1. To cope with this:
  - Either remove the _dangling nodes_.
  - _Stochastic Adjustment_ is applied to all the **0** columns of the matrixx $A$: specifically all the elements of such columns are replaced with $\frac{1}{n}$ to represent the probability of random surfer to land at nay other page equally. Thus, resulting in $S$: $$ S = A + a\left(\frac{1}{n}\right)e^T$$
  > a is the dangling node vector, where $a_i = 1$ if the node $i$ represents a dangling node, or $0$ otherwise and $e = [ 1 1 \ldots 1]^T$ a vector of all ones. 
  
- **Disconnected Graph**: Due to the presence of disconnected subgraphs, the iterations may not converge to a unique solution.  To handle this the idea of _teleportation_, i.e., a periodically activated jump from the current page to a random one was introduced, which is represented as matrix $M$: $$M = \alpha S + (1 - \alpha )E$$ where $\alpha$ is the _damping factor_ and $E$ is the teleportation matrix that uniformly guarantees to all nodes an equal likelihood of being the destination of a teleportation and is defines as $$E = \frac{1}{n} ee^T$$ 
Thus, finally the page ranks are calculated as :
$$x^* = \lim_{k \to \infty} M^kx$$
 

### HITS ( Hypertext-Induced Topic Search )

HITS exploits both the inlinks and outlinks of Web pages Pi to create two popularity scores: (i) the hub score, $h(P_i)$, and (ii) the authority score, $a(P_i)$.

The hub score provides an indication of the importance of the links which exit the node and is used in order to select the pages containing relevant information, whereas the authority score measures the value of the links which enter the node and is used to describe contents.

The implementation of HITS involves two main steps: (i) the construction of the Web graph stemming from the submitted query, and (ii) the calculation of the final authority and hub scores.

> **NOTE:** However, here in this implementation we are not considering the first part and have done the calculation of scores for a given graph. 


As in PageRank, the values of hub and authority scores for pages in the graph are calcuated in an iterative fashion.

**The authority score $a(P_j )$ of a page j is proportional to the sum of the hub scores $h(P_j )$ of the pages $P_j \in BI_{P_i}$ , where $BI_{P_i}$ are the pages linking into $P_i$; conversely, the hub score $h(P_i)$ of a page $i$ is proportional to the authority scores $a(P_j )$ of the pages $P_j \in BO_{P_i}$ , where $BO_{P_i}$ are the pages to which $P_i$ links.**

The hub and authority scores can be calculated by iteratively solving the following equation systems:
$$a_{norm}^k = E^Th^{k-1}, a^k = \frac{a_{norm}^k}{\lVert a_{norm}^k \rVert}_1$$
$$h_{norm}^k = Ea^{k}, h^k = \frac{h_{norm}^k}{\lVert h_{norm}^k \rVert}_1$$

$E$ denote the adjacency matrix of the directed graph composed by the base set of pages, where $E_{ij} = 1$ if there is a link from the node i to the node j , while $E_{ij} = 0$ otherwise.

> **Note:** In **HITS**, the adjacency matrix is similar to the usual matrix convetions that we use for defining the graph. However, in the case of **PageRank**, we work on the **transpose** of the actual adjcaency matrix.

Similarly to the PageRank, the computation of $a$ and $h$ can be cast as a problem of finding the eigenvector associated to the largest eigenvalue of a square matrix. The two equations can be simplified to:
$$a_{norm}^k = E^TEa^{k-1}, a^k = \frac{a_{norm}^k}{\lVert a_{norm}^k \rVert}_1$$
$$h_{norm}^k = EE^Th^{k-1}, h^k = \frac{h_{norm}^k}{\lVert h_{norm}^k \rVert}_1$$

Sometimes, $A$ and $H$ are also used in notations, where $$A = E^TE$$  $$H=EE^T$$

### Thank You !!!
