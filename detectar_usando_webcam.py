import pyttsx3
import speech_recognition as sr
import random
from ultralytics import YOLO
import cv2
from collections import defaultdict
import numpy as np
import pygame

# Inicializa o pygame mixer para tocar os áudios
pygame.mixer.init()

# Função para tocar um arquivo de áudio MP3
def tocar_audio(arquivo_audio):
    pygame.mixer.music.load(arquivo_audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

def reconhecer_fala():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Estou ouvindo...")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio, language="pt-BR").lower()
        except sr.UnknownValueError:
            return ""

# Cores reconhecidas
cores = ["vermelho", "amarelo", "roxo", "verde", "azul", "cinza", "rosa"]

# Função para sortear uma nova cor e tocar o áudio correspondente
def sortear_nova_cor():
    cor = random.choice(cores)
    tocar_audio(audios_cores[cor])
    return cor

# Início da interação por voz (com arquivos de áudio)
tocar_audio("boas_vindas.mp3")  # Áudio de boas-vindas

# Dicionário que mapeia as cores aos arquivos de áudio correspondentes
audios_cores = {
    "vermelho": "peca_vermelho.mp3",
    "amarelo": "peca_amarelo.mp3",
    "roxo": "peca_roxo.mp3",
    "verde": "peca_verde.mp3",
    "azul": "peca_azul.mp3",
    "cinza": "peca_cinza.mp3",
    "rosa": "peca_rosa.mp3"
}

# Sorteando a primeira cor
cor_escolhida = sortear_nova_cor()

# Variáveis de controle
cap = cv2.VideoCapture(0)
model = YOLO("C:/cursos/treinando_yolov8/runs/detect/train3/weights/best.pt")
track_history = defaultdict(lambda: [])
seguir = True
deixar_rastro = True
tentativas = 0  # Contador de tentativas

while True:
    success, img = cap.read()

    if success:
        if seguir:
            results = model.track(img, persist=True)
        else:
            results = model(img)

        # Processa os resultados da detecção
        for result in results:
            img = result.plot()

            if seguir and deixar_rastro:
                try:
                    boxes = result.boxes.xywh.cpu()
                    track_ids = result.boxes.id.int().cpu().tolist()

                    for box, track_id in zip(boxes, track_ids):
                        x, y, w, h = box
                        track = track_history[track_id]
                        track.append((float(x), float(y)))  # ponto central

                        if len(track) > 30:
                            track.pop(0)

                        points = np.hstack(track).astype(np.int32).reshape((-1, 1, 2))
                        cv2.polylines(img, [points], isClosed=False, color=(230, 0, 0), thickness=5)
                except:
                    pass

        # Aqui você verifica a cor detectada e compara com a cor escolhida
        cor_detectada = ""  # Implementar a lógica para detectar a cor aqui
        if cor_detectada == cor_escolhida:
            tocar_audio("vitoria.mp3")  # Toca áudio de vitória
            break
        else:
            tentativas += 1  # Incrementa o contador de tentativas
            tocar_audio("erro.mp3")  # Toca áudio de erro

        # Se o usuário errar 3 vezes, sorteia uma nova cor
        if tentativas >= 3:
            tocar_audio("vamos_tentar_outra_cor.mp3")  # Toca áudio de nova tentativa
            cor_escolhida = sortear_nova_cor()  # Sorteia nova cor
            tentativas = 0  # Reseta o contador de tentativas

        cv2.imshow("Tela", img)

    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
tocar_audio("desligando.mp3")  # Áudio ao desligar
