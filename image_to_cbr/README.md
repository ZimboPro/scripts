# Image to cbr creator 
## What is a *cbr* file
 
A cbr file is actually a zip file where the extension is *.cbr* instead of *.zip*. 
A cbr file is used with comic book viewers instead of having to view each image 
individualy. 

## How it works

The scripts accepts the absolute path of the folder containing the image. It will 
rename all the files to 3 digits with 0 as placeholders. After that is done, it will 
zip those files to the same name as the folder and place it in the parent folder. 

## NOTE
This script requires python3