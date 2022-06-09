from Crypto.Cipher import AES
import binascii
import json
import re

key = '011ec47c909e20f9efaab31bfb156b31'

def add_to_16(text):
    if len(text) % 16 != 0:
        text += '\0'
    else:
        text = text[0:16]
    return text


def encrypt(data):
    password = add_to_16(key)
    if isinstance(password, str):
        password = password.encode('utf8')

    bs = AES.block_size
    pad = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
    cipher = AES.new(password, AES.MODE_ECB)
    data = cipher.encrypt(pad(data).encode('utf8'))
    encrypt_data = binascii.b2a_hex(data)
    return encrypt_data.decode('utf8')


def decrypt(decrData):
    password = add_to_16(key)
    if isinstance(password, str):
        password = password.encode('utf8')

    cipher = AES.new(password, AES.MODE_ECB)
    plain_text = cipher.decrypt(binascii.a2b_hex(decrData))
    data = re.search('({.*})', str(plain_text)).group(0)
    return json.loads(data)

# if __name__ == '__main__':
#
#     data = '{"time_start":"2020-07-01 00:00:00","time_end":"2020-07-05 00:00:00"}'      # 待加密数据
#     password = '011ec47c909e20f9efaab31bfb156b31'  # 16,24,32位长的密码（密钥）
#     encrypt_data = encrypt(data)
#     print('加密前数据：{}\n======================='.format(data))
#     print('加密后的数据:', encrypt_data)
#
#     decrypt_data = decrypt('6b7b47314cda21c85a8bdacbde829e7b75e70f6d49b3ccf09e7b7ff36cbeccc94fe15c072d90e71b980d7f37463ed7710d4de75249b323b4152e5d22eedd1ffe5485c5acb986e224b80157d5ef7d84fcb7253803277b5be2c9c56f38438e5697705b3a33167a408e98955a43f5f0bdb072b7a8f79cc3852c13738f85309aecb758da1851eaec50ca9b94b3cb11e1d8009c6f08da1958aed23855adb5d07e90d38242f8c20bbe6e4dc857ae3f4d38947121faaa65d656d86857f421ba44cd48ac6a78f5c52d035eb0089b0e450db289d9b7e6eca543ff018459b11a5a785fdae3814e63afb40aff12454a5ed79a7d75ed57451f5f74ac59c72a876ec19eb70edc648ae8cd5f52e9c948368adac69717011edc6f398b7f0b0dd3e831286a4c0b1cc7f21849d4a1421fadc5cc2ecd370123c0479c2faa45cc3d2a335b2c9036d57ff6f03eaa75ee75af1a8ba80fcc6095785a4e6a86628d11acde0755a487e5ea9bede92691c7f245df0b5dba8831ea6544645927dfdc0d8a66b0a9333de39a37c3a8b575473582f46ac0349a3efad323d3cc9569f8c664c730ca148402ba7254ac7cceed2e51cf9573039353543c5dc2401b22ff2a4117e8091d9a1af47f9f62b8')
#     print('解密后的数据：{}'.format(decrypt_data))