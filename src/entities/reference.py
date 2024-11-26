class Reference:
    def __init__(self, _id: int, author, title, journal, year, _type="Article", pp=None):
        # __tablename__ = "reference_items"
        self.id = _id
        self.author = author
        self.title = title
        self.journal = journal
        self.year = year
        self.type = _type
        self.pp = pp

    def __str__(self):
        return f"{self.author}, {self.title}, {self.journal} (pp. {self.pp}), {self.year}" \
            if self.pp is not None \
            else f"{self.author}, {self.title}, {self.journal}, {self.year}"
