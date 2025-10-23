from algorithms.searching.linear_search import linear_search

def test_linear_search():
    assert linear_search([10, 23, 45, 70, 11, 15], 70) == 3
    assert linear_search([1, 2, 3, 4], 2) == 1
    assert linear_search([1, 2, 3, 4], 5) == -1
    assert linear_search([], 1) == -1