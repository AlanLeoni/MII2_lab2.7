from img_lib_v0_51 import (
    immagine_vuota,
    rettangolo,
    affianca,
    affianca_verticale,
    visualizza_immagine,
    altezza_immagine,
    Image,)

from img_util import (
    affianca_molte,)


def crea_quadratino(red: int, green: int, blue: int) -> Image:
    DIMENSIONE_CELLA =  10
    colore = "rgb(" + str(red) + "," + str(green) + "," + str(blue) + ")"
    cella = rettangolo(DIMENSIONE_CELLA, DIMENSIONE_CELLA, colore)
    return cella


def crea_riga(red: int, green: int, blue: int) -> Image:
    quadratino_prec = immagine_vuota()
    for i in range(0, 255, 32):
        quadratino_succ = crea_quadratino(red, green, blue)
        riga = affianca(quadratino_prec, quadratino_succ)
        quadratino_prec = riga
        blue = blue + 32
    return riga


def crea_quadrato(red: int) -> Image:
    green = 0
    blue = 0
    img_prec = immagine_vuota()
    for i in range(0, 255, 32):
        nuova_immagine = affianca_verticale(img_prec, crea_riga(red, green, blue))
        img_prec = nuova_immagine
        green = green + 32
    return nuova_immagine

    
def crea_slice_quadrati(red = 0) -> Image:
    green = 0
    blue = 0
    slice = []
    for i in range(0, 255, 32):
        slice_quadrato = crea_quadrato(red)
        spazio = rettangolo((altezza_immagine(slice_quadrato))//16, altezza_immagine(slice_quadrato), (000, 000,000,0))
        quadrato_con_spazio = affianca(slice_quadrato,spazio) 
        red = red + 32
        slice.append(quadrato_con_spazio)
    img_slice = affianca_molte(slice)
    return img_slice

visualizza_immagine(crea_slice_quadrati())