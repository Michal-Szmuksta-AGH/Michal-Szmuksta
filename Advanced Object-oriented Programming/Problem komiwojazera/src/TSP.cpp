#include "TSP.hpp"

#include <algorithm>
#include <stack>
#include <optional>

std::ostream &operator<<(std::ostream &os, const CostMatrix &cm) {
    for (std::size_t r = 0; r < cm.size(); ++r) {
        for (std::size_t c = 0; c < cm.size(); ++c) {
            const auto &elem = cm[r][c];
            os << (is_inf(elem) ? "INF" : std::to_string(elem)) << " ";
        }
        os << "\n";
    }
    os << std::endl;

    return os;
}

/* PART 1 */

/**
 * Create path from unsorted path and last 2x2 cost matrix.
 * @return The vector of consecutive vertex.
 */
path_t StageState::get_path() {
    for (size_t i = 0; i < matrix_.size(); i++) {
        for (size_t j = 0; j < matrix_.size(); j++) {
            if (matrix_[i][j] != INF) {
                vertex_t vertex(i, j);
                append_to_path(vertex);
                matrix_[i][j] = INF;
                matrix_[j][i] = INF;
            }
        }
    }
    path_t path;
    path.push_back(unsorted_path_[0].col);
    for (size_t i = 1; i < matrix_.size(); i++) {
        for (auto &edge: unsorted_path_) {
            if (edge.row == path.back()) {
                path.push_back(edge.col);
                break;
            }
        }
    }
    for (auto &vertex: path) {
        vertex++;
    }
    return path;
    // TODO: Implement it! DONE !!!
}

/**
 * Get minimum values from each row and returns them.
 * @return Vector of minimum values in row.
 */
std::vector<cost_t> CostMatrix::get_min_values_in_rows() const {
    cost_matrix_t matrix = get_matrix();
    std::vector<cost_t> min_values_in_rows_vector;
    for (auto &row: matrix) {
        cost_t min_value = *std::min_element(row.begin(), row.end());
        if (min_value != INF) {
            min_values_in_rows_vector.push_back(min_value);
        } else {
            min_values_in_rows_vector.push_back(0);
        }
    }
    return min_values_in_rows_vector;
    // TODO: Implement it! DONE!
}

/**
 * Reduce rows so that in each row at least one zero value is present.
 * @return Sum of values reduced in rows.
 */
cost_t CostMatrix::reduce_rows() {
    std::vector<cost_t> min_values_in_rows_vector = get_min_values_in_rows();
    for (size_t i = 0; i < matrix_.size(); i++) {
        for (size_t j = 0; j < matrix_.size(); j++) {
            if (matrix_[i][j] != INF) {
                matrix_[i][j] -= min_values_in_rows_vector[i];
            }
        }
    }
    return std::accumulate(min_values_in_rows_vector.begin(), min_values_in_rows_vector.end(), 0);
    // TODO: Implement it! DONE!
}

/**
 * Get minimum values from each column and returns them.
 * @return Vector of minimum values in columns.
 */
std::vector<cost_t> CostMatrix::get_min_values_in_cols() const {
    std::vector<cost_t> min_values_in_cols_vector;
    cost_matrix_t transposed_matrix = get_matrix();
    cost_matrix_t matrix = get_matrix();
    for (size_t i = 0; i < matrix.size(); i++) {
        for (size_t j = 0; j < matrix.size(); j++) {
            transposed_matrix[j][i] = matrix[i][j];
        }
    }
    for (auto &column: transposed_matrix) {
        cost_t min_value = *std::min_element(column.begin(), column.end());
        if (min_value != INF) {
            min_values_in_cols_vector.push_back(min_value);
        } else {
            min_values_in_cols_vector.push_back(0);
        }
    }
    return min_values_in_cols_vector;
    // TODO: Implement it! DONE!
}

/**
 * Reduces rows so that in each column at least one zero value is present.
 * @return Sum of values reduced in columns.
 */
