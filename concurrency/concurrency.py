import requests
import threading
import concurrent.futures
import asyncio
import aiohttp
import multiprocessing

class NonConcurrentRequest:
    def __init__(self, sites):
        self.sites = sites

    def download_site(self, url, session):
        with session.get(url) as response:
            print(f"Read {len(response.content)} from {url}")

    def download_all_sites(self):
        with requests.Session() as session:
            for url in self.sites:
                self.download_site(url, session)


class ConcurrentRequest:
    def __init__(self, sites):
        self.sites = sites
        self.thread_local = threading.local()

    def get_session(self):
        if not hasattr(self.thread_local, "session"):
            self.thread_local.session = requests.Session()
        return self.thread_local.session

    def download_site(self, url):
        session = self.get_session()
        with session.get(url) as response:
            print(f"Read {len(response.content)} from {url}")

    def download_all_sites(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(self.download_site, self.sites)


class AsyncRequest:
    def __init__(self, sites):
        self.sites = sites

    async def download_site(self, session, url):
        async with session.get(url) as response:
            print("Read {0} from {1}".format(response.content_length, url))

    async def download_all_sites(self):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for url in self.sites:
                task = asyncio.ensure_future(self.download_site(session, url))
                tasks.append(task)
            await asyncio.gather(*tasks, return_exceptions=True)

    async def run(self):
        asyncio.get_event_loop().run_until_complete(self.download_all_sites())


class MultiprocessingRequest:
    session = None
    def __init__(self, sites):
        self.sites = sites

    def set_global_session(self):
        global session
        if not session:
            session = requests.Session()

    def download_site(self, url):
        with session.get(url) as response:
            name = multiprocessing.current_process().name
            print(f"{name}:Read {len(response.content)} from {url}")

    def download_all_sites(self):
        with multiprocessing.Pool(initializer=self.set_global_session) as pool:
            pool.map(self.download_site, self.sites)


class CpuBound:
    def __init__(self, numbers):
        self.numbers = numbers

    def cpu_bound(self, number):
        return sum(i*i for i in range(number))

    def find_sums(self):
        for number in self.numbers:
            self.cpu_bound(number)


class CpuBoundMultiprocessing(CpuBound):
    def find_sums(self):
        with multiprocessing.Pool() as pool:
            pool.map(self.cpu_bound, self.numbers)