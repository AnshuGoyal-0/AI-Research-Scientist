from datetime import date


class ResearchPaper:

    def __init__(self, title, author, year, citations):
        self.title = title
        self.author = author
        self.year = year
        self.citations = citations

    def display_info(self):
        print(f"Title      : {self.title}")
        print(f"Author     : {self.author}")
        print(f"Year       : {self.year}")
        print(f"Citations  : {self.citations}")
        print(f"Age        : {self.get_age()} years")

    def add_citation(self):
        self.citations += 1

    def update_author(self, new_author):
        self.author = new_author

    def get_age(self):
        return date.today().year - self.year


paper1 = ResearchPaper(
    "Attention Is All You Need",
    "Google",
    2017,
    1000000
)

paper1.display_info()

paper1.add_citation()

print("\nAfter new citation:\n")

paper1.display_info()
