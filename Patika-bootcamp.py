#Homework

# Question 1 
# Python Veri Tipleri 

# Metin Veri Tipleri 

# string(str) => string veri tipi text(metin) yazı türlerini ifade eder. String veri türünün birçok fonksiyonuda vardır. Örnek => len(), count(), strip() gibi.
stringExample = "Hello Python "
stringInt = "4355"
print(stringExample)
print(int(stringInt))
print(len(stringExample))
print(type(stringExample))

# Sayısal Veri Tipleri 
# int => integer veri tipi pozitif veya negatif tam sayıları ifade eder. 
intExample = 23
intSecond = 35
print(intExample + intSecond) 
print(type(intExample))
print(type(intSecond))

# float =>  float veri tipi noktadan sonra ondalık sayı içeren sayıları ve tüm bilimsel sayıları ifade eder. 
floatExample = 2.45
print(floatExample)
print(type(floatExample))

# complex => complex veri tipi diğer sayısal veri türlerinden de büyük sayıları kapsar ve iki kısımdan oluşur, reel ve imajiner.  
complexExample = 3.14j
print(complexExample)
print(type(complexExample))

# [Boolean Veri Tipi] 
# boolean => tanımlanan değişkenleri geriye true veya false döndüren veri tipidir. 
booleanExample = true
theOtherOne = false
if(booleanExample== true):
  print("That is true")
else:
  print("That is false")
print(booleanExample, theOtherOne)
print(type(booleanExample))
print(type(theOtherOne))

# [Siralama Veri Tipleri] 
# list => birleşik veri tipidir. Virgül ile ayrılır veya köşeli parantez kullanılır. Bu veri tipinde birden fazla veriyi saklayabilliriz. 
listExampleFirst = ['Los Angeles' " "  'Adana' " " 'Istanbul']
listSecond = [True, "Hello World" , 'Test']
print(listExampleFirst)
print(type(listExampleFirst))
print(listExampleFirst + listSecond)
print(listExampleFirst , listSecond)

# tuple => list veri tipine benzer sadece parantez kullanılır. Ancak sadece read-only olarak çalışır. Herhangi bir değer girilemez arttırılamaz. 
tupleSame = ("Read Only", "Python")
print(tupleSame)
print(type(tupleSame))

# range  
# dictonary 

# [Haritalama Veri Tipi] 
# dict 

# [Set Veri Tipleri] 
# Set  
# FrozenSet  

# [Binary Veri Tipleri] 
# Bytes  
# Bytearray 
# Memoryview 

# Question 2 
# Ana sayfada görülen tüm textler string veri türündedir. Ancak bir data uzerinden aktarildigini dusunuyorum. 

# Yüzdelik tamamlandı bölümlerindeki sayısal veriler integer veri türündedir. 

# Kurslarım, tüm kurslar, sıkça sorulan sorular, kategori, profili düzenle vb. kısımlar list türündedir. 

# Question 3  
# Tamamlandımı, bitir ve devam et, programa dahil ol ve giriş yap kısımlarında döngüler ve sart bloklari kullanılmıştır. 
# for dongusu => Tamamlama orani yuzde 50 tamamlandiysa yarim doldur, yuzde 100 tamamlandiysa tam doldur gibi.
# boolean => programa dahil ol ve giris yap 
# list => kategoriler, kurslar vb.
# dictionary => kullanici bilgileri
# integer => tamamlama yuzdelik orani

# Sart blogu => giris yap bolumu ve programa dahil ol bolumunde kullanildigini dusunuyorum
dataBaseUserName = "userName"
dataBasePassword = "password"

userName = input("userName")
password = input("password")

print('Please enter your userName and password')
if (userName == dataBaseUserName and password == dataBasePassword):
  print("Welcome your in!")
else:
  print("Your informations not correct please try again!")
  
dataBaseRegisteredUser = True
if(dataBaseRegisteredUser == True):
  print("Congrats you can watch this program")
else:
  print("You can not watch this program. You should register on the website")

  

