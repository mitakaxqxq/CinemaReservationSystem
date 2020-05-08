def log_info(method):
    def inner(*args, **kwargs):
        def write_file(file, data):
            file = open(file, "a+")
            file.write(f'{data}\n')
            file.close()
        return write_file('root/my_file.txt', method(*args, **kwargs))
    return inner
