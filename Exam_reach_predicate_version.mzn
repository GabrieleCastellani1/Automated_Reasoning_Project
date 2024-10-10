include "globals.mzn";

int : n; % number of nodes

array[1..n] of int: fixed_costs;

array[1..n, 1..n] of var 0..1 : edges;

array[1..n, 1..n] of int: existing_bridges;

array[1..n, 1..n] of int: distances;

predicate reach(int: n1, int: n2, set of int : visited) =
  edges[n1, n2] == 1
  \/
  existing_bridges[n1, n2] == 1
  \/
  (not (n1 in visited) /\
  exists(j in 1..n)((edges[n1, j] = 1 \/ existing_bridges[n1, j] == 1)
  /\ reach(j, n2, visited union{n1})));

% Symmetry of bridges
constraint forall(i,j in 1..n where i < j)(
  edges[i,j] = edges[j,i]
);

% All islands must be able to reach each other
constraint forall(i, j in 1..n where i < j)(
  reach(i, j, {})
);

var int: cost = sum(i, j in 1..n where i < j /\ existing_bridges[i, j] = 0) ((
                distances[i,j]*10
                + fixed_costs[i]
                + fixed_costs[j])*edges[i,j]);

solve minimize cost;

output [
  "Value of cost: ", show(cost), "\n",
  "Value of edges: ", show(edges), "\n"
];