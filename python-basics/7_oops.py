from user import User

user_one = User("Jawad", "jawad@eg.com", "FE Developer")
user_one.print_info()

user_one.change_title("BE Developer")
user_one.print_info()

user_two = User("Test", "test@eg.com", "QA")
user_two.print_info()
