from pipeline import extract, transform, load


def test_extract_len():
    assert len(extract(5)) == 5


def test_transform_drops_zero():
    assert transform([{"id": 0, "amount": 0}]) == []


def test_load_returns_count():
    assert load([{"id": 1, "amount": 10}]) == 1
