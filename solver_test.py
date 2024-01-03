import solver


def is_solved():
    assert not solver.solver()


def test_solver():
    assert solver.solver() == 42
