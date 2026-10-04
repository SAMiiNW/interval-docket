import ast
from pathlib import Path

SOURCE = (Path(__file__).parents[1] / 'contracts' / 'contract.py').read_text()
TREE = ast.parse(SOURCE)
def load(name):
    node = next(x for x in TREE.body if isinstance(x, ast.FunctionDef) and x.name == name)
    scope = {}; exec(compile(ast.Module(body=[node], type_ignores=[]), '<contract>', 'exec'), scope); return scope[name]

def test_chronology_has_three_distinct_outcomes():
    classify = load('chronology_state')
    assert classify([[1, 1], [3, 3]], [[0, 1]]) == 'CONSISTENT'
    assert classify([[1, 4], [3, 6]], [[0, 1]]) == 'UNRESOLVED'
    assert classify([[6, 7], [3, 5]], [[0, 1]]) == 'IMPOSSIBLE'

def test_multi_edge_overlap_and_violation():
    classify = load('chronology_state')
    assert classify([[1, 1], [2, 4], [4, 5]], [[0, 1], [1, 2]]) == 'UNRESOLVED'
    assert classify([[1, 1], [7, 8], [4, 6]], [[0, 1], [1, 2]]) == 'IMPOSSIBLE'

def test_consensus_and_attribution_surface():
    assert 'prompt_comparative' in SOURCE
    assert 'every interval endpoint, citation index, and source digest must match exactly' in SOURCE
    assert 'every event requires source attribution' in SOURCE
    assert 'distinct source origins required' in SOURCE
    for method in ('open_docket', 'reconstruct', 'get_docket'): assert f'def {method}' in SOURCE
