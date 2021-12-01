from img_lib_v0_51 import (
    immagine_vuota,
    rettangolo,
    affianca,
    affianca_verticale,
    visualizza_immagine,
    Image,
)
PASSO = 32

def crea_quadratino(red: int, green: int, blue: int) -> Image:
    DIMENSIONE_CELLA = 10
    colore = "rgb(" + str(red) + "," + str(green) + "," + str(blue) + ")"
    cella = rettangolo(DIMENSIONE_CELLA, DIMENSIONE_CELLA, colore)
    return cella


def crea_riga(red: int, green: int, blue: int) -> Image:
    quadratino_prec = immagine_vuota()
    for blue in range(0, 255, PASSO):
        quadratino_succ = crea_quadratino(red, green, blue)
        riga = affianca(quadratino_prec, quadratino_succ)
        quadratino_prec = riga
    return riga


def crea_quadrato(red: int, green: int, blue: int) -> Image:
    img_prec = immagine_vuota()
    
    for green in range(0, 255, PASSO):
        nuova_immagine = affianca_verticale(img_prec, crea_riga(red, green, blue))
        img_prec = nuova_immagine
    return nuova_immagine


def affianca_molte(immagini_con_spazio: list) -> Image:
    affiancate = immagine_vuota()
    for immagine in immagini_con_spazio:
        affiancate = affianca(affiancate, immagine)
    return affiancate

    
def crea_slice_quadrati() -> Image:    
    green = 0
    blue = 0
    slice = []
    for red in range(0, 255, PASSO):
        slice_quadrato = crea_quadrato(red, green, blue)
        slice.append(slice_quadrato)
    img_slice = affianca_molte(slice)
    return img_slice

visualizza_immagine(crea_slice_quadrati())
