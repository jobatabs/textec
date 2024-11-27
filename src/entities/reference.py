class Reference:
    def __init__(self, _id: int, author, title, journal, year, type , pp=None, volume=None, number=None, publisher=None, howpublished=None, note=None):
        # __tablename__ = "reference_items"
        self.reference = {
        "id": _id,
        "author": author,
        "title": title,
        "journal": journal,
        "year": year,
        "type": type,
        "pp": pp,
        "volume": volume,
        "number": number,
        "publisher": publisher,
        "howpublished": howpublished,
        "note": note 
        }

    def __str__(self):
        return (
            f"{self.reference['author']}, {self.reference['title']}, {self.reference['journal']} (pp. {self.reference['pp']}), {self.reference['year']}"
            if self.reference["pp"] is not None
            else f"{self.reference['author']}, {self.reference['title']}, {self.reference['journal']}, {self.reference['year']}"
        )

if __name__ == "__main__":  # pragma: no cover
    #tämä toimii 
    test = Reference(1, "Orange Cat", "How To Dominate The World", "Cat Chronicles", "2005", "article", "200-300")
    print(test)