# plus-minus-interpreter
a maths interpreter that handles addition, subtraction and brackets. 

#To-Do
add comments                   
make code neater, faster and more understandable.           
make multiplication and division?       

#How to use
download maths.py and run the program with python3. 

#How it works
The maths string is input, the spacecs are removed and all of the different tokens/symbols are separated (the function that does this also handles multiple digit numbers being separated).
The token list is then fed into a function that converts all of the numbers into members of the num class.
the list of tokens and number is then fed into a function that separates the brackets into separate lists within the list that holds all the tokens.
then this structure is fed into a function that converts all of the functions in the equation into instances of func_node.
the structure returned from this is the equivalent to an ast in an interpreter.
the ast is then 'run' by calling the get_value function on the return value of the previous function.
