from os.path import join

def get_static_folder():
    base_dir = '.'
    static_folder=join(base_dir, 'static')
    # print(static_folder)
    return static_folder