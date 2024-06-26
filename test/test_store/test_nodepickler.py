import pickle

from rdflib.store import NodePickler
from rdflib.term import Literal

# same as nt/more_literals.nt
cases = [
    "no quotes",
    "single ' quote",
    'double " quote',
    'triple """ quotes',
    'mixed "\'""" quotes',
    '"',
    "'",
    '"\'"',
    "\\",  # len 1
    '\\"',  # len 2
    '\\\\"',  # len 3
    '\\"\\',  # len 3
    '<a some="typical" html="content">here</a>',
]


class TestUtil:
    def test_to_bits_from_bits_round_trip(self):
        np = NodePickler()

        a = Literal(
            """A test with a \\n (backslash n), "\u00a9" , and newline \n and a second line.
"""
        )
        b = np.loads(np.dumps(a))
        assert a == b

    def test_literal_cases(self):
        np = NodePickler()

        for l in cases:  # noqa: E741
            a = Literal(l)
            b = np.loads(np.dumps(a))
            assert a == b

    def test_pickle(self):
        np = NodePickler()
        dump = pickle.dumps(np)
        np2 = pickle.loads(dump)
        assert np._ids == np2._ids
        assert np._objects == np2._objects