cost_t CostMatrix::reduce_cols() {
    std::vector<cost_t> min_values_in_cols_vector = get_min_values_in_cols();
    for (size_t i = 0; i < matrix_.size(); i++) {
        for (size_t j = 0; j < matrix_.size(); j++) {
            if (matrix_[j][i] != INF) {
                matrix_[j][i] -= min_values_in_cols_vector[i];
            }
        }
    }
    return std::accumulate(min_values_in_cols_vector.begin(), min_values_in_cols_vector.end(), 0);
    // TODO: Implement it! DONE!
}

/**
 * Get the cost of not visiting the vertex_t (@see: get_new_vertex())
 * @param row
 * @param col
 * @return The sum of minimal values in row and col, excluding the intersection value.
 */
cost_t CostMatrix::get_vertex_cost(std::size_t row, std::size_t col) const {
    cost_matrix_t matrix = get_matrix();
    size_t size = matrix.size();
    cost_t Min_row = INF;
    for (size_t i = 0; i < size; i++) {
        if (matrix[row][i] < Min_row && i != col) {
            Min_row = matrix[row][i];
        }
    }
    cost_t Min_col = INF;
    for (size_t i = 0; i < size; i++) {
        if (matrix[i][col] < Min_col && i != row) {
            Min_col = matrix[i][col];
        }
    }
    return Min_row + Min_col;
    // TODO: Implement it! DONE!
}

/* PART 2 */

/**
 * Choose next vertex to visit:
 * - Look for vertex_t (pair row and column) with value 0 in the current cost matrix.
 * - Get the vertex_t cost (calls get_vertex_cost()).
 * - Choose the vertex_t with maximum cost and returns it.
 * @param cm
 * @return The coordinates of the next vertex.
 */
NewVertex StageState::choose_new_vertex() {
    size_t row_coordinate = 0, col_coordinate = 0;
    cost_t cost, max_cost = 0;
    size_t size = matrix_.size();
    for (size_t i = 0; i < size; i++) {
        for (size_t j = 0; j < size; j++) {
            if (matrix_[i][j] == 0) {
                cost = matrix_.get_vertex_cost(i, j);
                if (cost > max_cost) {
                    max_cost = cost;
                    row_coordinate = i;
                    col_coordinate = j;
                }
            }
        }
    }
    vertex_t Coordinates(row_coordinate, col_coordinate);
    NewVertex Vertex(Coordinates, max_cost);
    return Vertex;
    // TODO: Implement it! DONE!
}

/**
 * Update the cost matrix with the new vertex.
 * @param new_vertex
 */
void StageState::update_cost_matrix(vertex_t new_vertex) {
    size_t size = matrix_.size();
    for (size_t i = 0; i < size; i++) {
        for (size_t j = 0; j < size; j++) {
            if (i == new_vertex.row || j == new_vertex.col) {
                matrix_[i][j] = INF;
            }
        }
    }
    matrix_[new_vertex.col][new_vertex.row] = INF;
    for (size_t i = 0; i < unsorted_path_.size(); i++) {
        path_t path_tmp;
        path_tmp.push_back(unsorted_path_[i].row);
        path_tmp.push_back(unsorted_path_[i].col);
        for (size_t j = 0; j < unsorted_path_.size(); j++) {
            if (path_tmp.front() == unsorted_path_[j].col) {
                path_tmp.insert(std::begin(path_tmp), unsorted_path_[j].col);
                path_tmp.insert(std::begin(path_tmp), unsorted_path_[j].row);
                matrix_[path_tmp[0]][path_tmp.back()] = INF;
                matrix_[path_tmp.back()][path_tmp[0]] = INF;
            }
            if (path_tmp.back() == unsorted_path_[j].row) {
                path_tmp.push_back(unsorted_path_[j].row);
                path_tmp.push_back(unsorted_path_[j].col);
                matrix_[path_tmp[0]][path_tmp.back()] = INF;
                matrix_[path_tmp.back()][path_tmp[0]] = INF;
            }
        }
    }
    // TODO: Implement it! DONE !!!
}

/**
 * Reduce the cost matrix.
 * @return The sum of reduced values.
 */
cost_t StageState::reduce_cost_matrix() {
    return matrix_.reduce_rows() + matrix_.reduce_cols();
    // TODO: Implement it! DONE!
}

