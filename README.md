# Jogo de Detecção de Cores com YOLO  
Este projeto é um jogo interativo de detecção de cores utilizando o modelo YOLO (You Only Look Once) para visão computacional e reconhecimento de objetos em tempo real. A interação é feita por comandos de voz, e o usuário deve mostrar uma peça de uma cor específica, sorteada pelo sistema, para a câmera.

## Funcionalidades

- **Reconhecimento de Cores**: O jogo sorteia uma cor e pede para o usuário mostrar um objeto dessa cor para a câmera.
- **Interação por Voz**: A interação com o usuário é feita através de áudios (MP3) e o reconhecimento de voz é utilizado para capturar comandos do usuário.
- **Detecção de Objetos com YOLO**: Utiliza o modelo treinado YOLO para detectar objetos e tentar identificar a cor correta.
- **Limite de Tentativas**: O usuário tem 3 tentativas para acertar a cor. Caso erre 3 vezes, uma nova cor é sorteada e o jogo continua.
- **Rastro de Objeto**: Caso o objeto seja seguido, um rastro visual é exibido na tela.

## Tecnologias Utilizadas

- **Python**: Linguagem principal utilizada no projeto.
- **OpenCV**: Biblioteca para captura de vídeo e manipulação de imagem.
- **YOLO**: Modelo de visão computacional para detecção de objetos.
- **SpeechRecognition**: Biblioteca para reconhecimento de fala.
- **pyttsx3**: Biblioteca para sintetização de voz (texto para fala).
- **pygame**: Utilizado para tocar áudios em formato MP3.

## Requisitos

- Python 3.7 ou superior
- Dependências listadas no `requirements.txt`:
  - `opencv-python`
  - `ultralytics`
  - `speechrecognition`
  - `pyttsx3`
  - `pygame`
  - `numpy`

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/seuusuario/jogo-deteccao-cores.git
    ```

2. Acesse o diretório do projeto:

    ```bash
    cd jogo-deteccao-cores
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Certifique-se de que o YOLO está devidamente treinado e o caminho do modelo (`best.pt`) está correto no código.

5. Coloque os arquivos de áudio MP3 na raiz do projeto ou no diretório de áudio conforme indicado no código.

## Como Executar

1. Conecte uma câmera ao computador (ou utilize a webcam integrada).
2. Execute o script principal:

    ```bash
    python jogo_cores.py
    ```

3. O jogo começará com um áudio de boas-vindas, e o sistema sorteará uma cor. Mostre um objeto da cor solicitada para a câmera e tente acertar!

4. O sistema irá acompanhar suas tentativas. Caso acerte, um áudio de vitória será reproduzido. Se errar, um áudio de erro será executado. Se errar 3 vezes, o jogo sorteará outra cor.

5. Para sair do jogo, pressione a tecla `q`.
