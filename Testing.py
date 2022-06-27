def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx

import random

class TestDataEmptyArray(object):
    @staticmethod
    def get_array():
        return []

class TestDataUniqueValues(object):
    @staticmethod
    def get_array():
        TestDataUniqueValues.l1=random.sample(range(0,200), random.randint(2,100))
        return TestDataUniqueValues.l1

    @staticmethod
    def get_expected_result():
        index = 0
        for i in TestDataUniqueValues.l1:
            if i == min(TestDataUniqueValues.l1):
                return index
            index+=1

class TestDataExactlyTwoDifferentMinimums(object):
    @staticmethod
    def get_array():
        TestDataExactlyTwoDifferentMinimums.l2 = random.sample(range(0,200), random.randint(2,100))
        TestDataExactlyTwoDifferentMinimums.l2.insert(random.randint(0,len(TestDataExactlyTwoDifferentMinimums.l2)), min(TestDataExactlyTwoDifferentMinimums.l2))
        return TestDataExactlyTwoDifferentMinimums.l2

    @staticmethod
    def get_expected_result():
        index = 0
        for i in TestDataExactlyTwoDifferentMinimums.l2:
            if i == min(TestDataExactlyTwoDifferentMinimums.l2):
                return index
            index+=1

def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False


def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

TestWithEmptyArray()
TestWithUniqueValues()
TestiWithExactyTwoDifferentMinimums()
print("OK")
