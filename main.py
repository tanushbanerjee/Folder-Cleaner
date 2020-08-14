import os

def createNotExists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}")


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
medias = [files for file in files if os.path.splitext(file)[1].lower() in mediaExts]

others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in mediaExts) and (ext not in docsExts) and (ext not in imgExts) and os.path.isfile(file):
        others.append(file)

print(others)


move("Media", medias)
move("Docs", docs)
move("Images", images)
move("Other", others)
