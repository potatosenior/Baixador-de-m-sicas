from PySimpleGUI import WIN_CLOSED
from utils import *
from get_music import *
from gui import gui

if __name__ == "__main__":
  window = gui()

  def error(error):
    window.Element("error").Update(value=error)

  def download_visible(bool=True):
    window.Element('music_title').Update(visible=bool)
    if not bool:
      window.Element('-IMAGE-').Update('')
    window.Element('download').Update(visible=bool)
    window.Element('sucess').Update(visible=False)

  while True:

    event, values = window.read()

    if event == "search":
      url = values["url"]
      download_visible(False)

      if not url:
        error("Insira um link!")
      else:
        error("")
        music = get_music(url)
        if not music:
          error("Link inválido!")
          continue

        download_img(music.thumbnail_url)
        convert_to_png()
        window["-IMAGE-"].update(filename="thumb.png")
        window.Element("music_title").Update(value=music.title)
        delete_thumb()
        download_visible()
    
    if event == "download":
      path = values["-FOLDER-"]
      music = get_music(url)

      if not path:
        error("Seleciona a pasta de destino do download!")
      else:
        error("")
        download_visible()
        if donwload_music(music, path):
          window.Element('sucess').Update(visible=True)


    # End program if user closes window or
    # presses the OK button
    if event == "exit" or event == WIN_CLOSED:
      break
  
  window.close()