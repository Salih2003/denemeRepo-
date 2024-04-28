def topla(*args):
	toplam = 0
	for sayı in args:
		toplam = sayı + toplam
	return toplam
	
def çıkar(*args):
	sonuç = 0
	for sayı in args:
		sonuç = sayı - sonuç
	return sonuç
	
def böl(veri1,veri2):
	return veri1 / veri2
	
def tamBöl(veri1, veri2):
	return veri1 // veri2
	
def çarp(veri1, veri2):
	return veri1 * veri2
	
#def küçükSayı():