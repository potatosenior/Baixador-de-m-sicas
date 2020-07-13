from pytube import YouTube

def get_music(url):
  try:
    music = YouTube(url)
  except Exception as inst:
    return False
  else:
    return music

def donwload_music(music, path):
  try:
    music.streams.get_audio_only().download(path)
  except:
    return False
  else:
    return True

if __name__ == "__main__":
  music = get_music("https://www.youtube.com/watch?v=Px_KohohYT8")
  print(music.title, music.thumbnail_url)