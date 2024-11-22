class Reference:
    def __init__(self, id, author, title, journal, year, type="Misc"):
        __tablename__ = "reference_items"
        self.id = id
        self.author = author
        self.title = title
        self.journal = journal
        self.year = year
        self.type = type

    def __str__(self):
        return f"{self.author}, {self.title}, {self.journal}, {self.year}"
