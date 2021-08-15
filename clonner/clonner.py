from requests import get
from bs4 import BeautifulSoup
from os import getcwd, path


class Clonner:
    def __init__(self, url=str):
        self.url = url

    def get_content_file(self, path=str):
        content = open(path, "r")
        return content.read()

    def replace_url_redirect_frontend(self,):
        file_replace_uri = open(getcwd() + "/clonner/scripts_client/getValues.txt",
                                "r").read().replace("url_clone_site", f'"{self.url}"')
        return file_replace_uri

    def save_file_html(self, html_clone, path=str):
        with open(path, "w") as myfile:
            myfile.write(str(self.get_content_file(getcwd() + "/clonner/scripts_client/getSocketIo.txt") +
                         html_clone + self.replace_url_redirect_frontend()))
        myfile.close()

    def clone(self):
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
            }
            page_mobile = get(url=self.url, headers=headers)
            page_desktop = get(url=self.url)
            html_clone_mobile = BeautifulSoup(
                page_mobile.content, "html.parser")
            html_clone_desktop = BeautifulSoup(
                page_desktop.content, "html.parser")

            self.replace_url_redirect_frontend()
            # SAVE FILE DESKTOP
            self.save_file_html(html_clone_desktop.prettify(),
                                path="./templates/desktop_clone.html")
            # SAVE FILE MOBILE
            self.save_file_html(html_clone_mobile.prettify(),
                                path="./templates/mobile_clone.html")
            return "Successfully cloned website 🤖"
        except Exception as e:
            return e
