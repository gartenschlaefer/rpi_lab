#serial_data = [['tm','0000-00-00','00:00:00'],['pm','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']]
serial_data = None

def set_serial_data(input):
    global serial_data
    serial_data = input
def get_serial_data():
    return serial_data
