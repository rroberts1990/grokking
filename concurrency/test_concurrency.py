import pytest
from concurrency.concurrency import *
import time

@pytest.fixture
def sites():
    return  [
                "https://www.jython.org",
                "http://olympus.realpython.org/dice",
            ] * 80

def test_non_concurrent(sites):
    requester = NonConcurrentRequest(sites)
    start_time = time.time()
    requester.download_all_sites()
    duration = time.time() - start_time
    print(duration)

def test_concurrent(sites):
    requester = ConcurrentRequest(sites)
    start_time = time.time()
    requester.download_all_sites()
    duration = time.time() - start_time
    print(duration)

def test_async(sites):
    requester = AsyncRequest(sites)
    start_time = time.time()
    requester.run()
    duration = time.time() - start_time
    print(duration)

def test_multi(sites):
    requester = MultiprocessingRequest(sites)
    start_time = time.time()
    requester.download_all_sites()
    duration = time.time() - start_time
    print(duration)

def test_cpu_synchronous():
    cpu = CpuBound([5_000_000 + x for x in range(20)])
    start_time = time.time()
    cpu.find_sums()
    duration = start_time - time.time()
    print(f"\nDuration {duration} second")

def test_cpu_multi():
    cpu = CpuBoundMultiprocessing([5_000_000 + x for x in range(20)])
    start_time = time.time()
    cpu.find_sums()
    duration = start_time - time.time()
    print(f"\nDuration {duration} second")