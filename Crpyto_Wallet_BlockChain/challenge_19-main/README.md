# challenge_19

The goal of this challenge was to determine the cost in ethers for a specific employee based on their hourly rate.
After calculating the cost based on hours selected, we perform a transaction through our local blockchain to the employees account.

Steps: 
  1. We first imported the required libraries which include: streamlit, dataclasses, typing, web3.
  2. Select an employee from the list.
  3. Update how many hours the employee worked or needs to work.
  4. Multiply the hours by the amount of ether they charge per hour.
  5. Execute the transaction of sending them the ether payment.
    
Code Explanation:    
Below is the explanation of some of the important lines of code:

  1."from crypto_wallet import generate_account, get_balance, send_transaction"
     This imports important functions from the crypto_wallet.py file.
     
  2. generate_account() function:
     This function is responsible for creating our wallet instance by using the mnemonic provided to us by our local Ganache server.
     It generates our public and private keys, creates our account using our private key, and returns our created account.
  
  3. get_balance() function:
     This returns the balance from our account.  We first get the wei value, calculate it to ether, and return the ether value.
     
  4. send_transaction() function:
     Responsible for: 
        1. calculating our ether back to wei because transactions are handled in wei.
        2. Estimate the has estimate that will be required for our transaction.  Gas is the estimated cost to mine a transaction.
        3. Create the transaction object which includes the perameters that tells it from who, to who, the amount, and the gas estimate, and the nonce which is the        total number of transactions from this account.
        4. Signs the transaction using our private key and sends the transaction to the chain to the mining que.
   
   5. candidate_database variable: This dictionary holds 4 different employees and their respective informations.
   
   6. get_people() function:
      This populates each employee to our front end by loop through the candidate_database dictionary and people list, and outputs their information and photo using    the streamlite st.write function.
      
      
   7.  "wage = hours * candidate_database[person][3]"
       This calculates the wage by multiplying the selected hours with the employees hourly rate.
   
   8. if st.sidebar.button("Send Transaction"):
          transaction_hash = send_transaction(w3,account,candidate_address,wage)
          st.sidebar.markdown("#### Validated Transaction Hash")
          st.sidebar.write(transaction_hash)
          st.balloons()
       
       This creates a button.  When clicked we exectute the send_transaction function which takes the provider, account, the address and total wage as its perameters.
        After the transaction has been completed, we get a verifaction on the sidebar of the streamlit front-end and balloons are shown using the streamlits built in function st.balloons(). 
    
  
