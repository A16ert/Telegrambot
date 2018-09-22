from ..db.SQLighter import SQLighter

class BaseService:
    """class provide access for date base helper"""

    def __init__(self):
        self.db = SQLighter()
        pass

    def close(self):
        self.db.close()
        pass





