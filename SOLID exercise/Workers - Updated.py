from abc import abstractmethod, ABC
import time


class AbstractWorker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class Worker(AbstractWorker):
    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(AbstractWorker):
    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Manager:
    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        try:
            assert isinstance(worker, Worker), f"`worker` must be of type {Worker}"
        except:
            pass
        try:
            assert isinstance(worker, SuperWorker), f"`worker` must be of type {SuperWorker}"
        except:
            pass
        try:
            assert isinstance(worker, Robot), f"`worker` must be of type {Robot}"
        except:
            pass
        self.worker = worker

    def manage(self):
        self.worker.work()

    def lunch_break(self):
        if self.worker.__class__.__name__ == "Robot":
            print(f'The Robot cannot have a lunch break, because he cannot eat lunch...')
            return
        self.worker.eat()


class Robot:
    @staticmethod
    def work():
        print("I'm a robot. I'm working....")
