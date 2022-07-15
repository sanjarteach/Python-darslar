


#talaba_0 = {
#    'ism':'alijon',
#    'familiya':'shamsiyev',
#    'yosh':22,
#   'fakultet':'matematika',
#    'kurs':4
#  }

#print(talaba_0.items())
#for key, Value in talaba_0.items():
#    print(f"Kalit: {key}")
#    print(f"qiymat: {Value} \n")

#telefonlar = {
#        'ali':'iphone x',
#       'vali':'galaxy s9',
#       'olim':'mi 10 pro',
#       'Sanjar':'Iphone 13 pro max'
#    }
#for k, q in telefonlar.items():
#    print(f"{k.title()} ning telefoni {q}")

#mahsulotlar = {
#    'olma':'100000',
#   'nok':'12000',
#   'behi':'13000',
#    'banan':'23000'
#}   
#print(mahsulotlar.keys())

#for mahsulot in mahsulotlar.keys():
#print(mahsulot.keys())

#print('Do\'kondagi mahsulotlar:')
#for mahsulot in mahsulotlar.keys():
#    print(mahsulot.title())
#print('do\'kondagi maxsulotlar:keys')
#for mahsulot in mahsulotlar:
#    print(mahsulot.title())
#bozorlik = ['anor', 'uzum','non','baliq']
#for mahsulot in mahsulotlar:
#    if mahsulot in bozorlik:
#       print(f"{mahsulot.title()} {mahsulot[mahsulot]} so'm")


#print("do'konimizdagi mahsulotlar:")
#for mahsulot in sorted(mahsulotlar):
#    print(mahsulot.title())

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'hamida':'galaxy s9',
    'tohir':'huawei p 30',
    'umar':'x'
}

print('foydalanuvchilar quyidagi telefonlarni ishlatishadi')
for tel in set(telefonlar.values()):
    print(tel)


toys = {"ball", "car", "lamp", "ball"}