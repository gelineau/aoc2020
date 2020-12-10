from collections import Counter

from d10 import calculate_differences, count_arrangements


def test_differences():
    input = [
        28,
        33,
        18,
        42,
        31,
        14,
        46,
        20,
        48,
        47,
        24,
        23,
        49,
        45,
        19,
        38,
        39,
        11,
        1,
        32,
        25,
        35,
        8,
        17,
        7,
        9,
        4,
        2,
        34,
        10,
        3,
    ]

    differences = calculate_differences(input)

    assert differences == Counter({1: 22, 3: 9})


def test_arrangements():
    input = [
        28,
        33,
        18,
        42,
        31,
        14,
        46,
        20,
        48,
        47,
        24,
        23,
        49,
        45,
        19,
        38,
        39,
        11,
        1,
        32,
        25,
        35,
        8,
        17,
        7,
        9,
        4,
        2,
        34,
        10,
        3,
    ]

    input = sorted(input)
    input.append(input[-1] + 3)
    arrangements = count_arrangements(0, tuple(input))
    assert arrangements == 19208

def test_arrangements_small_set():
        input = [
            16,
            10,
            15,
            5,
            1,
            11,
            7,
            19,
            6,
            12,
            4,
        ]

        input = sorted(input)
        input.append(input[-1] + 3)
        arrangements = count_arrangements(0, tuple(input))
        assert arrangements == 8