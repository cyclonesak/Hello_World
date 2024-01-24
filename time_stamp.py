from datetime import datetime

def sak_TimeStamp():
    '''Output example: Wednesday 24-January-2024 2:35pm'''
    date_time = datetime.now()
    timeStamp = f'{date_time.strftime("%A %d-%B-%Y %I:%M%P").replace(" 0", " ")}'
    return timeStamp

if __name__ == '__main__':
    '''This stops the line below being run if called from another program'''
    print(sak_TimeStamp())