from queue import Queue
from Sequence import Sequence

class Organizer:
    def __init__(self):
        self.temp_seq = 0
        self.start_seq = 0 #dachte ist einfach nett so
        self.queue : Queue[Sequence] = Queue()
        self.missing_tuples : set[tuple[bool, str]] = set()

    def append(self, new_sequence : Sequence):
        sequence_missing : tuple[bool, str] = (new_sequence.more_in_first, new_sequence.missing)
        if sequence_missing not in self.missing_tuples:
            self.missing_tuples.add(sequence_missing)
            self.queue.put(new_sequence)
            self.temp_seq += 1
            return

    def set_start_seq(self):
        self.start_seq = self.temp_seq

    def pull_first(self):
        self.temp_seq -= 1
        return self.queue.get()

    def get_temp_seq(self):
        return self.temp_seq
    
    def get_start_seq(self):
        return self.start_seq
    
    def get_queue(self):
        return self.queue
