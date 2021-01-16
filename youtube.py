from pytube import Playlist
import os
from moviepy.editor import *
import glob

print("##== YOUTUBE PLAYLIST DL AND CONVERT ==##")
print("##== Version : 1.0 ==##")

# Récupération url playlist
url = input("URL de la playlist YT = ")

if url != "":
    p = Playlist(url)
    pTitle = p.title

    # Demande de la convertion ou non
    goToMp3 = False
    convertMp3 = input("Convertir en mp3 ? (o/n) : ")

    # Mise en place de la convertion
    if convertMp3 == "o":
        goToMp3 = True

    # Vérification de l'existance du dossier de la playlist
    if not os.path.exists(pTitle):
        os.makedirs(pTitle)
        # Création des dossiers mp4 et mp3
        if goToMp3:
            if not os.path.exists(pTitle + "/mp4"):
                os.makedirs(pTitle + "/mp4")
            if not os.path.exists(pTitle + "/mp3"):
                os.makedirs(pTitle + "/mp3")

    # Téléchargement des vidéos
    for video in p.videos:
        print("Téléchargement en cours de : " + video.title)
        if goToMp3:
            video.streams.first().download('./' + pTitle + "/mp4")
        else:
            video.streams.first().download('./' + pTitle)

    if goToMp3:
        # Récupération des fichiers mp4
        videos = glob.glob(pTitle + "/mp4/*.mp4")

        # Convertion en mp3
        for video in videos:
            video = video.replace(".mp4","")
            mp4_file = r'./' + video + '.mp4'
            video = video.replace("mp4","mp3")
            mp3_file = r'./' + video + '.mp3'

            videoclip = VideoFileClip(mp4_file)

            audioclip = videoclip.audio
            audioclip.write_audiofile(mp3_file)

            audioclip.close()
            videoclip.close()

    print("##== Merci d'avoir utilisé cet outil ! ==##")
else:
    print("Veuillez saisir une url playlist Youtube !")