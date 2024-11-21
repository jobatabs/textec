from repositories.reference_repository import get_references

def create_bibfile():
    reference_list = get_references()
    tag = generate_tag(reference.author, reference.year)
    with open("references.bib", "w") as f:
        for reference in reference_list:
            f.write(f"@misc{{{tag},\n")
            f.write(f'  author = "{reference.author}",\n')
            f.write(f'  title = "{reference.title}",\n')
            f.write(f'  journal = "{reference.journal}",\n')
            f.write(f'  year = "{reference.year}"\n')
            f.write("}\n\n")

def generate_tag(name, year):
    tag = str(name[:3] + year)
    return tag