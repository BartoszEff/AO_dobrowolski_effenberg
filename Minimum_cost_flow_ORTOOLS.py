
import numpy as np

from ortools.graph.python import min_cost_flow


def main():
 

    smcf = min_cost_flow.SimpleMinCostFlow()

    start_nodes = np.array([0, 0, 1, 1, 1, 2, 2, 3, 4, 5, 5, 5, 0, 1, 2])
    end_nodes = np.array([1, 2, 2, 3, 4, 3, 4, 4, 2, 0, 1, 2, 5, 3, 4])
    capacities = np.array([15, 8, 20, 4, 10, 15, 4, 20, 5, 15, 10, 8, 100, 100, 100])
    unit_costs = np.array([4, 4, 2, 2, 6, 1, 3, 2, 3, 4, 4, 2, 0, 0, 0]) 

    supplies = [20, 0, 0, -5, -15, 0]
    
    all_arcs = smcf.add_arcs_with_capacity_and_unit_cost(
        start_nodes, end_nodes, capacities, unit_costs
    )
    for i in range(len(start_nodes)):
        smcf.add_arcs_with_capacity_and_unit_cost(start_nodes[i], end_nodes[i], capacities[i], unit_costs[i])

    # Add supply for each node.
    for i, supply in enumerate(supplies):
        smcf.set_nodes_supplies(i, supply)

    # Find the min cost flow.
    status = smcf.solve()

    if status != smcf.OPTIMAL:
        print("There was an issue with the min cost flow input.")
        print(f"Status: {status}")
        exit(1)

    # Print results.
    print("Minimum cost:", smcf.optimal_cost())
    print("Flow:")
    for i in range(smcf.num_arcs()):
        print(f"From node {smcf.tail(i)} to node {smcf.head(i)}: flow {smcf.flow(i)} / capacity {smcf.capacity(i)}")

if __name__ == "__main__":
    main()