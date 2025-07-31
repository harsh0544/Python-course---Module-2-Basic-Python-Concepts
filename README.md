
# Python File Handling Tasks

## Task 1: Read a File and Handle Errors

### Objective:
This script reads a text file called `sample.txt`, and it prints each line of the file along with its line number. If the file does not exist, it gracefully handles the error and displays a message indicating the issue.

### Steps:
1. Open and read the contents of `sample.txt`.
2. Print the contents of the file line by line, each with a line number.
3. If the file is missing, display an error message (`FileNotFoundError`).

### How to Run:
1. Ensure that `sample.txt` exists in the same directory as `task1.py`.
2. Run the script:
   ```bash
   python task1.py
````

### Expected Output:

* If the file exists, the program will output each line of the file with the corresponding line number.
* If the file is missing, it will print an error message like:

  ```
  Error: The file 'sample.txt' does not exist.
  ```

---

## Task 2: Write, Append, and Read Data

### Objective:

This script allows the user to interact with a file named `output.txt`. It first prompts the user for input, writes it to the file, then appends additional input to the same file. Finally, it reads and displays the entire content of the file.

### Steps:

1. Prompt the user for input and write it to `output.txt`.
2. Prompt the user for additional input and append it to `output.txt`.
3. Open the file and display the entire content after both write and append operations.

### How to Run:

1. Simply run the script, and it will prompt you to enter text.
2. The script will then write the first input, append the second input, and display the contents of the file.

```bash
python task2.py
```

### Expected Output:

* The user will first be prompted to enter some text to write to the file.
* After writing, the user will be prompted again to append more text.
* The final content of the file will be displayed, which should include both inputs, separated by newlines.

Example interaction:

```
Enter some text to write to the file: Hello, this is the first line.
Enter additional text to append to the file: This is the second line.

Final content of the file:
Hello, this is the first line.
This is the second line.
```

---

### Notes:

* Both tasks handle common file operations such as reading, writing, and appending.
* The tasks also demonstrate basic error handling and user interaction with file I/O in Python.

```

---

### Breakdown of Sections:
1. **Task Descriptions**: Detailed explanation of what each task does.
2. **Step-by-step instructions**: What the user should expect in the process of running the scripts.
3. **How to run**: Clear instructions on how to run the scripts using the command line.
4. **Expected output**: What the user should see when they execute the script.

This version of the `README.md` is more detailed and will help users understand exactly what each task is doing, how to run the scripts, and what to expect in terms of output. Let me know if you need more adjustments!
```
