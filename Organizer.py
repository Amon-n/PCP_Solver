from queue import Queue
from Sequence import Sequence

class Organizer:
    def __init__(self):
        self.temp_opt = 0
        self.start_opt = 0 #dachte ist einfach nett so
        self.queue : Queue[Sequence] = Queue()

    def append(self, new_sequence : Sequence):
        self.queue.put(new_sequence)
        self.temp_opt += 1

    def pull_first(self):
        self.queue.get()
        self.temp_opt -= 1