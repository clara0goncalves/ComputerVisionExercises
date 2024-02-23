# The objective is to minimize the sum of squared distances from a point x to a set of lines li.
# The squared distance for each line li can be written as (x · li)^2.
# The total sum of squared distances D is given by Equation (2.120):
# D = Σ_i (x · li)^2

# 1. Write the Dot Product:
#    - Express the dot product x · li as x^T li.
# D = Σ_i (x^T li)^2

# 2. Expand the Squared Term:
#    - Expand the squared term (x^T li)^2 to get a quadratic form.
# D = Σ_i (x^T li li^T x)

# 3. Combine the Sum:
#    - Combine the sum to represent the entire expression in matrix form.
# D = x^T (Σ_i li li^T) x

#    - Let A = Σ_i li li^T. Now, D = x^T A x.

# 4. Minimize the Quadratic Form:
#    - To minimize D, set the derivative of D with respect to x equal to zero and solve for x.
# (∂D/∂x) = 2Ax = 0

#    - Solve the system of equations Ax = 0 to find the point x.
