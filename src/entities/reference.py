class Reference:
    def __init__(self, id: int, author, title, journal, year, type="Article", pp=None):
        __tablename__ = "reference_items"
        self.id = id
        self.author = author
        self.title = title
        self.journal = journal
        self.year = year
        self.type = type
        self.pp = pp

    def __str__(self):
        attributes = [
            f"{value}" for attr, value in vars(self).items() if value is not None
        ]
        return ", ".join(attributes)