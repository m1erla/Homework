#Homework

# Question 1 
# Python Veri Tipleri 

# Metin Veri Tipleri 

# string(str) => string veri tipi text(metin) yazı türlerini ifade eder. String veri türünün birçok fonksiyonuda vardır. Örnek => len(), count(), strip() gibi.
stringExample = "Hello Python "
print(stringExample)
print(len(stringExample))

# Sayısal Veri Tipleri 
# int => integer veri tipi pozitif veya negatif tam sayıları ifade eder. 
intExample = 23
int2 = -24
print(intExample, int2) 

# float =>  float veri tipi noktadan sonra ondalık sayı içeren sayıları ve tüm bilimsel sayıları ifade eder. 
floatExample = 2.45
print(floatExample)

# complex => complex veri tipi diğer sayısal veri türlerinden de büyük sayıları kapsar ve iki kısımdan oluşur, reel ve imajiner.  
complexExample = 3.14j
print(complexExample)

# [Boolean Veri Tipi] 
# boolean => tanımlanan değişkenleri geriye true veya false döndüren veri tipidir. 
booleanExample = true
theOtherOne = false
print(booleanExample, theOtherOne)

# [Siralama Veri Tipleri] 
# list => birleşik veri tipidir. Virgül ile ayrılır veya köşeli parantez kullanılır. Bu veri tipinde birden fazla veriyi saklayabilliriz. 
listExample = ['Los Angeles'  'Adana'  'Istanbul']
print(listExample)

# tuple => list veri tipine benzer sadece parantez kullanılır. Ancak sadece read-only olarak çalışır. Herhangi bir değer girilemez arttırılamaz. 
tupleSame = ("Read Only")
print(tupleSame)

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
# Ana sayfada görülen tüm textler string veri türündedir. 

# Yüzdelik tamamlandı bölümlerindeki sayısal veriler integer veri türündedir. 

# Kurslarım, tüm kurslar, sıkça sorulan sorular, kategori, profili düzenle vb. kısımlar list türündedir. 

# Question 3  
# Tamamlandımı, bitir ve devam et, programa dahil ol ve giriş yap kısımlarında döngüler kullanılmıştır. 

dataBaseUserName = 'yyyy'
dataBasePassword = 'xxxx'
password = 'xxxx'
userName = 'yyyy'

print('Please enter your userName and password')
if (userName == dataBaseUserName and password == dataBasePassword):
  print('Welcome your in!')
else:
  print('Your informations not correct please try again!')

