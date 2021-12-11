# Experimenting with downloading xlsx files from an API  

In this case, I'll initially experiment with a WhiteSourceSoftware API.  

The initial goal being to accept the data and write it to a file that will work with Microsoft Excel, or open source equivalents.  
A follow-on feature may be to convert the xlsx formatted-bytes to simple csv and then write that file for enhanced portability.  Challenges: The expected data includes columns with quotes, tics, *multiple lines* with carriage returns and line feeds, and dates in number of different date formats.  



Initial reading:  
* [https://www.geeksforgeeks.org/convert-excel-to-csv-in-python/](https://www.geeksforgeeks.org/convert-excel-to-csv-in-python/)  
* [https://datatofish.com/excel-to-csv-python/](https://datatofish.com/excel-to-csv-python/)  
* [https://github.com/dilshod/xlsx2csv](https://github.com/dilshod/xlsx2csv)  
* []()  
* ...and if all else fails, convert the xlsx files with PowerShell: [https://docs.microsoft.com/en-us/answers/questions/597931/convert-xlsx-to-csv-using-powershell.html](https://docs.microsoft.com/en-us/answers/questions/597931/convert-xlsx-to-csv-using-powershell.html)  
