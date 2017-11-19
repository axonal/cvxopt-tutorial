from cvxopt import matrix, solvers


def solve_chicken(solver=None):
    c = matrix([1., 1., 1., 1.])
    G = matrix([[1., 1., 0., 0.], [-2., 0., 0., -1.], [0., -2., -1., 0.],
                [0., 0., -2., -2.]])
    h = matrix([0., 0., 0., 0.])

    A = matrix([[1.], [1.], [1.], [1.]])
    b = matrix(1.)

    return solvers.lp(c, G, h, A, b, solver=solver)


if __name__ == '__main__':
    # suppress output
    solvers.options['show_progress'] = False
    solvers.options['glpk'] = {'LPX_K_MSGLEV': 0, 'msg_lev': "GLP_MSG_OFF"}

    print("objective = {}".format(solve_chicken('glpk')['primal objective']))
    print("x = {}".format(solve_chicken('glpk')['x']))
