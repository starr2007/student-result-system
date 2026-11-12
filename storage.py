import json
import os
from student import Student

DATA_FILE = os.path.join("data", "students.json")


def load_students():
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        return {sid: Student.from_dict(d) for sid, d in data.items()}
    except (json.JSONDecodeError, KeyError):
        print("Data file is corrupted. Starting fresh.")
        return {}


def save_students(students):
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump({sid: s.to_dict() for sid, s in students.items()}, f, indent=4)