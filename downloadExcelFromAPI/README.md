# Experimenting with downloading xlsx files from an API  

In this case, I'll initially experiment with a WhiteSourceSoftware API.  

The initial goal being to accept the data and write it to a file that will work with Microsoft Excel, or open source equivalents.  
A follow-on feature may be to convert the xlsx formatted-bytes to simple csv and then write that file for enhanced portability.  Challenges: The expected data includes columns with quotes, tics, *multiple lines* with carriage returns and line feeds, and dates in number of different date formats.  

