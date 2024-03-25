class FileHandler:
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath

    def read(self) -> list[str]:
        rows: list[str] = []
        try:
            file_handle = open(self.filepath, 'r', encoding="UTF-8")
            row = file_handle.readline()
            while row != '':
                row = row.rstrip('\n')
                rows.append(row)
                row = file_handle.readline()
        except Exception as err:
            print(f'Unable to read file {self.filepath}.')
            print(err)
            exit(-1) # from sys library
        return rows