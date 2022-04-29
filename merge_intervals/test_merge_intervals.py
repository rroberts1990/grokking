import pytest
from merge_intervals.merge_intervals import MergeIntervals, Interval, Meeting, CpuJob
from typing import List

def interval_factory(intervals: List[List]) -> List[Interval]:
    return [Interval(*interval) for interval in intervals]

def meeting_factory(intervals: List[List]) -> List[Meeting]:
    return [Meeting(*interval) for interval in intervals]\

def cpu_factory(intervals: List[List]) -> List[CpuJob]:
    return [CpuJob(*job) for job in intervals]

@pytest.mark.parametrize('input, expected',
                         [(interval_factory([[1,4], [2,5], [7,9]]), interval_factory([[1,5], [7,9]])),
                          (interval_factory([[6,7], [2,4], [5,9]]), interval_factory([[2,4], [5,9]])),
                          (interval_factory([[1,4], [2,6], [3,5]]), interval_factory([[1, 6]]))])
def test_merge_intervals(input, expected):
    solver = MergeIntervals()
    actual = solver.merge_intervals(input)
    assert actual == expected


@pytest.mark.parametrize('intervals, new_interval, expected',
                         [(interval_factory([[1,3], [5,7], [8,12]]), Interval(4, 6), interval_factory([[1,3], [4,7], [8,12]])),
                          (interval_factory([[1,3], [5,7], [8,12]]), Interval(4, 10), interval_factory([[1,3], [4,12]])),
                          (interval_factory([[2,3],[5,7]]), Interval(1, 4), interval_factory([[1,4], [5,7]]))])
def test_insert_interval(intervals, new_interval, expected):
    solver = MergeIntervals()
    actual = solver.insert_interval(intervals, new_interval)
    assert actual == expected


@pytest.mark.parametrize('intervals_a, intervals_b, expected',
                         [(interval_factory([[1, 3], [5, 6], [7, 9]]), interval_factory([[2, 3], [5, 7]]), interval_factory([[2, 3], [5, 6], [7, 7]])),
                          (interval_factory([[1, 3], [5, 7], [9, 12]]), interval_factory([[5, 10]]), interval_factory([[5, 7], [9, 10]]))])
def test_intervals_intersection(intervals_a, intervals_b, expected):
    solver = MergeIntervals()
    actual = solver.intervals_intersection(intervals_a, intervals_b)
    assert actual == expected


@pytest.mark.parametrize('appointments, expected',
                         [(interval_factory([[1,4], [2,5], [7,9]]), False),
                          (interval_factory([[6,7], [2,4], [8,12]]), True),
                          (interval_factory([[4,5], [2,3], [3,6]]), False)])
def test_conflicting_appointments(appointments, expected):
    solver = MergeIntervals()
    actual = solver.conflicting_appointments(appointments)
    assert actual == expected


@pytest.mark.parametrize('meetings, expected',
                         [(meeting_factory([[1,4], [2,5], [7,9]]), 2),
                          (meeting_factory([[6,7], [2,4], [8,12]]), 1),
                          (meeting_factory([[1,4], [2,3], [3,6]]), 2),
                          (meeting_factory([[4,5], [2,3], [2,4], [3,5]]), 2)])
def test_min_meeting_rooms(meetings, expected):
    solver = MergeIntervals()
    actual = solver.min_meeting_rooms(meetings)
    assert actual == expected

@pytest.mark.parametrize('cpu_jobs, expected',
                         [(cpu_factory([[1,4,3], [2,5,4], [7,9,6]]), 7),
                          (cpu_factory([[6,7,10], [2,4,11], [8,12,15]]), 15),
                          (cpu_factory([[1,4,2], [2,4,1], [3,6,5]]), 8)])
def test_max_cpu_load(cpu_jobs, expected):
    solver = MergeIntervals()
    actual = solver.max_cpu_load(cpu_jobs)
    assert actual == expected


@pytest.mark.parametrize('shifts, expected',
                         [([[Interval(1,3), Interval(5,6)], [Interval(2,3), Interval(6,8)]], [Interval(3,5)]),
                          ([[Interval(1,3), Interval(9,12)], [Interval(2,4)], [Interval(6,8)]], interval_factory([[4,6], [8,9]])),
                          ([[Interval(1,3)], [Interval(2,4)], [Interval(3,5), Interval(7,9)]], [Interval(5,7)])])
def test_employee_free_time(shifts, expected):
    solver = MergeIntervals()
    actual = solver.employee_free_time(shifts)
    assert actual == expected
