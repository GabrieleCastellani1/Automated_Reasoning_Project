% Ensure that fixed edges are always selected
selected(X, Y) :- fixed_edge(X, Y).

% Choose edges to include in the spanning tree
{ selected(X, Y) : edge(X, Y, C)}.

selected(Y, X) :- selected(X, Y).

% Define reachability
reachable(X, Y) :- selected(X, Y).
reachable(X, Z) :- reachable(X, Y), reachable(Y, Z).

% All nodes must be reachable from any other node (connected graph)
:- node(X), node(Y), X < Y, not reachable(X, Y).

% Minimize the sum of the weights of the selected edges
#minimize { C * 10 + C1 + C2, X, Y : selected(X, Y), fixed_cost(X, C1), fixed_cost(Y, C2), edge(X, Y, C), not fixed_edge(X, Y)}.

#show selected/2.