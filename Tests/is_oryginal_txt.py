import pytest

class TestIsThisOriginalText:
    def tstring_comparsion():
            with open('Kto_ma_co.txt') as f:
                to_cmp=f.read()
            assert to_cmp.strip()=="Ala ma psa od 2022-04-30"
            
        

## Asercja sprawdzenie czy wynik jest poprawny

