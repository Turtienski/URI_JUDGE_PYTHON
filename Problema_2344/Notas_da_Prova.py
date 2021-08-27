def convert(nota_str):
    nota = int(nota_str)
    if nota == 0:
         return 'E'
    elif nota > 0 and nota < 36:
        return 'D'
    elif nota > 35 and nota < 61:
        return 'C'
    elif nota > 60 and nota < 85:
        return 'B'
    else:
        return 'A'

entrada = input ()
print(convert(entrada))
