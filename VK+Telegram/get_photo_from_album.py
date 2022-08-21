import requests
import json

def write_in_json(data):
    with open ('album.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


###https://oauth.vk.com/blank.html#
access_token = 'vk1.a.HAum9xBmk7YHWNePGG2Wp1RHpailFc5SgJmIzxs416wJE8Vvqp6M6a1emqg8XZGn7rixVx32QCUMUA3Cygnkd2TQEkC79P8UqN4p5V7NxkjreGxgWh0Euptc6GXF0-H5p8-oDNvpDR0u21bpbiZ8RFRGBzpqmVtQ_yjQuQLjCX0Hprggm_jD4aFkqzIMD9GO'

# &expires_in=0&user_id=188652733

# https://api.vk.com/method/photos.get?v=5.131&access_token=


def get_requests_to_album():
    group_id = '-13212026'
    album_id = '287118582'
    count = '10'
    re = requests.get(f'https://api.vk.com/method/photos.get?v=5.131&access_token={access_token}', params={'owner_id':group_id, 'count' : count,'album_id':album_id})
    write_in_json(re.json())

get_requests_to_album()