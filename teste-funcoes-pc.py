from gtts import gTTS

# texto = """Respiração profunda.
# Inspire pelo nariz, lenta e profundamente... Um, dois, três, quatro...
# Segure o ar... um, dois...
# Agora solte devagar pela boca... seis, cinco, quatro, três, dois, um...
# Repita.
# Sinta o ar entrando fresco, e saindo leve.
# Deixe os ombros caírem... a mandíbula relaxar...
# Sua testa solta... as sobrancelhas sem tensão.

# Agora leve a atenção para as pálpebras.
# Sinta o peso delas protegendo seus olhos.
# Piscar devagar...
# Mais devagar...
# Imagine os olhos descansando numa rede, flutuando.
# Como se mergulhassem em água fria, refrescando.

# Imagine agora um campo aberto, silencioso.
# Ao redor, uma brisa suave.
# Nada precisa ser resolvido agora.
# Só esse momento de descanso.
# Respire.
# A cada expiração, solte a tensão dos olhos, da testa, da mente.
# Repita mentalmente:
# “Estou aqui. Estou seguro. Estou em paz.”

# Traga sua atenção de volta devagar.
# Mexa os dedos dos pés, das mãos.
# Sinta o ambiente ao redor.
# Quando estiver pronto, abra os olhos lentamente.
# Respire fundo mais uma vez... e continue o dia com leveza.
# """

# tts = gTTS(text=texto, lang='pt-br')
# tts.save("relaxamento.mp3")



# from moviepy.editor import *

# # Carrega o áudio
# audio = AudioFileClip("relaxamento.mp3")

# # Carrega uma imagem de fundo
# imagem = ImageClip("fundo.jpg") \
#     .set_duration(audio.duration) \
#     .set_audio(audio) \
#     .resize(height=720) \
#     .set_fps(24)

# # Exporta o vídeo
# imagem.write_videofile("relaxamento_video.mp4")


import psutil
import time
import winsound  # só funciona no Windows

ALVO = 80  # porcentagem que você quer atingir

def tocar_alarme():
    print("🔔 Bateria chegou a 90%! Desconecte o carregador.")
    for _ in range(3):
        winsound.Beep(1000, 500)  # frequência, duração (ms)
        time.sleep(0.5)

while True:
    bateria = psutil.sensors_battery()
    porcentagem = bateria.percent
    carregando = bateria.power_plugged

    print(f"Bateria: {porcentagem}% {'(carregando)' if carregando else '(desplugado)'}")

    if carregando and porcentagem >= ALVO:
        tocar_alarme()
        break  # sai do loop depois do aviso

    time.sleep(30)  # checa a cada 30 segundos


# ALVO = 22

# def tocar_alarme():
#     print("🔌 Bateria chegou a 20%! Hora de conectar o carregador.")
#     for _ in range(3):
#         winsound.Beep(800, 500)
#         time.sleep(0.5)

# while True:
#     bateria = psutil.sensors_battery()
#     porcentagem = bateria.percent
#     carregando = bateria.power_plugged

#     print(f"Bateria: {porcentagem}% (carregando: {carregando})")

#     if not carregando and porcentagem <= ALVO:
#         tocar_alarme()
#         break

#     time.sleep(30)
