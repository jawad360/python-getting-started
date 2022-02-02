from datetime import datetime

user_input = input("Enter task with deadline\n")
task = user_input.split(":")[0]
deadline = user_input.split(":")[1]

date = datetime.strptime(deadline, "%d.%m.%Y")
today = date.today()
print(today)
till_deadline = date - today

print(f"For task\n{task} you have {till_deadline.days} days")
