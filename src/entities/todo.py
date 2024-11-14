class Todo:
    def __init__(self, id, author, title, journal, year):
        self.id = id
        self.author = author
        self.title = title
        self.journal = journal
        self.year = year

    def __str__(self):
        is_done = "done" if self.done else "not done"
        return f"{self.content}, {is_done}"
