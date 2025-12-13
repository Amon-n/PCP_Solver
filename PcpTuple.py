class PcpTuple:
    def __init__(self, id, pcp_tuple : tuple[str, str]):
        self.id : int = id
        self.pcp_tuple : tuple[str, str] = pcp_tuple
    def __str__(self):
        return f"{self.pcp_tuple}"