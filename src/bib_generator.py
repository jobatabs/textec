from entities.reference import Reference


# tähän pitäis voida laittaa suoraan get_references()
def create_bibfile(reference_list: list[Reference] = []):
    with open("references.bib", "w", encoding="utf-8") as f:
        for reference in reference_list:
            tag = generate_tag(reference)
            f.write(f"@{reference.reference['type'].capitalize()}{{{tag},\n")
            fields = Reference.get_fields(reference.reference["type"])

            attributes = []
            for field in fields:
                value = reference.reference.get(field)
                if value is not None:
                    attributes.append(f'  {field.ljust(9)}= "{value}"')

            f.write(",\n".join(attributes) + "\n" + "}\n\n")


def generate_tag(ref: Reference):
    tag = str(ref.reference['title'][:3] + str(ref.reference['year']))
    return tag


if __name__ == "__main__":  # pragma: no cover
    # kovakoodattu lista paikallista testausta varten
    reference_stub = [
        Reference(1, 'article', 'Orange Cat', 'How to Dominate The world',
                  '2005', 'Cat Chronicles', pp='200-300'),
        Reference(2, 'book', 'Black Cat', 'How to Jump',
                  '2024', publisher='Brother')
    ]
    create_bibfile(reference_stub)  # create_bibfile(get_references())
