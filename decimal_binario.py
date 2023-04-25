import unittest

from decimal_binario import decimal_binario


def decimal_binario(decimal, binario):
    
    binario_resultado = bin(decimal)[2:]
    assert binario_resultado == binario, f"El valor binario esperado para {decimal} es {binario}, pero se obtuvo {binario_resultado}"
    
    
    decimal_resultado = int(binario, 2)
    assert decimal_resultado == decimal, f"El valor decimal esperado para {binario} es {decimal}, pero se obtuvo {decimal_resultado}"
    
    
    return True
     
         
if __name__== '__main__':
    unittest.main()