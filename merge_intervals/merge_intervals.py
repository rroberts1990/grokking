from typing import List
from heapq import *


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"Interval({self.start}, {self.end})"

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.end <= other.end

class CpuJob:
    def __init__(self, start, end, load):
        self.start = start
        self.end = end
        self.load = load

    def __lt__(self, other):
        return self.end <= other.end

class EmployeeInterval:
    def __init__(self, interval, employee_index, interval_index):
        self.interval = interval
        self.employee_index = employee_index
        self.interval_index = interval_index

    def __lt__(self, other):
        return self.interval.start < other.interval.start


class MergeIntervals:

    def merge_intervals(self, intervals: List[Interval]):
        if len(intervals) < 2:
            return intervals

        intervals.sort(key= lambda x: x.start)

        merged_intervals = []
        start = intervals[0].start
        end = intervals[0].end

        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval.start <= end:
                end = max(interval.end, end)
            else:
                merged_intervals.append(Interval(start, end))
                start = interval.start
                end = interval.end
        merged_intervals.append(Interval(start, end))
        return merged_intervals

    def insert_interval(self, intervals, new_interval):
        merged_intervals = []
        i = 0
        while i < len(intervals) and intervals[i].end < new_interval.start:
            merged_intervals.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i].start <= new_interval.end:
            new_interval.start = min(intervals[i].start, new_interval.start)
            new_interval.end = max(intervals[i].end, new_interval.end)
            i += 1

        merged_intervals.append(new_interval)
        while i < len(intervals):
            merged_intervals.append(intervals[i])
            i += 1
        return merged_intervals


    def intervals_intersection(self, intervals_a, intervals_b):
        intersecting_intervals = []
        i, j = 0, 0

        while i < len(intervals_a) and j < len(intervals_b):
            a_overlaps_b = intervals_b[j].start <= intervals_a[i].start <= intervals_b[j].end
            b_overlaps_a = intervals_a[i].start <= intervals_b[j].start <= intervals_a[i].end

            if a_overlaps_b or b_overlaps_a:
                intersect = Interval(max(intervals_a[i].start, intervals_b[j].start), min(intervals_a[i].end, intervals_b[j].end))
                intersecting_intervals.append(intersect)
            if intervals_a[i].end < intervals_b[j].end:
                i += 1
            else:
                j += 1
        return intersecting_intervals


    def conflicting_appointments(self, appointments):
        appointments.sort(key = lambda x: x.start)
        start, end = appointments[0].start, appointments[0].end
        for i in range(1, len(appointments)):
            if start <= appointments[i].start <= end:
                return False
            elif appointments[i].start <= start <= appointments[i].end:
                return False
            i += 1
        return True

    def min_meeting_rooms(self, meetings):
        meetings.sort(key=lambda x: x.start)

        min_rooms = 0
        min_heap = []

        for meeting in meetings:
            while len(min_heap) > 0 and meeting.start >= min_heap[0].end:
                heappop(min_heap)
            heappush(min_heap, meeting)
            min_rooms = max(min_rooms, len(min_heap))
        return min_rooms

    def max_cpu_load(self, jobs):
        jobs.sort(key=lambda x: x.start)
        min_heap = []
        max_load = 0
        current_load = 0

        for job in jobs:
            while len(min_heap) > 0 and job.start >= min_heap[0].end:
                current_load -= min_heap[0].load
                heappop(min_heap)
            heappush(min_heap, job)
            current_load += job.load
            max_load = max(max_load, current_load)

        return max_load

    def employee_free_time(self, shifts):
        if shifts is None:
            return []

        n = len(shifts)
        min_heap = []
        result = []

        for i in range(n):
            heappush(min_heap, EmployeeInterval(shifts[i][0], i, 0))

        previous_interval = min_heap[0].interval

        while min_heap:
            queue_top = heappop(min_heap)

            if previous_interval.end < queue_top.interval.start:
                result.append(Interval(previous_interval.end, queue_top.interval.start))
                previous_interval = queue_top.interval
            else:
                if previous_interval.end < queue_top.interval.end:
                    previous_interval = queue_top.interval

            employee_shifts = shifts[queue_top.employee_index]
            if len(employee_shifts) > queue_top.interval_index + 1:
                heappush(min_heap, EmployeeInterval(employee_shifts[queue_top.interval_index + 1], queue_top.employee_index, queue_top.interval_index + 1))

        return result