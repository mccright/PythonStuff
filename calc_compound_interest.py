#!/usr/bin/python3

import sys
import getopt



# Source resources:
# https://www.statology.org/compound-interest-in-python/
# https://www.enki.com/post/how-to-calculate-compound-interest-in-python
def calculate_compound_interest(principal: float, interest_rate: float, times_compounded: int, years_duration: int) -> float:
    """
    INPUTS:
    principal = the initial deposit or loan amount
    interest_rate = annual interest rate in decimal form
    times_compounded = number of compounding periods per year
    years_duration = number of years the money is invested or borrowed
    CALCULATION:
    A = principal(1 + interest_rate/times_compounded)^times_compounded*years_duration
    RETURNS:
    amount = future value of the investment or loan, including interest
    """
    amount = principal * (1 + interest_rate/times_compounded)**(times_compounded*years_duration)
    # or use python's pow() function:
    # amount = principal*(pow((1+interest_rate/times_compounded), times_compounded*years_duration))
    return amount


def main(argv):
    # From: https://github.com/mccright/PythonStuff/blob/main/githubfilestree.py
    if sys.version_info < (3, 10):
        raise Exception("Use only with Python 3.10 or higher")
    
    principal: float = ''
    interest_rate: float = ''
    times_compounded: int = ''
    years_duration: int = ''
    

    if not (sys.argv[1:]):
        print('Calculate future value of an investment or loan, including interest.')
        print('Inputs required: -p <principal> -r <interest_rate> -t <times_compounded> -y <years_duration>')
        """
        principal = the initial deposit or loan amount
        interest_rate = annual interest rate in decimal form
        times_compounded = number of compounding periods per year
        years_duration = number of years the money is invested or borrowed')
        """
        sys.exit(2)

    try:
        opts, args = getopt.getopt(argv, 'hp:r:t:y:', ['principal=','rate=','times=','years='])
    except getopt.GetoptError as err:
        print(err)
        print('\nCalculate future value of an investment or loan, including interest.')
        print(f'{sys.argv[0] } -p <principal> -r <interest_rate> -t <times_compounded> -y <years_duration>')
        sys.exit(2)

    try:
        for opt, arg in opts:
            if opt == '-h':
                print('\nCalculate future value of an investment or loan, including interest.')
                print(f'{sys.argv[0] } -p <principal> -r <interest_rate> -t <times_compounded_per_year> -y <years_duration>\n')
                sys.exit()
            elif opt in ("-p", "--principal"):
                principal = float(arg)
            elif opt in ("-r", "--rate"):
                interest_rate = float(arg)
            elif opt in ("-t", "--times"):
                times_compounded = int(arg)
            elif opt in ("-y", "--years"):
                years_duration = int(arg)
    except Exception as err:
        print(err)
        print('\nCalculate future value of an investment or loan, including interest.')
        print(f'{sys.argv[0] } -p <principal> -r <interest_rate> -t <times_compounded> -y <years_duration>\n')
        sys.exit(2)


    """
    principal: float = ''
    interest_rate: float = ''
    times_compounded: int = ''
    years_duration: int = ''
    """
    
    total_amount = calculate_compound_interest(principal, interest_rate, times_compounded, years_duration)
    print(f"${principal:,.2f} at an interest rate of {interest_rate} compounded {times_compounded} times per year for {years_duration} years = ${total_amount:,.2f}")
    interest_earned = total_amount - principal
    print(f"${total_amount:,.2f} - ${principal:,.2f} = ${interest_earned:,.2f} interest.\n")

if __name__ == '__main__':
    main(sys.argv[1:])
    

    """
    Think about using argparse instead of getopts:
    For example:  
        https://github.com/mccright/PythonStuff/blob/main/lottery_numbers/PowerBall-MegaMillions.py
      
    python get user input from command line
    https://duckduckgo.com/?ia=web&origin=funnel_home_website&t=h_&q=python+get+user+input+from+command+line&chip-select=search

    """
