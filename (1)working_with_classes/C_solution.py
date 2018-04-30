import traceback
class Player:
    def __init__(self, name):
        def func(new_start, new_ready):
            self.new_start = new_start
            self.new_ready = new_ready
        exec("self." + name + " = func")

def play(g):
    p = Player("ready")
    start = "start"
    while True:
        exec("g." + start + "(p)")
        start = p.new_start
        p = Player(p.new_ready)
