# Замыкание

# nonelocal

def summ(arg_summ):
    """Идея в том что бы брать итог каждого метода и закидывать сюда для подсчета стоимости чека"""
    itogo = 0  # Выступает в роле

    def s(arg_summ):
        nonlocal itogo
        return itogo + arg_summ

    return s


itog = summ(0)
itog(100)
itog(100)


