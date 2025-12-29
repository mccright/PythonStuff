# Generate Candidate Powerball and Mega-Millions Plays  


This script was just an exercise in response to a query by a relative.  
It is not unique. There are other scripts available for the same purposes on Github and elsewhere.  
If you want something like this, maybe try writing your own.  

This script spits out sets of numbers matching the rules for [Powerball](https://en.wikipedia.org/wiki/Powerball) and 
[Mega-Millions](https://en.wikipedia.org/wiki/Mega_Millions) games.  
It uses the Python module ```secrets``` to generate values having 
*maximum* entropy (think '*random*') which are then used to assemble each play.  
No need to think about your numbers, nor worry about the Lottery empire 
or someone else generating your numbers for you.  

## Some of the programming challenges in this exercise  
* Accepting user's command line input specifying the number of plays (default to one).  
* Set a *sane* maximum number of plays to help protect system resources (e.g., using the script to generate 2 billion plays would, under most circumstances, be unproductive and should be resisted).  
* Specify the universe of candidate integers for each grouping that makes up a Powerball or Mega-Millions game play.  
* With a *reasonable* level of [entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory)), "randomly" select numbers from the "universes" specified above for each Powerball or Mega-Millions game play.  
* Ensure that there are no duplicates in the "first five" grouping.  
* Sort the "first five" grouping low to high.  
* Present the final Powerball or Mega-Millions game play on the terminal.  
* "Catch" and handle exceptions where *needed*.

### Example Output  
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

### There is also a way to do this on the bash shell command line:  
[shuf](https://www.mankier.com/1/shuf) does the heavy lifting in our one-liner.  And this old StackOverflow answer by Dan Fego was also helpful for dealing with shuf output: https://stackoverflow.com/a/8714446  
```terminal
$ echo -n "Powerball: " && shuf -i 1-69 -n 5 |  awk -vORS=' ' '{ print $1 }' && echo -n '- ' && shuf -i 1-26 -n 1
Powerball: 67 17 25 21 68 - 7
$ echo -n "Mega-Millions: " && shuf -i 1-70 -n 5 |  awk -vORS=' ' '{ print $1 }' && echo -n '- ' && shuf -i 1-25 -n 1
Mega-Millions: 37 43 58 31 34 - 4
```
or simply:  
```terminal
echo -n "Powerball: " && shuf -i 1-69 -n 5 |  awk -vORS=' ' '{ print $1 }' && echo -n '- ' && shuf -i 1-26 -n 1 && echo -n "Mega-Millions: " && shuf -i 1-70 -n 5 |  awk -vORS=' ' '{ print $1 }' && echo -n '- ' && shuf -i 1-25 -n 1
Powerball: 19 27 29 50 30 - 3
Mega-Millions: 20 61 70 49 38 - 11
```
Wrap that code in a conditional to ensure we receive user input -- an ```if; then``` and ```for (<a positive integer>)``` and then the one-liner above ```else; tell the user how to use the script```  
[lottery_numbers.sh](lottery_numbers.sh).  


## Reference  
Powerball and Mega-Millions are played by selecting six numbers.  
Powerball:     Five numbers between 1-69 and one “Powerball” number between 1-26.  (*Approximate odds of a jackpot are [1 in 292,201,338](https://www.usamega.com/powerball/faq)*)  
Mega-Millions: Five numbers between 1-70 and one “Mega Ball” number between 1-25.  (*Approximate odds of a jackpot are [1 in 290,472,336](https://www.usamega.com/mega-millions/faq)*)  

See [Powerball](https://www.usamega.com/powerball/faq) and 
[Mega-Millions](https://www.usamega.com/mega-millions/faq) FAQs for more information.  

Each Powerball play is $2.00 and each Mega-Millions play is $5.00 (*and have options that have their own additional costs*)  

## Caution  
REMEMBER: **The odds are not in your favor**. You are gambling when you buy tickets and there is no guarantee you'll win any money. Playing the lottery is only entertainment. It is described by [Salil Mehta](https://statisticalideas.blogspot.com/2012/11/statistical-ideas-website.html) as "[a tax on people who may not really understand what they’re doing](https://www.nytimes.com/2024/03/29/business/lottery-jackpot-megamillions-powerball.html)" followed by "Unquestionably, if you need the money, don’t waste it on a lottery ticket. Use it to pay the bills, or save it and invest it."  

https://en.wikipedia.org/wiki/Powerball#Power_Play  
https://en.wikipedia.org/wiki/Mega_Millions#Winning_and_probability  
This is also true for all commercial gambling.  See:  
Gambling FAQ: https://yourlifeiowa.org/health-and-wellness-gambling#frequently-asked-questions  
And the "Payout Wizard" at: https://yourlifeiowa.org/health-and-wellness-gambling#frequently-asked-questions  

But...  
### Some of the Biggest Jackpots in the U.S.  
* $2.04 billion: Powerball Won Nov. 7, 2022, in California  
* $1.817 billion: Powerball Won Dec. 24, 2025 in Arkansas  
* $1.787 billion: Powerball Won Sept. 6, 2025, in Missouri and Texas  
* $1.765 billion: Powerball Won Oct. 11, 2023, in California  
* $1.602 billion: Mega Millions, Aug. 8, 2023, Florida  
* $1.6   billion: Powerball No winner yet  
* $1.586 billion: Powerball Won Jan. 13, 2016, in California, Florida and Tennessee  
* $1.537 billion: Mega Millions,Oct. 23, 2018, South Carolina  
* $1.348 billion: Mega Millions Jan. 13, 2023, Maine  
* $1.337 billion: Mega Millions July 29, 2022, in Illinois  
* $1.326 billion: Powerball Won April 6, 2024, in Oregon  
* $1.269 billion: Mega Millions Dec. 27, 2024, California  
* $1.08 billion: Powerball Won July 19, 2023, in California  
* $842.4 million: Powerball Won Jan. 1, 2024, in Michigan  
* $768.4 million: Powerball Won March 27, 2019, in Wisconsin  
* $758.7 million: Powerball Won Aug. 23, 2017, in Massachusetts  
