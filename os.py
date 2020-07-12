import os

#os.chdir("C:/Users") #dizinin değiştirir

print(os.getcwd()) # hangi dizin altında çalıştığımızı verir

for i in os.listdir(): # bulunduğumuz dizindeki dosyaları ekrana yazar

    print(i)

#os.mkdir("Deneme1")

#os.makedirs("Deneme1/deneme2") #deneme 1 altında deneme2 yi oluşturdu

#os.rmdir("Deneme1/deneme2") #deneme2 yi siler 
#os.removedirs("sd/sad") # iki dizini de siler

#os.rename("ilk dsoya","ikinci dosya") ilk dosyayı ikinci ile değiştirir

#print(os.stat("test2.txt")) test2.txt dosyasının özelliklerini verir

for dizin,isim,dosya in os.walk("C:/Users/Lenovo/Desktop"):
    for i in dosya:
        if i.endswith(".txt"):
            print(i)

