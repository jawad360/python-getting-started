class User:
    def __init__(self, name, email, title):
        self.name = name
        self.email = email
        self.title = title

    def change_title(self, new_title):
        self.title = new_title

    def print_info(self):
        print(f"\nUser details:\nName: {self.name}\nEmail: {self.email}\nTitle: {self.title}")
