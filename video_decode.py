import cv2
import argparse
from pyzbar.pyzbar import decode

def pre_processing(image):
    # Converte a imagem para a escala de cinza:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Suaviza a imagem com um filtro gaussiano de borramento:
    suavizada = cv2.GaussianBlur(gray_image, (3, 3), 0)

    # Binariza a imagem:
    _, binary_image = cv2.threshold(suavizada, 190, 255, cv2.THRESH_BINARY)

    return binary_image

def decode_qr_code(image):
    # Aplica o processamento na imagem:
    new_image = pre_processing(image)

    # Decodifica qrcodes
    decoded_objects = decode(new_image)
    
    # Verifica se algum QRcode foi encontrado
    if decoded_objects:
        # Itera sobre os resultados e imprime os dados decodificados
        for obj in decoded_objects:
            # Obtém as coordenadas da bounding box
            x, y, w, h = obj.rect
            
            # Desenha a bounding box ao redor do QR code na imagem
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            
            # Adiciona o texto do QR code na imagem
            cv2.putText(image, obj.data.decode('utf-8'), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        # Mostra a imagem com a bounding box e o texto
        cv2.imshow('video', image)
    else:
        # Mostra a imagem sem bounding box:
        cv2.imshow('video', image)

def main():
    # Criação do parser de argumentos de linha de comando
    parser = argparse.ArgumentParser(description='Decodifica Qrcode e barcodes em um video.')
    parser.add_argument('video_path', type=str, help='Caminho para o video.')

    # Parse dos argumentos
    args = parser.parse_args()

    # Abre o vídeo para leitura
    video_capture = cv2.VideoCapture(args.video_path)
    
    # Loop para processar cada frame do vídeo
    while True:
        # Lê um frame do vídeo
        ret, frame = video_capture.read()

        # Verifica se o frame foi lido corretamente
        if not ret:
            break

        # Aplica um resize no frame
        frame = cv2.resize(frame, (1000, 800))

        # Chama a função para decodificar o QR code no frame
        decode_qr_code(frame)

        # Verifica se o usuário pressionou a tecla 'q' para sair
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libera o objeto de captura e fecha todas as janelas
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()