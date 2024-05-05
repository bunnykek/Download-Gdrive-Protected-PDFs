import re
import requests
import os
import argparse
import img2pdf


parser = argparse.ArgumentParser(description='Google-drive read-only pdfs downloader.')

parser.add_argument('fileid', type=str)
args = parser.parse_args()
document_id = args.fileid
tokenRx = re.compile(r"https://drive\.google\.com/viewer2/prod-\d{2}/meta\?ck\\u003ddrive\\u0026ds\\u003d(.+?)\",")
fileNameRx = re.compile(r"itemJson: \[null,\"(.+?)\"")


if not os.path.exists("temp"):
    os.makedirs("temp")
if not os.path.exists("pdfs"):
    os.makedirs("pdfs")

session = requests.Session()
response = session.get(
    f'https://drive.google.com/file/d/{document_id}/view',
)

tokenSearch = tokenRx.search(response.text)
url_token = tokenSearch[1]
nameSearch = fileNameRx.search(response.text)
file_name = nameSearch[1][:-4]
# print(file_name)
os.makedirs(os.path.join("temp", file_name))
print("Filename:", file_name)


print("Downloading pages...")
for i in range(999):
    image_url = f"https://drive.google.com/viewer2/prod-01/img?ck=drive&ds={url_token}&authuser=0&page={i}&skiphighlight=true&w=1600&webp=true"
    imgRes = session.get(image_url)
    if imgRes.status_code != 200:
        print(f"Downloaded {i} pages.")
        break
    with open(os.path.join("temp", file_name, f"{str(i).zfill(3)}.png"), "wb+") as f:
        f.write(imgRes.content) 

print("Merging the pages into a single PDF file.")
dirname = os.path.join("temp", file_name)
imgs = []
for fname in os.listdir(dirname):
	if not fname.endswith(".png"):
		continue
	path = os.path.join(dirname, fname)
	if os.path.isdir(path):
		continue
	imgs.append(path)
with open(os.path.join("pdfs", f"{file_name}.pdf"),"wb") as f:
	f.write(img2pdf.convert(imgs))
print(f"PDF has been saved to {os.path.join("pdfs", f"{file_name}.pdf")}")


