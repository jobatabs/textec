class Reference:
    def __init__(self, id, author, title, journal, year, pp=None):
        __tablename__ = "reference_items"
        self.id = id
        self.author = author
        self.title = title
        self.journal = journal
        self.year = year
        self.pp = pp

    def __str__(self):
        return f"{self.author}, {self.title}, {self.journal} (pp. {self.pp}), {self.year}" \
            if self.pp is not None \
            else f"{self.author}, {self.title}, {self.journal}, {self.year}"
