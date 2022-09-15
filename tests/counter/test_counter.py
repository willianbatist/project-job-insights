from src.counter import count_ocurrences


def test_counter():
    result = count_ocurrences("src/jobs.csv", "National Debt Relief")
    assert(result == 413)
