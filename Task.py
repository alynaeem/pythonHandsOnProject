class Task:

    def __init__(self, title):
        self.title = title
        self.done = False

    def markDone(self):
        self.done = True