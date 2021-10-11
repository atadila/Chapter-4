print("Lama Perjalanan")
def akeb(jarakakeb,kecepatan):
    return (jarakakeb*1000)/(kecepatan*1000/60)
def bkec(jarakbkec,kecepatan1):
    return (jarakbkec*1000)/(kecepatan1*1000/60)
def ttl(total,total1,istirahat):
    return (total+total1+istirahat)
#inputdata
jarakakeb= float(input("Berapa jarak dari kota A ke kota B :"))
kecepatan= float(input("Berapa kecepatan rata-ratanya :"))
total= round(akeb(jarakakeb,kecepatan))
print("Waktu yang dibutuhkan dari kota A ke kota B",total, "Menit")
jarakbkec= float(input("Berapa jarak dari kota B ke kota C :"))
kecepatan1= float(input("Berapa kecepatan rata-ratanya : "))
total1= round(bkec(jarakbkec,kecepatan1))
print("Waktu yang dibutuhkan dari kota B ke kota C", total1, "Menit")
istirahat= float(input("Berapa lama waktu istirahat : "))
ttlo= round(ttl(total,total1,istirahat))
print("total", ttlo, "Menit")