# Image to cbr creator 
## What is a *cbr* file
 
A cbr file is actually a zip file where the extension is *.cbr* instead of *.zip*. 
A cbr file is used with comic book viewers instead of having to view each image 
individualy. 

## How it works

The scripts accepts the absolute path of the folder containing the images. It will 
rename all the files to 3 digits with 0 as placeholders. After that is done, it will 
zip those files to the same name as the folder and place it in the parent folder. 

## Example

There are 2 options for the script, *single* or *multiple* folders. The single folder 
option will only zip a single folder's contents while the multiple folder option 
will loop through multiple folders and zip their respective contents.

### Sinlge folder option

eg *python3 creator.py -s ~/Documents/1* 
or 
*python3 creator.py --single ~/Documents/1* 

It requires that the folder name containing the images is a number and that the 
images are numbers as well.

>*1* 
>>*-1.jpg*  
>>*-2.jpg*  
>>*...*  

### Multiple folder option

eg *python3 creator.py -m ~/Documents/1-20* 
or 
*python3 creator.py --multiple ~/Documents/1-20*

It requires that the parent folder name containing subfolders with the images is the 
lowest value folder name *-* the highest value folder name and the subfolders have the
same requirements as the single folder option
eg *1-20* when the folders contains the folders *1* to and including *20*

>*1-20*  
>>*1*  
>>>*1.jpg*  
>>>*2.jpg*  
>>>*...*  
>>*2*  
>>>*1.jpg*  
>>>*2.jpg*  
>>>*...*  
>>*...*  

### Output

Once executed it will display the full filepath of the folder being zipped and will either
display *Single folder zipped successfully!* or *Multiple folders zipped successfully!* 
depending on the option chosen once finished

## NOTE
This script requires python3