"""
Description: Chatbot application.  Allows user to perform balance 
inquiries and make deposits to their accounts.
Author: ACE Department
Modified by: {Student Name}
Date: 2023-10-15
Usage: From the console: python src/chatbot.py
"""

## GIVEN CONSTANT COLLECTIONS
ACCOUNTS = {
    123456 : {"balance" : 1000.0},
    789012 : {"balance" : 2000.0}
}

VALID_TASKS = {"balance", "deposit", "exit"}

## CODE REQUIRED FUNCTIONS STARTING HERE:

def get_account() -> int:

    """
    This function is prompt the user for the account number and returns it 
    as an integer.
    This function is also try using try/catch block to catch an exception.
        
    Returns:
        int: returns a valid account number

    Exceptions:
        ValueError: raise an error message when non-numeric data entered or account
        number does not exist.
        """
    try:
        user_input = int(input("Please enter your account number:"))

    except ValueError:
        raise ValueError("Account number must be a whole number.")

    if user_input not in ACCOUNTS:
        raise ValueError("Account number entered does not exist.")

    return user_input

def get_amount() -> float:
    """
    This function is prompt the user to enter a valid amount and return it 
    as a float.
    This function is also try using try/catch block to catch an exception.

    Returns:
        float: returns a valid transaction amount

    Exceptions:
        ValueError: raise an error message when non-numeric amount entered or amount 
        is zero or negative.
    """
    try:
        user_transaction_amount_input = float(input("Enter the transaction amount: "))
        # if user_transaction_amount_input > 0 :
        #      return user_transaction_amount_input
    except ValueError:
          raise ValueError("Invalid amount. Amount must be numeric.")
    if user_transaction_amount_input <= 0:
           raise ValueError("Invalid amount. Please enter a positive number.")
    return user_transaction_amount_input

def get_balance(account : int) -> str:
      """
      This function is retrieving the balance of a specified account.
      
      Args:
          account (int): The account number
      Returns:
          str: Text with a message include account number and balance.
          Exceptions: Raise ValueError if account number does not exist.
      """
      if account not in ACCOUNTS:
           raise ValueError("Account number does not exist.")
      return f"Your current balance for account {account} is ${ACCOUNTS[account]["balance"]:,.2f}."

## GIVEN CHATBOT FUNCTION
## REQUIRES REVISION
"""
def chatbot():
    '''
    The main program.  Uses the functionality of the functions:
        get_account()
        get_amount()
        get_balance()
        make_deposit()
        user_selection()
    '''

    print("Welcome! I'm the PiXELL River Financial Chatbot!  Let's get chatting!")

    keep_going = True
    while keep_going:
        try:
            ## CALL THE user_selection FUNCTION HERE 
            ## CAPTURING THE RESULTS IN A VARIABLE CALLED
            ## selection:

            if selection != "exit":
                
                # Account number validation.
                valid_account = False
                while valid_account == False:
                    try:
                        ## CALL THE get_account FUNCTION HERE
                        ## CAPTURING THE RESULTS IN A VARIABLE 
                        ## CALLED account:

                        valid_account = True
                    except ValueError as e:
                        # Invalid account.
                        print(e)
                if selection == "balance":
                        ## CALL THE get_balance FUNCTION HERE
                        ## PASSING THE account VARIABLE DEFINED 
                        ## ABOVE, AND PRINT THE RESULTS:

                else:

                    # Amount validation.
                    valid_amount = False
                    while valid_amount == False:
                        try:
                            ## CALL THE get_amount FUNCTION HERE
                            ## AND CAPTURE THE RESULTS IN A VARIABLE 
                            ## CALLED amount:


                            valid_amount = True
                        except ValueError as e:
                            # Invalid amount.
                            print(e)
                ## CALL THE make_deposit FUNCTION HERE PASSING THE 
                ## VARIABLES account AND amount DEFINED ABOVE AND 
                ## PRINT THE RESULTS:


            else:
                # User selected 'exit'
                keep_going = False
        except ValueError as e:
            # Invalid selection:
            print(e)

    print("Thank you for banking with PiXELL River Financial.")
"""
    
"""
if __name__ == "__main__":
    chatbot()
"""
