import datetime as datetime

def file_opener(file_location, mode,**kwargs):
    file = open(file_location, mode,**kwargs)
    return file


def time_exec(func_name):
    execution_time=datetime.now().strftime('%Y-%M-%D %H:%M:%S')
    print(f'Execution time for {func_name}:{execution_time}')