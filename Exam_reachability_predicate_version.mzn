include "globals.mzn";

par int : n;

array[1..n] of int: fixed_costs;

array[1..n, 1..n] of int: distances;

array[1..n, 1..n] of int: existing_bridges;

array[1..n*(n-1) div 2] of int: from = [i | i in 1..n, j in 1..n where i < j];

array[1..n*(n-1) div 2] of int: to = [j | i in 1..n, j in 1..n where i < j];

array[1..n] of var bool : ns;

array[1..n*(n-1) div 2] of var bool : es;

% Ensure all nodes are reachable from the root
constraint forall(r in 1..n)(
  reachable(n, n*(n-1) div 2, from, to, r, ns, es)
);

% Ensure all nodes are included
constraint forall(i in 1..n)(ns[i] = true);

var int : cost = sum(i in 1..n*(n-1) div 2)(
    if(existing_bridges[from[i], to[i]] == 0) then
      es[i]*(distances[from[i], to[i]]*10 + fixed_costs[from[i]] + fixed_costs[to[i]])
    else 0
    endif 
  );
solve minimize cost;

output [
  "Value of es: ", show(es), "\n",
  "Value of cost: ", show(cost), "\n"
];