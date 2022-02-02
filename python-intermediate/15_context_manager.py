from contextlib import contextmanager
# Resources allocate and release resources when needed

# This will close the `file` and free resources after with statement
with open('file.txt', 'w') as file:
    file.write("Todo")

# The above is same as
file_2 = open('file_2.txt', 'w')
try:
    file_2.write("Todo 2")
finally:
    file_2.close()


# custom context
print(" === Custom context ===")


class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print("Entering")
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        print("Exiting")

# Can be also done like this
# man_file = ManagedFile('notes.txt')


with ManagedFile('notes.txt') as file:
    print("Doing stuff")
    file.write("Todoooo")


# Exception in custom context
print("=== Exception in custom context ===")


class ManagedFileExp:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print("Entering")
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        print("Exiting")
        # If we return true then `Continue` will be printed as it means exception is handled
        return True

# Can be also done like this
# man_file = ManagedFile('notes.txt')


with ManagedFileExp('notes.txt') as file_exp:
    print("Doing stuff")
    # This will create exception, but __exit__ method will be complete
    # `Continue` will not be printed
    file_exp.some_random("Todoooo")

print("Continue")

# Using function
print("=== Context using function ===")


@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f
    # Exception can also be handled here
    finally:
        # Finally will be executed after with is finished
        f.close()


with open_managed_file('notes.txt') as file:
    file.write("Todoooo!!!")
print("Continue!!")






