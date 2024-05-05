# Gdrive read-only PDF Downloader
~Browser's console code to download the read-only Gdrive pdfs.~ 
> [!NOTE]
> Google has now implemented `TrustedScriptURL` in the drive web app, Hence we cannot import third party js libraries via cdns which was responsible for compiling the pages collection into a pdf. Therefore I have written a python script instead.

A python script for downloading the read-only gdrive pdfs.

When the Download, print and copy has been disabled for a Google drive shared PDF file then you can simply run this python script to download that file.

## Installation
```
git clone https://github.com/bunnykek/Download-Gdrive-Protected-PDFs
cd Download-Gdrive-Protected-PDFs
pip install -r requirements.txt
```

## Usage
```
py download.py fileid
```
The file will be saved in the `/pdfs` directory.

#### If you like my work then please do drop a star. Thanks.
