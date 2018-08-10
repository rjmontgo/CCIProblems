from problem_1 import mixBits

def test_small_mask():
    app = 2 # 10
    source = 8 # 1010
    start = 1
    end = 2

    assert mixBits(app, source, start, end) == 12

def test_large_mask():
    app = 5 # 101
    source = 754 # 1011110010  1011110110
    start = 2 #
    end = 4

    assert mixBits(app, source, start, end) == 758
