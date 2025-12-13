from queue import Queue
from Sequence import Sequence

class Organizer:
    def __init__(self):
        self.temp_seq = 0
        self.start_seq = 0 #dachte ist einfach nett so
        self.queue : Queue[Sequence] = Queue()

    def append(self, new_sequence : Sequence):
        self.queue.put(new_sequence)
        self.temp_seq += 1

    def set_start_seq(self):
        self.start_seq = self.temp_seq

    def pull_first(self):
        self.queue.get()
        self.temp_seq -= 1

    def get_temp_seq(self):
        return self.temp_seq
    
    def get_start_seq(self):
        return self.start_seq
    
    def get_queue(self):
        return self.queue