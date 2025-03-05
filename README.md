# BaixaCoisas

BaixaCoisas é uma interface web moderna para o **yt-dlp**, combinando **Python (Flask)** e **HTML com Tailwind CSS** para permitir o download de vídeos do YouTube em diferentes formatos e qualidades diretamente pelo navegador.

## Características

- **Download de Vídeos** em resoluções padrão do YouTube (1080p, 720p, 480p, 360p, 240p, 144p).
- **Download de Áudio (MP3)** com conversão automática via **FFmpeg**.
- **Download de Thumbnails** dos vídeos.
- **Interface Moderna** utilizando Tailwind CSS.
- **Histórico de Downloads**, exibindo os vídeos baixados.

## Requisitos

- **Python 3.7+**
- **yt-dlp**
- **FFmpeg** (para conversão de áudio)
- **Flask**

## Instalação e Execução

1. **Clone o Repositório:**
   ```bash
   git clone https://github.com/lenmuo/baixacoisas.git
   cd baixacoisas
   ```

2. **Crie e Ative um Ambiente Virtual (Opcional, mas Recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```

3. **Instale as Dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o Servidor Flask:**
   ```bash
   python app.py
   ```

5. **Acesse no Navegador:**
   ```
   http://localhost:5000
   ```

## Uso

1. Insira a **URL** do vídeo do YouTube.
2. Escolha a **qualidade** do vídeo ou **opte pelo download de áudio (MP3)**.
3. Clique em **Baixar** e aguarde a conclusão do download.
4. Veja seu histórico de downloads na página.

## Tecnologias Utilizadas

- **Python + Flask** para o backend.
- **yt-dlp** para o download de vídeos.
- **Tailwind CSS** para estilização.
- **HTML + JavaScript** para interação no frontend.

## Contribuição

Fique à vontade para abrir **issues** e **pull requests** para melhorias!

## Licença

Este projeto é livre para ser adaptado como você quiser, não tendo licença em específico.
