from PIL import Image
import encyptor

def encode_image(image_path, destination_path, binary_data):
    img = Image.open(image_path)
    img = img.convert('RGBA')
    encoded_img = img.copy()
    pixels = list(encoded_img.getdata())

    binary_string = ''.join(format(byte, '08b') for byte in binary_data)
    binary_string += '1111111111111110'
    data_len = len(binary_string)
    img_data_len = len(pixels)

    if data_len > img_data_len:
        raise ValueError("The binary data is too large to be encoded in the provided image.")
    
    encoded_pixels = []
    data_index = 0
    for pixel in pixels:
        if data_index < data_len:
            new_pixel = (int(format(pixel[0], '08b')[:-1] + binary_string[data_index], 2), pixel[1], pixel[2], pixel[3])
            encoded_pixels.append(new_pixel)
            data_index += 1
        else:
            encoded_pixels.append(pixel)
    encoded_img.putdata(encoded_pixels)
    encoded_img.save(destination_path, format='BMP')
    print('done encoding!!')

def decode_image(image_path):
    img = Image.open(image_path)
    img = img.convert('RGBA')
    pixels = list(img.getdata())

    binary_string = ''
    count = 0
    for pixel in pixels:
        if count < 24 :
            count += 1
        binary_string += str(pixel[0] & 1)
    print(binary_string)
    delimiter = '1111111111111110'
    data_end = binary_string.find(delimiter)

    if data_end != -1:
        binary_string = binary_string[:data_end]

    binary_data = int(binary_string, 2).to_bytes((len(binary_string) + 7) // 8, byteorder='big')
    return binary_data

if __name__ == '__main__':
    image_path = 'input/test.png'
    destination_path = 'output/test.bmp'
    data = 'T'.encode('utf-8')
    print(data)
    encode_image(image_path, destination_path, data)
    decoded_data = decode_image(image_path)
    print(decoded_data)
