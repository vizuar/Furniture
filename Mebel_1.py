def kv(a,b):
    return (a*b)/10000

def kk(a,b):
  return ((2*a)+(2*b))/100

#TODO да направя калкулация за типов шкаф
#TODO да сумира калкулираните стойности за отделните шкафове
#TODO da калкулира оферта за всеки шкаф поотделно


x = int(input('Въведи ширина = '))
y = int(input('Въведи височина = '))
z= int(input('Въведи дълбочина = '))
vr1 = int(input('Въведи височина на вратата = '))
rc = int(input('Въведи брой рафтове = '))
str_v = int(input('Въведи брой видими страници = '))
str_s = int(input('Въведи брой скрити страници = '))

vrata = kv(x,vr1)
grab = kv(x,y)
str_l = kv(y,z)
str_r = kv(y,z)
dano = kv(x,z)
tavan = kv(x,z)
raft = (kv(x,z))*rc

kvrata = kk(x,vr1)
kgrab = kk(x,y)
kstr_l = kk(y,z)
kstr_r = kk(y,z)
kdano = kk(x,z)
ktavan = kk(x,z)
kraft = (kk(x,z))*rc

mat = sum([vrata,grab,str_l,str_r,dano,tavan,raft])
kant = kvrata+kgrab+kstr_l+kstr_r+kdano+ktavan+kraft

print('квадратурата материала =', mat)
print('дължина на канта =', kant)

