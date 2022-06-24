class NumberError(Exception):
    def __str__(self):
        return '\n' + 'No one is joining for the party'
