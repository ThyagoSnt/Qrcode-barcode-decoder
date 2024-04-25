# QR Code & Barcode Decoder

Este é um decoder de QR Code e Barcode desenvolvido para processar imagens, vídeos e aplicações de imagens em tempo real.

## Instalação

Use o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar as dependências necessárias.

```bash
pip install pyzbar
pip install numpy
pip install opencv-python
```

## Uso
### Decodificação de Imagens e Vídeos
Para decodificar QR codes e barcodes de imagens ou vídeos, execute o seguinte comando:

```bash
python decode.py <caminho_para_a_imagem> image
python decode.py <caminho_para_o_video> video
```


## Aplicação em Tempo Real
### Para decodificar QR codes e barcodes em tempo real usando a câmera, execute o seguinte comando:

```bash
python real_time_decode.py
```

## Licença
### MIT
