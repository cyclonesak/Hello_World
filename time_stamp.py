from datetime import datetime

date_time = datetime.now()

print(f'{date_time.strftime("%A %d-%B-%Y %I:%M%P").replace(" 0", " ")}') 
