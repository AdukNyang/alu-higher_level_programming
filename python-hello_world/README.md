# Python - Hello, World

This project contains Python scripts and shell scripts for basic Python programming tasks.

## Requirements

- Ubuntu 20.04 LTS
- Python 3.8.5
- All files must be executable
- All files must end with a new line
- Python files start with `#!/usr/bin/python3`
- Shell files start with `#!/bin/bash`

## Tasks

### 0. Run Python file (0-run)
Shell script that runs a Python script stored in environment variable `$PYFILE`.

**Usage:**
```bash
export PYFILE=main.py
./0-run
```

### 1. Run inline (1-run_inline)
Shell script that runs Python code stored in environment variable `$PYCODE`.

**Usage:**
```bash
export PYCODE='print(f"Best School: {88+10}")'
./1-run_inline
```

### 2. Hello, print (2-print.py)
Python script that prints a specific string with quotes.

**Usage:**
```bash
./2-print.py
```

### 3. Print integer (3-print_number.py)
Python script that prints an integer with text using f-strings.

**Usage:**
```bash
./3-print_number.py
```

### 4. Print float (4-print_float.py)
Python script that prints a float with 2 decimal precision.

**Usage:**
```bash
./4-print_float.py
```

### 5. Print string (5-print_string.py)
Python script that prints a string 3 times and its first 9 characters.

**Usage:**
```bash
./5-print_string.py
```

### 6. Play with strings (6-concat.py)
Python script that concatenates strings to create a welcome message.

**Usage:**
```bash
./6-concat.py
```

### 7. Copy - Cut - Paste (7-edges.py)
Python script that extracts parts of a string using slicing.

**Usage:**
```bash
./7-edges.py
```

### 8. Create a new sentence (8-concat_edges.py)
Python script that creates a new sentence from parts of an existing string.

**Usage:**
```bash
./8-concat_edges.py
```

### 9. Easter Egg (9-easter_egg.py)
Python script that prints "The Zen of Python".

**Usage:**
```bash
./9-easter_egg.py
```

## Setup Instructions

1. **Create files:**
   ```bash
   vi filename
   ```

2. **Make executable:**
   ```bash
   chmod +x filename
   ```

3. **Test scripts:**
   ```bash
   ./filename
   ```

## File Structure
```
python-hello_world/
├── 0-run
├── 1-run_inline
├── 2-print.py
├── 3-print_number.py
├── 4-print_float.py
├── 5-print_string.py
├── 6-concat.py
├── 7-edges.py
├── 8-concat_edges.py
├── 9-easter_egg.py
└── README.md
```