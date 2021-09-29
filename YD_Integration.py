import requests
from pprint import pprint

files_list = []


with open('YD_token.txt', 'r') as file_object:
    yd_token = file_object.read().strip()


class YaUploader:
    def __init__(self, yd_token):
        self.token = yd_token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_folder(self, path):
        folder_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': path}
        response = requests.put(folder_url, headers=headers, params=params)
        return response.status_code

    def check_folder(self, path):
        folder_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': 'disk:/'}
        data = requests.get(folder_url, headers=headers, params=params).json()
        items = data['_embedded']['items']
        for item in items:
            if item['type'] == 'dir':
                files_list.append(item['name'])
        if path in files_list:
            return 'success'
        else:
            return 'no such folder'





if __name__ == '__main__':
    uploader = YaUploader(yd_token)
    print(uploader.create_folder('2'))
    print(uploader.check_folder('2'))



