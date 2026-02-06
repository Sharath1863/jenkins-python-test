def add(a, b):
    return a + b


if __name__ == "__main__":
    print("Hello from Jenkins Python Build")

    # WRONG CALL (missing argument)
    print("Addition:", add(10))

    print("Build executed successfully!")