/**
 * Given the optimal path, return the optimal cost.
 * @param optimal_path
 * @param m
 * @return Cost of the path.
 */
cost_t get_optimal_cost(const path_t &optimal_path, const cost_matrix_t &m) {
    cost_t cost = 0;

    for (std::size_t idx = 1; idx < optimal_path.size(); ++idx) {
        cost += m[optimal_path[idx - 1] - 1][optimal_path[idx] - 1];
    }

    // Add the cost of returning from the last city to the initial one.
    cost += m[optimal_path[optimal_path.size() - 1] - 1][optimal_path[0] - 1];

    return cost;
}

/**
 * Create the right branch matrix with the chosen vertex forbidden and the new lower bound.
 * @param m
 * @param v
 * @param lb
 * @return New branch.
 */
StageState create_right_branch_matrix(cost_matrix_t m, vertex_t v, cost_t lb) {
    CostMatrix cm(m);
    cm[v.row][v.col] = INF;
    return StageState(cm, {}, lb);
}

/**
 * Retain only optimal ones (from all possible ones).
 * @param solutions
 * @return Vector of optimal solutions.
 */
tsp_solutions_t filter_solutions(tsp_solutions_t solutions) {
    cost_t optimal_cost = INF;
    for (const auto &s: solutions) {
        optimal_cost = (s.lower_bound < optimal_cost) ? s.lower_bound : optimal_cost;
    }

    tsp_solutions_t optimal_solutions;
    std::copy_if(solutions.begin(), solutions.end(),
                 std::back_inserter(optimal_solutions),
                 [&optimal_cost](const tsp_solution_t &s) { return s.lower_bound == optimal_cost; }
    );

    return optimal_solutions;
}

/**
 * Solve the TSP.
 * @param cm The cost matrix.
 * @return A list of optimal solutions.
 */
tsp_solutions_t solve_tsp(const cost_matrix_t &cm) {

    StageState left_branch(cm);

    // The branch & bound tree.
    std::stack<StageState> tree_lifo;

    // The number of levels determines the number of steps before obtaining
    // a 2x2 matrix.
    std::size_t n_levels = cm.size() - 2;

    tree_lifo.push(left_branch);   // Use the first cost matrix as the root.

    cost_t best_lb = INF;
    tsp_solutions_t solutions;

    while (!tree_lifo.empty()) {

        left_branch = tree_lifo.top();
        tree_lifo.pop();

        while (left_branch.get_level() != n_levels && left_branch.get_lower_bound() <= best_lb) {
            // Repeat until a 2x2 matrix is obtained or the lower bound is too high...

            if (left_branch.get_level() == 0) {
                left_branch.reset_lower_bound();
            }

            // 1. Reduce the matrix in rows and columns.
            cost_t new_cost = left_branch.reduce_cost_matrix();; // @TODO (KROK 1) DONE!


            // 2. Update the lower bound and check the break condition.
            left_branch.update_lower_bound(new_cost);
            if (left_branch.get_lower_bound() > best_lb) {
                break;
            }

            // 3. Get new vertex and the cost of not choosing it.
            NewVertex new_vertex = left_branch.choose_new_vertex(); // @TODO (KROK 2) DONE!

            // 4. @TODO Update the path - use append_to_path method. DONE!
            left_branch.append_to_path(new_vertex.coordinates);

            // 5. @TODO (KROK 3) Update the cost matrix of the left branch. DONE!
            left_branch.update_cost_matrix(new_vertex.coordinates);

            // 6. Update the right branch and push it to the LIFO.
            cost_t new_lower_bound = left_branch.get_lower_bound() + new_vertex.cost;
            tree_lifo.push(create_right_branch_matrix(cm, new_vertex.coordinates,
                                                      new_lower_bound));
        }

        if (left_branch.get_lower_bound() <= best_lb) {
            // If the new solution is at least as good as the previous one,
            // save its lower bound and its path.
            best_lb = left_branch.get_lower_bound();
            path_t new_path = left_branch.get_path();
            solutions.push_back({get_optimal_cost(new_path, cm), new_path});
        }
    }

    return filter_solutions(solutions); // Filter solutions to find only optimal ones.
}
