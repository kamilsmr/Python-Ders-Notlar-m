
# stringler
# eğer tek veya çift tırnak ile nasıl başlarsa öyle bitmesi gerekir.

# print('kamil')
# print("kamil")
# print("""kamil """)
# kullanım yanlış
# print("kamil')
# iki tarz yazımı var kesmeli ifadenin
# print("kamil'in kalemi var")
# print('kamil\'in kalemi var')

# string indexleri

# a = "kamil"
# print(a[0])
# print(a[3])
# print(a[4])
# print(a[1])

# b = "selim"
# print(b[-1])
# print(b[-4])
# print(b[-2])
# print(b[-3])

# string parçalama 

# a = "Bir gun cok degerlidir."
# print(a[3:10])
# print(a[:5])
# print(a[6:])
# print(a[:])
# print(a[:-1])
# print(a[::2])
# print(a[3:18:2])
# print(a[::-1])

# len uzunluğunu bulma.
# string = "istanbul"
# print(len(string))
# string[3] = a # strinler değiştirilemez.

# x = "python"
# print(x*3)

# x = "python"
# y = "java"
# print(x+y)

# stringler değiştirilemez fakat deiştirmek istersek yeni bir string yapmalıyız

# x = "kamil"
# x = "ali" + "kamil"
# print(x)

# \n satır atlama
# print("merhaba\nnasilsin\nnasilgidiyor\n")

# \t boşluk bırakma
# print("ali\tmehmet\tselim")
# print("ali\t\tmehmet\t\tselim")

# sep parametresi 
# print("ali","ahmet","mehmet",sep="/")
# print("ali","ahmet","mehmet",sep="\n")


# print("01","02","2021",sep="/")

# * kullanma
# print(*"python")
# print(*"python",sep=".")

#formatlama
# a=2
# b=5
# print("{} + {} = {} ye esittir.".format(a,b,a+b))

