REM Converts all images from one format into the .jpg file
REM Requires ImageMagick 7 installed and in PATH env
REM Is a simple enough script, simply iterates through
REM all of the files provided

for %%f in (imports/images/*) do (
       magick.exe convert "imports/images/%%~nf%%~xf" "exports/%%~nf.jpg"
)