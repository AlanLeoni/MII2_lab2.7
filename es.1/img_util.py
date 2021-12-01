from img_lib_v0_51 import (
    rettangolo,
    immagine_vuota,
    affianca_verticale,
    affianca,
    sovrapponi,
    Image,)


def affianca_molte(immagini: list) -> Image:
    """
    Affianca le immagini elencate all'interno di una lista.

    :param immagini: lista di immagini

    :returns: un'immagine composta da varie immagini affiancate
    """
    affiancate = immagine_vuota()
    for immagine in immagini:
        affiancate = affianca(affiancate, immagine)
    return affiancate


def affianca_verticale_molte(immagini: list) -> Image:
    """
    Affianca verticalmente le immagini elencate all'interno di una lista.

    :param immagini: lista di immagini

    :returns: un'immagine composta da varie immagini affiancate verticalmente
    """
    affiancate_verticale = immagine_vuota()
    for immagine in immagini:
        affiancate_verticale = affianca_verticale(
            affiancate_verticale, immagine)
    return affiancate_verticale


def sovrapponi_molte(immagini: list):
    """
    Sovrappone le immagini elencate all'interno di una lista.

    :param immagini: lista di immagini

    :returns: un'immagine composta da varie immagini sovrapposte una all'altra
    """
    immagine_sovrapposta = immagine_vuota()
    for immagine in immagini:
        immagine_sovrapposta = sovrapponi(immagine_sovrapposta, immagine)
    return immagine_sovrapposta