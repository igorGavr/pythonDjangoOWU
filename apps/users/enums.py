from enum import Enum


class RegEx(Enum):
    PASSWORD = (
        r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\s])[^\s]{8,20}$',
        [
            'password must contain 1 number (0-9)',
            'password must contain 1 uppercase letter',
            'password must contain 1 lowercase letter',
            'password must contain 1 non-alpha numeric',
            'password min 8 max 20 ch',
        ]
    )

    NAME = (
        r'^[a-zA-Z]{2,20}$',
        'only letters min 2 max 20'
    )

    PHONE = (
        r'^0[95687]\d{8}$',
        'invalid phone number'
    )

    def __init__(self, pattern, msg: str | list[str]):
        self.pattern = pattern
        self.msg = msg