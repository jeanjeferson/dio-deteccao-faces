import cv2
import numpy as np
from ultralytics import YOLO

def main():
    # Inicializa o modelo YOLO pré-treinado
    model = YOLO('yolov8n.pt')
    
    # Inicializa a captura de vídeo (0 é geralmente a webcam padrão)
    cap = cv2.VideoCapture(0)
    
    # Verifica se a câmera foi aberta corretamente
    if not cap.isOpened():
        print("Erro ao abrir a webcam")
        return
    
    print("Pressione 'q' para sair")
    
    while True:
        # Captura frame por frame
        ret, frame = cap.read()
        
        if not ret:
            print("Erro ao capturar o frame")
            break
            
        # Executa a detecção no frame atual
        results = model(frame, conf=0.5)  # conf é o threshold de confiança
        
        # Processa os resultados
        for result in results:
            boxes = result.boxes.cpu().numpy()
            for box in boxes:
                # Verifica se a detecção é uma pessoa (classe 0 no COCO dataset)
                if box.cls[0] == 0:  # classe 0 = pessoa
                    # Extrai as coordenadas do bbox
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    confidence = float(box.conf[0]) if isinstance(box.conf, np.ndarray) else float(box.conf)
                    
                    # Ajusta a região para focar mais no rosto (parte superior do bbox)
                    face_height = int((y2 - y1) * 0.4)  # Usa 40% superior do bbox
                    y2 = y1 + face_height
                    
                    # Desenha o retângulo ao redor do rosto
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    
                    # Adiciona o texto de confiança
                    text = f'Face: {confidence:.0%}'
                    cv2.putText(frame, text, (x1, y1-10), 
                              cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        # Mostra o frame resultante
        cv2.imshow('Face Detection', frame)
        
        # Verifica se o usuário pressionou 'q' para sair
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Libera os recursos
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
