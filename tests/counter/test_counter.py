from src.counter import count_ocurrences


def test_counter():
    result = count_ocurrences("src/jobs.csv", "ASPCA")
    assert(result == 59)
