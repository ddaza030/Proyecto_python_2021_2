'''
Funcionalidad de la clase: En este se pone la enumeracion del tipo de las sillas

Autores: Daniel Santiago Cadavid, Marlon Calle, Daniel Daza, Juan Esteban Ochoa
'''

from enum import Enum

#Enums que tiene como utilidad darle un tipo a cada silla del cine
class Tipo(Enum):
    VIP="VIP"
    SENCILLA="SENCILLA"