# Generate Candidate Powerball and Mega-Millions Plays  


This script was just an exercise in response to a query by a relative.  
It is not unique. There are other scripts available on Github and elsewhere.  
If you want something like this, maybe try writing your own.  

This script spits out sets of numbers matching the rules for Powerball and 
Mega-Millions games.  
It uses the Python module ```secrets``` to generate values having 
maximum entropy (think 'random') then used to assemble each play.  
No need to think about your numbers, nor worry about the Lottery empire 
or someone else generating your numbers for you.  

```terminal
user@LT01:/mnt/dev/lottery_numbers$ python3 PowerBall-MegaMillions.py --help
usage: PowerBall-MegaMillions.py [-h] [-n NUM_PLAYS]

Generate candidate Powerball and Mega-Millions plays

optional arguments:
  -h, --help            show this help message and exit
  -n NUM_PLAYS, --num_plays NUM_PLAYS
                        Generate this many candidate Powerball and Mega-Millions plays
user@LT01:/mnt/dev/lottery_numbers$ python3 PowerBall-MegaMillions.py -n 3
PowerBall: 4 5 22 36 47 + 3
Mega-Ball: 3 11 31 39 67 + 14
- - - - - - - - - - - - - - -
PowerBall: 16 35 50 53 66 + 3
Mega-Ball: 22 30 35 47 56 + 7
- - - - - - - - - - - - - - -
PowerBall: 24 28 31 49 62 + 1
Mega-Ball: 2 4 18 27 52 + 21
- - - - - - - - - - - - - - -
user@LT01:/mnt/dev/lottery_numbers$ 
```

## Reference  
Powerball and Mega-Millions are played by selecting six numbers.  
Powerball:     Five numbers between 1-69 and one “Powerball” number between 1-26.  
Mega-Millions: Five numbers between 1-70 and one “Mega Ball” number between 1-25.  

See [Powerball](https://www.usamega.com/powerball/faq) and  
[Mega-Millions](https://www.usamega.com/mega-millions/faq)  

Each play is $2.00  

REMEMBER: **The odds are not in your favor**.  
https://en.wikipedia.org/wiki/Powerball#Power_Play  
https://en.wikipedia.org/wiki/Mega_Millions#Winning_and_probability  
