import vk_api
from vk_api import audio
import time
import os

class GetAudioVK():
    def auth_vk(self, username, password, my_id):
        try:
            self.vk_session = None
            self.vk_session = vk_api.VkApi(login=username, password=password)
            self.vk_session.auth()
            self.vk = self.vk_session.get_api()
            self.download_refresh(my_id)
        except vk_api.exceptions.Captcha as captcha:
            self.urlCaptcha = captcha.get_url() # Получить ссылку на изображение капчи
            self.otvet = input("Enter key: ")
            captcha.try_again(self.otvet)

    def download_refresh(self, my_id):
        if self.vk_session is not None:
            vk_audio = audio.VkAudio(self.vk_session)
            time_start = time.time()
            list_audio = vk_audio.get(owner_id=my_id)
            os.remove("music.txt")
            file = open("music.txt", "a", encoding="utf-8")
            for i in list_audio:
                try:
                    file.write(str(i["url"]) + "\n")
                    file.write(str(i["title"]) + "\n")
                    file.write(str(i["artist"]) + "\n")
                except Exception as e:
                    file.write("Undefined_Except_Title\n")
                    file.write("Undefined_Except_Artist\n")
            file.close()

            time_finish = time.time()
            print("Time seconds:", time_finish - time_start)
        else:
            print("Error!")