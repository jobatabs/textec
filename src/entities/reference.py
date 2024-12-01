class Reference:
    def __init__(self, _id: int, type, author, title, year, journal=None, volume=None, number=None, publisher=None, howpublished=None, note=None, pp=None):
        # __tablename__ = "reference_items"
        self.reference = {
            "id": _id,
            "type": type,
            "author": author,
            "title": title,
            "year": year,
            "journal": journal,
            "volume": volume,
            "number": number,
            "pp": pp,
            "publisher": publisher,
            "howpublished": howpublished,
            "note": note
        }

    @classmethod
    def get_fields(cls, reference_type):
        fields = ["author", "title", "year"]
        if reference_type == 'article':
            fields.extend(['journal', 'volume', 'number'])
        elif reference_type == 'book':
            fields.append('publisher')
        else:  # type=misc
            fields.extend(['howpublished', 'note'])

        fields.append('pp')
        return fields

    def __str__(self):
        output = []
        for field in self.__class__.get_fields(self.reference['type']):
            value = self.reference.get(field)
            if value is not None:
                if field == "pp":
                    output.append(f"pp. {value}")
                else:
                    output.append(str(value))

        return ", ".join(output)


if __name__ == "__main__":  # pragma: no cover
    # tämä toimii
    test = Reference(1, 'article', 'Orange Cat', 'How to Dominate The world',
                     '2005', 'Cat Chronicles', pp='200-300')
    test2 = Reference(2, 'book', 'Black Cat', 'How to Jump',
                      '2024', publisher='Brother')
    print(test)
    print(test2)
