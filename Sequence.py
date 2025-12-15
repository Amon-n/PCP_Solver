from PcpTuple import PcpTuple
from queue import Queue
import copy

class Sequence:
    def __init__(self, start_tuple : PcpTuple):
        self.pcp_queue : Queue[PcpTuple] = Queue()
        self.pcp_queue.put(start_tuple)
        self.missing : str = ""
        self.topString : str = ""
        self.bottomString : str = ""
        self.more_in_first : bool = True # True => more in first part of tuple

    # This Method can be called when a tuple is beeing added to the sequence so that the missing var is updated
    def __add_to_missing(self, pcp_tuple : PcpTuple):
        pass

    def is_appendable(self, pcp_tuple : PcpTuple) -> bool:
        if self.more_in_first:
            concatination = self.missing + pcp_tuple[1]
            other_string = pcp_tuple[0]
        else:
            concatination = self.missing + pcp_tuple[0]
            other_string = pcp_tuple[1]
        shorter, longer = sorted((concatination, other_string), key=len)
        return longer.startswith(shorter)

    def add_tupel(self, pcp_tuple : PcpTuple):
        pass
    
    def is_solution(self):
        if len(self.missing) == 0:
            return True
        return False
