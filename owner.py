import json
from pathlib import Path

DATA_FILE = Path(__file__).with_suffix('.json')

DEFAULT_VARIABLES = {
    1: "password",
    2: "name",
}


def load_variables():
    if DATA_FILE.exists():
        try:
            with DATA_FILE.open('r', encoding='utf-8') as f:
                data = json.load(f)
                return {int(k): v for k, v in data.items()}
        except (json.JSONDecodeError, ValueError):
            pass
    return DEFAULT_VARIABLES.copy()


def save_variables(data):
    with DATA_FILE.open('w', encoding='utf-8') as f:
        json.dump({str(k): v for k, v in data.items()}, f, indent=2)


varibles = load_variables()


def change_password():
    new_password = input("What do you want your new password to be? ")
    varibles[1] = new_password
    save_variables(varibles)


def get_password():
    return varibles[1]


def change_name():
    new_name = input("What do you want your new name to be? ")
    varibles[2] = new_name
    save_variables(varibles)


def get_name():
    return varibles[2]


def reset_variables():
    varibles[1] = "password"
    varibles[2] = "name"
    save_variables(varibles)
