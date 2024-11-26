from entities.reference import Reference


# tähän pitäis voida laittaa suoraan get_references()
def create_bibfile(reference_list: list[Reference] = None):
    if reference_list is None:
        reference_list = []

    with open("references.bib", "w", encoding="utf-8") as f:
        for reference in reference_list:
            tag = generate_tag(reference)
            # muista varmistaa uniikki tagi!
            f.write(f"@{reference.type}{{{tag},\n")

            attributes = []
            for attr, value in vars(reference).items():
                if attr not in ["id", "type"] and value is not None:
                    attributes.append(f'  {attr.ljust(9)}= "{value}"')

            f.write(",\n".join(attributes) + "\n" + "}\n\n")


def generate_tag(ref: Reference):
    tag = str(ref.title[:3] + str(ref.year))
    return tag


if __name__ == "__main__":  # pragma: no cover
    # kovakoodattu lista paikallista testausta varten
    reference_stub = [
        Reference(_id=0, author="mlenni", title="test_title1",
                  journal="my_journal", year=2024),
        Reference(_id=1, author="joku", title="test_title2",
                  journal="other_journal", year=2002, _type="Book"),
        Reference(_id=42, author="joku_toinen", title="test_title3",
                  journal="some_journal", year=2013, pp="10-13")
    ]
    create_bibfile(reference_stub)  # create_bibfile(get_references())
