# 📸 Detecção de Faces com YOLO

Este projeto utiliza o modelo YOLO (You Only Look Once) para detectar rostos em tempo real através da webcam. O modelo YOLO é conhecido por sua rapidez e precisão na detecção de objetos em imagens.

## 🛠️ Pré-requisitos

Antes de começar, certifique-se de ter os seguintes itens instalados:

- Python 3.6 ou superior
- OpenCV
- NumPy
- Ultralytics YOLO

Você pode instalar as dependências necessárias usando o pip:

```bash
pip install opencv-python numpy ultralytics
```

## 🚀 Como executar o projeto

Siga os passos abaixo para rodar o projeto:

1. **Clone o repositório**:
   ```bash:dio-deteccao-faces/README.md
   git clone https://github.com/seu-usuario/dio-deteccao-faces.git
   cd dio-deteccao-faces
   ```

2. **Execute o script**:
   ```bash
   python yolo-face.py
   ```

3. **Interaja com a aplicação**:
   - A aplicação abrirá uma janela mostrando a captura da webcam com detecção de rostos.
   - Pressione `q` para sair da aplicação.

## 📝 Como funciona

- O script inicializa o modelo YOLO pré-treinado para detecção de objetos.
- A captura de vídeo é feita através da webcam padrão do sistema.
- Para cada frame capturado, o modelo YOLO é utilizado para detectar objetos.
- Se um objeto detectado for uma pessoa, o script ajusta a região do bounding box para focar no rosto.
- Um retângulo verde é desenhado ao redor do rosto detectado, e a confiança da detecção é exibida.

## 📂 Estrutura do Projeto

- `yolo-face.py`: Script principal que executa a detecção de rostos.
- `README.md`: Este arquivo, com instruções detalhadas sobre o projeto.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

Divirta-se detectando rostos! 😄