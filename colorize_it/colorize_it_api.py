import Algorithmia
import base64
import random
import string
import _config


def send_pic(image_file, filename, api_key=_config.ALGORITHMIA_API_KEY):
    # with open(image_file, "rb") as image_file:
    #     image_encoded = base64.b64encode(image_file.read())
    client = Algorithmia.client(api_key)

    algo = client.algo('deeplearning/ColorfulImageColorization/1.1.13')
    path_on_server = 'data://.algo/deeplearning/ColorfulImageColorization/temp/' + filename + '.jpg'
    client.file(path_on_server).putFile(image_file.name)

    input = {
    "image": path_on_server
    }

    output_path = algo.pipe(input).result['output']
    return client.file(output_path).getBytes()

def main():
    pass

if __name__ == '__main__':
    main()
