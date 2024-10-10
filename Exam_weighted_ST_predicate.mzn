include "globals.mzn";

par int : n;

array[1..n] of int: fixed_costs;

array[1..n, 1..n] of int: distances;

array[1..n, 1..n] of int: existing_bridges;

array[1..n*(n-1) div 2] of int: from = [i | i in 1..n, j in 1..n where i < j];

array[1..n*(n-1) div 2] of int: to = [j | i in 1..n, j in 1..n where i < j];

array[1..n*(n-1) div 2] of var bool : es;

array[1..n*(n-1) div 2] of int : w = [(distances[from[i], to[i]] * 10
                                     + fixed_costs[from[i]]
                                     + fixed_costs[to[i]]) * (1-existing_bridges[from[i], to[i]])
                                     | i in 1..n*(n-1) div 2];
var int : k;
% Ensure all nodes are reachable from the root
constraint weighted_spanning_tree(n, n*(n-1) div 2, from, to, w, es, k);

solve minimize k;