from google.cloud import texttospeech

# Instancia o cliente
client = texttospeech.TextToSpeechClient()

# Configura a solicitação
synthesis_input = texttospeech.SynthesisInput(text="Olá, bem-vindo ao jogo de cores!")

# Seleciona o tipo de voz
voice = texttospeech.VoiceSelectionParams(
    language_code="pt-BR",
    name="pt-BR-Wavenet-A",
    ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
)

# Configura o tipo de áudio
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Solicita a síntese de fala
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# Salva a saída de áudio em um arquivo
with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
    print("Áudio salvo como output.mp3")

# Você pode usar um reprodutor de áudio para tocar o arquivo, ou integrar com bibliotecas como `pygame`.
