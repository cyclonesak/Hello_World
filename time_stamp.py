from datetime import datetime

def sak_TimeStamp():
    date_time = datetime.now()
    timeStamp = f'{date_time.strftime("%A %d-%B-%Y %I:%M%P").replace(" 0", " ")}'
    return timeStamp

def main():
    print(sak_TimeStamp())

if __name__ == '__main__':
    main()