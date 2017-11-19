from cvxopt import matrix, solvers


def solve_clrs(solver=None):
    c = matrix([-1., -1.])
    G = matrix([[4., 2., -5.], [-1., 1., 2.]])
    h = matrix([8., 10., 2.])

    return solvers.lp(c, G, h, solver=solver)


if __name__ == '__main__':
    # suppress output
    solvers.options['show_progress'] = False
    solvers.options['glpk'] = {'LPX_K_MSGLEV': 0, 'msg_lev': "GLP_MSG_OFF"}

    print("objective = {}".format(solve_clrs()['primal objective']))
    print("x = {}".format(solve_clrs()['x']))

    print("objective = {}".format(solve_clrs('glpk')['primal objective']))
    print("x = {}".format(solve_clrs('glpk')['x']))
