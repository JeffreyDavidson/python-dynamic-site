class Player(object):
    def __init__(self):
        self.id = ''
        self.player_name = ''
        self.position = ''

class Fielder(Player):
    def __init__(self):
        super(Fielder, self).__init__()
        self.bats = ''
        self.throws = ''
        self.avg = ''
        self.hr = ''
        self.rbi = ''

class Pitcher(Player):
    def __init__(self):
        super(Pitcher, self).__init__()
        self.ip = ''
        self.era = ''
        self.strikeouts = ''
        self.walks = ''
        self.saves = ''


