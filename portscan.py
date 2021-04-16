import os

os.system("apt-get install figlet")
os.system("clear")
os.system("apt-get install nmap")
os.system("clear")
os.system("figlet -c Port Tarama")

print("""
Port Tarama Programına hoşgeldiniz.

1) Hızlı Port Tarama

2) Servis ve Versiyon Bilgisi

3) İşletim Sistemi Bilgisi

4) Açık Port Taraması

			İnstagram = https://instagram.com/iskender_eren_goktas
""")

İşlem = int(input("İşlem Numarası Giriniz : "))

if İşlem == 1 :
	hedef = input("Hedef IP Giriniz : ")
	os.system("nmap " + hedef)
elif İşlem == 2 :
	hedef1 = input("Hedef IP Giriniz : ")
	os.system("nmap -sS -sV " + hedef1)
elif İşlem == 3 :
	hadef2  = input("Hedef IP Giriniz : ")
	os.system("namp -O " + hadef2)
elif İşlem == 4 :
	hedefip = input("Hedef IP Giriniz : ")
	os.system("sudo nmap -Pn -sS -n -v --reason --open " + hedefip)
else:
	print("          !!!Hatalı Seçim Yaptınız Program Kapatıldı!!!")

