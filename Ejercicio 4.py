QUADRAT_NEGRE = chr(int('000' + '2B1C', 16))
QUADRAT_BLANC = chr(int('000' + '2B1B', 16))

for i in range(4):
    print((QUADRAT_NEGRE + QUADRAT_BLANC)*4)
    print((QUADRAT_BLANC + QUADRAT_NEGRE)*4)
   
    