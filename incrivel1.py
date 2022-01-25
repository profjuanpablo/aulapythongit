# importa biblioteca regex (expressões regulares)
import re

mpax = 'o motorista me protegeu do  mal que stava em volta e foi mau-educado na viagem.'

if 'mal' in mpax:
    print('palavra encontrada')
    print('ocorre: ',mpax.count('mal'))

else:
    print('não encontrada')

