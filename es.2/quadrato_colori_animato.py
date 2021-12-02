from img_lib_v0_51 import (
    immagine_vuota,
    rettangolo,
    affianca_verticale,
    crea_gif,
    Image,)

from img_util import (
    affianca_molte,)

PASSO = 32
DIMENSIONE_CELLA = 10

def crea_quadratino(red: int, green: int, blue: int) -> Image:
    """
    Crea un singolo quadratino di un unico colore.

    :param red: Intensità del colore rosso tra 0 e 255
    :param green: Intensità del colore verde tra 0 e 255
    :param blue: Intensità del colore blue tra 0 e 255

    :returns: un'immagine di un quadratino del colore definito secondo RGB
    """
    colore = "rgb(" + str(red) + "," + str(green) + "," + str(blue) + ")"
    return rettangolo(DIMENSIONE_CELLA, DIMENSIONE_CELLA, colore)


def crea_riga(red: int, green: int) -> Image:
    """
    Crea una sequenza orizzontale di 8 quadratini con intensità costante crescente di blu da 0 a 255.

    :param red: Intensità del colore rosso tra 0 e 255
    :param green: Intensità del colore verde tra 0 e 255

    :returns: una sequenza di quadratini con intensità costante crescente di blu da 0 a 255
    """
    elementi_riga = [
        crea_quadratino(red, green, blue)
        for blue in range(0, 256, PASSO)
        ]
    return affianca_molte(elementi_riga)

    
def crea_quadrato(red: int) -> Image:
    """
    Crea un quadrato con aumento costante di intensità di blu in orizzontale e di verde in verticale.

    :param red: Intensità del colore rosso tra 0 e 255
    
    :returns: un'immagine di un quadrato con sfumature di colore sempre maggiori di blu in orizzontale e di verde in verticale
    """
    img_prec = immagine_vuota()
    
    for green in range(0, 256, PASSO):
        quadrato = affianca_verticale(img_prec, crea_riga(red, green))
        img_prec = quadrato
    return quadrato


def crea_quadrato_animato():
    sequenza_quadrati = [
        crea_quadrato(red)
        for red in range(0, 256, PASSO)
    ]
    return crea_gif("quadrato_animato", sequenza_quadrati)
 
crea_quadrato_animato()