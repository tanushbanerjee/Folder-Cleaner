import os

def createNotExists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


files = os.listdir()
files.remove('main.py')
print(files)

createNotExists('Images')
createNotExists('Docs')
createNotExists('Media')
createNotExists('Other')

imgExts = [".png", ".img", ".jpg", ".jpeg", ".ico"]
images = [files for file in files if os.path.splitext(file)[1].lower() in imgExts]

docsExts = [".txt", ".docx", ".doc", ".pdf", ".odt"]
docs = [files for file in files if os.path.splitext(file)[1].lower() in docsExts]

mediaExts = [".mp4", ".mp3", ".mkv", ".flv"]
media = [files for file in files if os.path.splitext(file)[1].lower() in mediaExts]


