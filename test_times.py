from times import compute_overlap_time, time_range

def test_generic_case():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)

    # since only only overlap is in short, result should equal short
    assert result == short

def test_no_overlap():
    # tests if the function returns empty when there is no overlap
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 12:30:00", "2010-01-12 12:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = []

    assert result == expected

def test_overlap_at_start():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 09:30:00", "2010-01-12 10:30:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = time_range('2010-01-12 10:00:00', '2010-01-12 10:30:00')

    assert result == expected

def test_overlap_at_end():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 11:30:00", "2010-01-12 12:30:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 11:30:00', '2010-01-12 12:00:00')]

    assert result == expected
