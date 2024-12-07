

Define Variables: Each covered tile (initially all tiles are covered).
Define Domains: {Mine, Safe} for each tile.
Define Constraints: For each revealed tile (with number `N`), the sum of mines in its adjacent tiles = `N`.


function MinesweeperCSP(grid):
    # Parse the grid
    revealedTiles = findAllRevealedTiles(grid)
    coveredTiles = findAllCoveredTiles(grid)

    # Initialize the CSP
    variables = coveredTiles
    domains = {tile: {Mine, Safe} for tile in coveredTiles}
    constraints = generateConstraints(grid, revealedTiles)

    # Backtracking Search
    assignment = backtrack({}, variables, domains, constraints)
    if assignment is not None:
        return assignment
    else:
        return "No solution found"

function backtrack(assignment, variables, domains, constraints):
    if all variables are assigned:
        return assignment

    variable = selectUnassignedVariable(variables, assignment)
    for value in orderDomainValues(variable, domains, assignment):
        if isConsistent(value, variable, assignment, constraints):
            assignment[variable] = value
            result = backtrack(assignment, variables, domains, constraints)
            if result is not failure:
                return result
            del assignment[variable]
    return failure

function generateConstraints(grid, revealedTiles):
    constraints = []
    for tile in revealedTiles:
        N = grid[tile.row][tile.column]
        neighbors = `getNeighbors`(tile)
        constraint = (sum(value == Mine for value in neighbors) == N)
        constraints.append(constraint)
    return constraints


function selectUnassignedVariable(variables, assignment):
    return first variable in variables not in assignment
    # Optionally use MRV (Minimum Remaining Values) for optimization

function orderDomainValues(variable, domains, assignment):
    return list of values in domains[variable]
    # Optionally use least-constraining value heuristic

function isConsistent(value, variable, assignment, constraints):
    for constraint in constraints involving variable:
        if constraint is violated with assignment[variable] = value:
            return false
    return true

function getNeighbors(tile):
    return list of all adjacent tiles within bounds