try:
    print("Reading File Content:")
    with open("sample.txt") as file:
        for i, line in enumerate(file, 1):
            print(f"Line {i}: {line.strip()}")
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
