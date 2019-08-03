REM Converts all images from one format into the .jpg file
REM Intended for use from versions Tudrme v1 to Tudrme v2
REM Requires ImageMagick 7 installed and in PATH env

for %%f in (imports/images/*) do (
       magick.exe convert "imports/images/%%~nf%%~xf" "exports/%%~nf.jpg"
)