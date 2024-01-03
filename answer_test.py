import answer


def is_answered():
    assert not answer.answer()


def test_answer():
    assert answer.answer() == 42
