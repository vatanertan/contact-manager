# Contact Manager

A terminal-based contact management application written in Python. It allows users to add, update, delete, and manage contact records interactively, with built-in support for operation cancellation and multi-field editing.

## Features

- **Add Contacts:** Create new contact entries with validation and safe cancellation handling.
- **Edit Contacts:** Modify single or multiple fields of an existing contact, or cancel mid-operation without corrupting existing records.
- **Delete Contacts:** Remove contacts cleanly from the directory.
- **Automated Test Verification:** Includes sample input scenarios and expected outputs covering standard flows and cancellation edge cases.

## Project Structure

```text
contact-manager/
├── contact_manager.py
├── tests/
│   ├── sample_inputs/
│   │   ├── test1_add_contact_cancel.txt
│   │   ├── test2_edit_contact_cancel.txt
│   │   ├── test3_multiple_edit.txt
│   │   ├── test4_edit_all.txt
│   │   └── test5_delete.txt
│   └── expected_outputs/
│       ├── test1_add_contact_cancel_output.txt
│       ├── test2_edit_contact_cancel_output.txt
│       ├── test3_multiple_edit_output.txt
│       ├── test4_edit_all_output.txt
│       └── test5_delete_output.txt
├── .gitignore
└── README.md
```

## Prerequisites

- Python 3.x

## Usage

Run the application interactively from the root directory:

```bash
python contact_manager.py
```

## Running Tests

You can verify the program's behavior against the included test scenarios by passing a sample input file as a command-line argument and comparing the output with the expected result:

```bash
python contact_manager.py tests/sample_inputs/test1_add_contact_cancel.txt > actual_output.txt
diff -u tests/expected_outputs/test1_add_contact_cancel_output.txt actual_output.txt
```

If `diff` produces no output, the test passed completely.
