import datetime  
now = datetime.datetime.now()  
print("Fecha y hora actual:", now)

date = datetime.datetime(2025, 5, 15)  
print("Fecha personalizada:", date.strftime("%d/%m/%Y"))
