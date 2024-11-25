from repositories.reference_repository import get_references
from entities.reference import Reference


# tähän pitäis voida laittaa suoraan get_references()
def create_bibfile(list_of_references: list[Reference] = []):

    reference_list = list_of_references  # vähän turha, mutta selkeempi

    with open("references.bib", "w") as f:
        for reference in reference_list:
            tag = generate_tag(reference)
            # muista varmistaa uniikki viite!
            f.write(f"@{reference.type}{{{tag},\n")
            f.write(f'  author   = "{reference.author}",\n')
            f.write(f'  title    = "{reference.title}",\n')
            f.write(f'  journal  = "{reference.journal}",\n')
            f.write(f'  year     = {reference.year}\n')
            f.write("}\n\n")


def generate_tag(ref: Reference):
    tag = str(ref.title[:3] + str(ref.year))
    return tag


if __name__ == "__main__":  # pragma: no cover
    # kovakoodattu lista paikallista testausta varten
    reference_stub = [
        Reference(id=0, author="mlenni", title="test_title1",
                  journal="my_journal", year=2024),
        Reference(id=1, author="joku", title="test_title2",
                  journal="other_journal", year=2002, type="Book"),
        Reference(id=2, author="joku_toinen", title="test_title3",
                  journal="some_journal", year=2013)
    ]
    create_bibfile(reference_stub)  # create_bibfile(get_references())
