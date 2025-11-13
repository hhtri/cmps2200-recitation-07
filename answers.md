# CMPS 2200 Recitation 10## Answers

**Name:** Tri Huynh
**Name:** Kiet Huynh

- **2)** Assuming $n$ nodes and $m$ edges, the work is $O(n + m)$ because each node only makes it into the frontier once, and as we pop nodes off, we end up scanning through all their neighbors. Since the total number of neighbor checks across the whole graph is proportional to the number of edges, everything adds up to linear work in the size of the graph.

- **4)** In the worst case, we would still only need to call `reachable` one time because a single check with the function from any starting node already tells us whether we can get to every other node in the graph.

- **5)** The work of `connected` is $O(n+m)$ because it just makes one call to `reachable`, and that call already does all the work of exploring the graph. Outside of that, connected only does constant-time steps like picking a start node and comparing set sizes, so the overall cost is dominated by the single reachability run.

- **7)** Yes, the work would change. With an adjacency matrix, reachable would take $O(n^2)$ work, because every time we visit a node we have to scan its entire row of the matrix to see which edges exist, even if there are very few actual edges. In the worst case we end up doing this for about $n$ nodes, so the total work scales like $n$ x $n$ = $n^2$ instead of $O(n+m)$ like with an adjacency list.