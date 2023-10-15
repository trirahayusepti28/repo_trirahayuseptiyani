print (20*"=")
print ("Menghitung Volume Bangun Ruang")
print(20*"=" + "\n")

#Login sederhana
username = "trirahayuseptiyani"
nim = "2309116004"
password = "280904"

nama = input("Masukan username :")
nim = input("Masukan nim :")
password = input("Masukan pin :")
if username == nama and password == password:
    print("login berhasil")
else:
    print("login gagal")

#Menghitung volume bangun ruang bola
print(10*"==")
print("Menghitung volume bola")

r = int(input("Masukan jari-jari :"))
phi = 22/7

volume = 4/3*(phi*r*r*r)
print("volume bola = ", volume)

#Menghitung volume bangun ruang tabung
print(10*"==")
print ("Menghitung volume tabung")

r = int(input("Masukan jari-jari :"))
t = int(input("Masukan tinggi :"))
phi = 22/7

volume = phi*r*r*t
print("Volume tabung = ", volume)

#Menghitung volume bangun ruang limas segitiga
print(10*"==")
print("Menghitung volume limas segitiga")

la = int(input("Masukan luas alas :"))
ts = int(input("Masukan tinggi sisi :"))

volume = 1/3*(la*ts)
print("Volume limas segitiga = ", volume)

print(10*"==")
print("selesai")



