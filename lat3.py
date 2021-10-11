print("Konsumsi BBM")
def bbm(jaraktempuh,konsumsibbm):
    return jaraktempuh/konsumsibbm
def isibbm(total,kapasitas):
    return total/kapasitas
#inputdata
jaraktempuh= float(input("Jarak yang ditempuh : "))
konsumsibbm= float(input("Rata rata konsumsi BBM per liter : "))
total= bbm(jaraktempuh,konsumsibbm)
print("BBM yang dibutuhkan", total, "Liter")
kapasitas= float(input("Kapasitas Tangki BBM : "))
total2= isibbm(total,kapasitas)
print("Jadi, untuk menyelesaikan perjalanan pak budi harus mengisi sebanyak", total2, "kali")