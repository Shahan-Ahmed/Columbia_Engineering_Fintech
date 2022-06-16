# Fintech_mod_18_challenge
Module 18 challenge

In this challange, we used our skills learned in module 18 to:

1. To define objects known as dataclasses.  This datatype can hold anything from variables, arrays, functions etc.

2. We learned how to hash data.  A hash takes any size data and converts it to a fixed length output.  In our case we used the sha256 hashing method which takes an input and outputs a string 256 bits long.

3. Used streamlit which allows us to quicly make a front-end web application which communicates without python code.  We created an interface which allows the user to    input data which we hashed and added each new input to the chain.  The front-end shows the user the ledger as it is updated in real-time.

4. We chained blocks together.  These chains include the hash of the previous blocks data to ensure the integrity of each block.  If one hash of a block changes, this causes a domino affect of all the blocks to have the invalid has of the previous block which invalidates the entire block.




Steps taken:

1. We imported our required libraries.  In this case, we needed the streamlit, dataclasses, typing, datetime, pandas and hashlib libraries.

2. We defined a class named 'Record'.  This class includes information about the sender, receiver and the amount to being transacted.

3. We defined the 'Block' class.  This class includes an instance of the 'Record' class itsself and other data such as the ID of the creator, the hash of the previous block and timestamp of its creation.  Inside this class is also the function which hashes all the attributes and returns the hash value.

4. We defined the 'Pychain' class.  This class, before adding new blocks to the chain, performs the following proccesses: 
   a) In the proof of work, we define how many zeros our pattarn must start with it.  By doing this, we control the level of difficulty and potential time it may for the       computer to find the solution.
   b) we addded a new variable of type integer called 'nonce' - Until we find the right number of zeros the nonce is incremented by one until we find the required trail of zeros.
   c) Once the required number of zeros are achieved, then the block is added to the chain.
   
5.  We created an interface using streamlit. The interface is defined in this order:
    -  We used a caching function which allows the current page to remember its current status until we close the browser.
    -  We defined an input field which will accept from the user the senders info.
    -  We defined an input field which will accept from the user the receivers info.
    -  We defined an input field which will accept from the user the amount to be transacted.

6. When the user clicks 'Add block', new block is created each one holding a new instance of the record class.  A genesis block was automatically created before hand so that we have a starting block.
7. The entire block is converted to a dataframe using the pandas library and then reflected on to the screen.
8. Finally, to validate that each block on the chain that we linked has not been tampered with and is valid, we added a button at the bottom of the page called 'Validate Chain'.  When the user clicks this button, the is_valid function in our pychain class is called to loop through the chain to ensure that the next chain has the correct hash of the previous chain.  It returns true or false.
