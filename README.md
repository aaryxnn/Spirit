# Spirit

A desktop management app for a taekwondo academy.

Spirit is a Python coursework project that combines student record management with equipment ordering and billing. It uses a Tkinter interface and a MySQL database for student records, with text files for saved bills.

## Features

- Login screen and a menu for the student and equipment modules.
- Add, search, update, list, and delete student records.
- Track student details such as joining dates, contact information, and academy branch.
- Select uniforms and training equipment, add items to an order, and calculate totals.
- Generate, save, and look up bills.

## Stack

**Python Â· Tkinter / ttk Â· MySQL Â· PyMySQL**

## Run locally

Use a desktop environment with Python and Tkinter installed. The project was originally developed with Python 3.10; compatibility with other versions has not been verified.

```bash
git clone https://github.com/aaryxnn/Spirit.git
cd Spirit
python -m pip install pymysql
python -m tkinter
```

The last command opens a small window to confirm Tkinter is available. Some Linux distributions package Tkinter separately.

Create a folder for generated bills before starting the equipment module:

```bash
mkdir bills
```

For the student module, run MySQL locally and configure the connection in `studentF.py`. The original code uses a local development account (`sqluser`) and a placeholder password. Use an account for your own local database with permission to create the `studentmanagement` database and its `student` table. The **Connect** button initializes the database connection.

Start the app from the repository root so the image assets can be found:

```bash
python login.py
```

The original coursework login is `Admin` / `1234`. It is a demonstration login with hardcoded checks.

## Project structure

| File | Purpose |
| --- | --- |
| `login.py` | Login window and entry point |
| `menu.py` | Navigation between modules |
| `studentF.py` | Student forms, table view, and database operations |
| `equipmentOrder.py` | Equipment selection, cart, totals, and billing |
| `Logo.png`, `bg-2.png` | Interface assets |
| Numbered `.txt` files | Original sample bill output |

## Project status

This is an early desktop application preserved as a learning project. It demonstrates GUI event handling, SQL CRUD operations, and file-based billing. The code includes fixed window sizes, basic validation, and hardcoded development settings. Student schema/form consistency and end-to-end behavior need review before extending it for real academy use.

The `.pyc` files are compiled artifacts from the original upload; run the Python source files. The original `35566.pdf` file contains plain-text bill output despite its extension.
