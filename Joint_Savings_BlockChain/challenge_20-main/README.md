# challenge_20
Columbia Fintech Challenge 20


About:
  In this challenge we created a smart contract which holds two accounts.
  The contract holds information including the account numbers, withdrawal info, the account balance.
  The contract allows us to perform actions such as depositing and withdrawing ether.
  
  
  
Explanation of key lines of code:

  "pragma solidity ^0.5.0;"
    This line tells the code which version of the solidty compiler to use.
    
   "address payable accountOne;
    address payable accountTwo;
    address public lastToWithdraw;
    uint public lastWithdrawAmount;
    uint public contractBalance;"
      These are our variables which holds its respective information.  The "address" datatype tells the code that this variable will hold the ethereum address. 
      "payable" allows us access to send ether to this address.
      
   "function withdraw(uint amount, address payable recipient) public" 
      This function takes 2 perameters: An unsigned int and payable address.
      it is responsible for withdrawing from either of the two accounts.
      To ensure unauthorized access we used a require statement which checks to see if the recipient is equal to either accounts.
      after withdrawal, the account balance is updated.
   
    "function deposit() public payable"
      This function allows us to deposit in to the account.  The "public payable" tells the code that this function can be accessed from outside the scope of this 
      contract and can accept ether.
      
      
      
     "function setAccounts(address payable account1, address payable account2) public"
        This function is responsible for settings the account addresses before we perform any other functions on them.
        
        
      "function() external payable {}"
        This is a fall-back function incase the user doesnt use the deposit function.   This allows the contract to store ether. 
       
     
      
    
  
