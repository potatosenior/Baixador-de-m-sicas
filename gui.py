import PySimpleGUI as sg
    
def gui():
  sg.theme('DarkRed2') 
  labelSize = (13, 1)
  inputSize = (45, 1)
  buttonSize = (10, 1)
  layout = [
    [
      sg.Text("Pasta de destino", size=labelSize),
      sg.In(size=inputSize, enable_events=True, key="-FOLDER-", disabled=True, text_color="#000", background_color="red"),
      sg.FolderBrowse(button_text="Selecionar", size=buttonSize),
    ], 
    [
      sg.Text("Link da musica", size=labelSize), 
      sg.InputText(key="url", size=inputSize),
      sg.Button("Procurar", key="search", size=buttonSize)
    ],
    [
      sg.Text("", key="error", size=(40, 1), text_color="#000", font=("Arial", 16))
    ],
    [sg.HorizontalSeparator()],
    [sg.Text("", key="music_title", size=(50,2), font=("Arial", 15), visible=False)],
    [sg.Image(key="-IMAGE-")],
    [sg.Button("Baixar", key="download", visible=False, size=(70, 1), button_color=('green', 'white'))],
    [sg.Text("Música baixada com sucesso!", key="sucess", size=(30,1), font=("Arial", 10), visible=False, text_color="#b6eb7a")],
    [
      sg.Button("SAIR", key="exit", size=buttonSize)
    ],
  ]

  # output_column = [
  #   [sg.Text("", key="music_title", size=(30,1), font=("Arial", 15), visible=False)],
  #   [sg.Image(key="-IMAGE-")],
  #   [sg.Button("Baixar", key="download", visible=False)],
  #   [sg.Text("Música baixada com sucesso!", key="sucess", size=(30,1), font=("Arial", 10), visible=False, text_color="#b6eb7a")]
  # ]

  # layout = [
    
  #   [input_column],
  #   # sg.HorizontalSeparator(),
  #   [output_column]
    
  # ]

  window = sg.Window(title="Baixar musicas", layout=layout, resizable=True)

  return window

if __name__ == "__main__":
  gui()