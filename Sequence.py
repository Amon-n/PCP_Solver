from PcpTuple import PcpTuple
from queue import Queue
import copy

class Sequence:
    def __init__(self, start_tuple : PcpTuple):
        self.pcp_queue : Queue[PcpTuple] = Queue()
        self.pcp_queue.put(start_tuple)
        self.missing : str = ""
        self.more_in_first : bool = True # True => more in first part of tuple

    def get_queue(self):
        return self.pcp_queue

    def get_copy(self):
        return copy.deepcopy(self)

    def __add_to_missing(self, pcp_tuple : PcpTuple):
        f = pcp_tuple.pcp_tuple[0]
        s = pcp_tuple.pcp_tuple[1]

        if self.more_in_first:
            f = self.missing + f
        else:
            s = self.missing + s

        for i in range(min(len(f), len(s))):
            pass

        if len(f) > len(s):
            self.missing = f[len(s):]
        else:
            self.missing = s[f:]

    def is_appendable(self, pcp_tuple : PcpTuple):
        pass
    
    def add_tupel(self, pcp_tuple : PcpTuple):
        pass
    
    def is_solution(self):
        if len(self.missing) == 0:
            return True
        return False