from tripper.domain.elements import Station


class MemRepo(object):

    def __init__(self, data):
        self.data = data

    def list(self):
        return [Station.from_dict(a) for a in self.data]