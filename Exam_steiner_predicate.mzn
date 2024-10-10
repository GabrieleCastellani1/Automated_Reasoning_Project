include "globals.mzn";

par int : n;

array[1..n] of int: fixed_costs;

array[1..n, 1..n] of int: distances;

array[1..n, 1..n] of int: existing_bridges;

array[1..n*(n-1) div 2] of int: from = [i | i in 1..n, j in 1..n where i < j];

array[1..n*(n-1) div 2] of int: to = [j | i in 1..n, j in 1..n where i < j];

array[1..n] of var bool : ns;

array[1..n*(n-1) div 2] of var bool : es;

array[1..n*(n-1) div 2] of int : w = [(distances[from[i], to[i]] * 10
                                     + fixed_costs[from[i]]
                                     + fixed_costs[to[i]]) * (1-existing_bridges[from[i], to[i]])
                                     | i in 1..n*(n-1) div 2];
var int : k;
% Ensure all nodes are reachable from the root
constraint steiner(n, n*(n-1) div 2, from, to, w, ns, es, k);

% Ensure all nodes are included
constraint forall(i in 1..n)(ns[i] = true);

solve minimize k;

output [
  "Value of es: ", show(es), "\n",
  "Value of k: ", show(k), "\n"
];