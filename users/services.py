import json

class FileReadWriteService:
    _file_name = None

    @classmethod
    def load_users(cls):
        try:
            with open(cls._file_name) as file:
                return json.load(file)
        except (Exception,):
            return []

    @classmethod
    def save_users(cls, data):
        try:
            with open(cls._file_name, 'w') as file:
                return json.dump(data, file)
        except Exception as err:
            return str(err)
