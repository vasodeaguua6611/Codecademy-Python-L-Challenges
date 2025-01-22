# match statements
# We use the match, case, and default keywords to define match-case statements in Python. The match statement is used to compare a value against a set of possible patterns. The case keyword is used to define the patterns to match against. The default keyword is used to define the default case when no other case matches.
# EXAMPLE
# match expression:  
#     case value_1:  
#         # code to execute when expression equals value_1  
#     case value_2:  
#         # code to execute when expression equals value_2  
#     case value_3:  
#         # code to execute when expression equals value_3  
#     case value_4:  
#         # code to execute when expression equals value_4  
#     case value_N:  
#         # code to execute when expression equals value_N  
#     case default:  
#         # code to execute when expression isn't equal to any of the values  


# In the above code, match is a keyword that marks the start of the match block. expression can be a variable, an arithmetic expression, a Boolean expression, or a Python object like a list, tuple, or string.
# The code inside a case block is executed for a single value of expression. For example, only if expression evaluates to value_1 will the code inside the case value_1 block be executed. If expression evaluates to value_2, then only the code inside the case value_2 block will be executed.
# Only one case block is executed in the entire match block for any given value of expression. Once a case block is executed, the program’s control flow moves out of the match block.
# The default block is always present at the end of the match block. If expression matches none of the values in other case blocks, the code inside case default is executed.

#EXAMPLE

user_name = "Dave"  
match user_name:  
    case "Dave":  
        print("Get off my computer Dave!")  
    case "angela_catlady_87":  
        print("I know it is you, Dave! Go away!")   
    case "Codecademy":  
        print("Access Granted.")  
    case default:  
        print("Username not recognized.")  
        #CC