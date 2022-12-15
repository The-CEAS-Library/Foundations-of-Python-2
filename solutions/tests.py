"""
Aidan Sorensen 12/15/2022


I totally remade my original idea for checking functions. The kaggle codebase was awesome, but not practical for me to implement. There was no need
to track clicks, or make an extremely robust abstraction of classes to make hints randomized or special quips when you answer on the first try or
something. So I stripped it down and each exercise is represented by a single class. 

Each class will at minimum have a check() and a solution() func. I also have a class variable for a single hint. This could easily be compounded on if it were turned into a function with multiple hints that randomly select
or something fun along those lines. 

note: the docstring for each class is its solution. I remembered a fun little way of printing out docstrings that maintains indents and it was helpful to literally
print the code solution to the screen for the user. This ran into some issues with the longer code snippets, where it wouldn't print it all to the screen. Maybe 
there is an elegant solution to this, but for now I have only implemented two of the exercises in intro part 2 anyway. This should be super easy to add exercises to,
and should work for pretty much any problem.

Another distinct thing that I did was made DNAtoRNA robust, but I didn't do that for SixPlusTwo. I just wanted to show the difference in code. SixPlusTwo assumes you use
my name, "Aidan Sorensen" and operates off of a single conditional that just checks if the 6+2 is sorensan. But DNAtoRNA takes the input DNA string, your resultant RNA
string, and computes its own RNA string and compares the two. Either way is technically fine, but as the questions get more complex it will be more important for the 
check() function to be robust so that workshop attendees don't get frustrated with the check() not behaving.


ALSO! If this actually starts getting used, this should totally get rid of the need for a 'solutions.ipynb'. All the solutions could be accessed via the func calls 
from each exercises class. But that would take a while.
""" 


class SixPlusTwo():
    """
Solution:

if len(last_name)>=6:
    sixplus2 = last_name[0:6] + first_name[0] + first_name[-1]
else:
    sixplus2 = last_name + first_name[0:(6-len(last_name)+1)] + first_name[-1]

# make sure the 6 + 2 is in lowercase, then print it to the screen.(printing is not required for the solution)
sixplus2 = sixplus2.lower()
print(sixplus2)
"""
    _var = 'sixplus2'
    hint = "For length of the last name is >=6, sixplus2 = last_name[0:?] + first_name[0] + first_name[?]"
    

    def check(sixplus2):
        # this check function simply checks if the variable input to it matches sorensan...
        # it is not intended to be more robust than that. technically, I could write it to take first and last name, then check based off that computation. 
        if sixplus2 == "sorensan":
            print("\033[1;32mCorrect!")
        else:
            print("\033[1;31mIncorrect... Something isn't quite right.")
    
    def solution():
        print(SixPlusTwo.__doc__)
        # I have the solution as a docstring to preserve formatting .... idk if this is too hacky or not but it works


class DNAtoRNA():
    """
# Take input for DNA string and store in a variable DNA_string
DNA_string = input("Give the input DNA Code : ")

# Intialize the RNA output as an empty string
RNA_string = ''

# Use "for" loop to traverse the DNA string. Use "If..elif..else" sub block to check and concactenate the appropriate letter 
# to RNA_string.
# Use "else" block in the "If..elif..else" sub block to output an error message and break if a diffrent letter is encountered

for i in DNA_string.upper():
    # the upper() method is used to make our program case insensitive
    if i == 'G':
        RNA_string = RNA_string + 'C'
    # Continue the "elif" blocks of the "If..elif..else" block for the other letters
    elif i == 'C':
        RNA_string = RNA_string + 'G'
    elif i == 'A':
        RNA_string = RNA_string + 'T'
    elif i == 'T':
        RNA_string = RNA_string + 'A'
    # Complete the "If..elif..else" block with "else" block for an error message assigned to RNA_string 
    # break out of the loop    
    else: 
        RNA_string = 'Incorrect DNA string'
        break
else:
    # This else is attached to the for loop
    print('Done with Translation')

print('DNA output: ', RNA_string)
"""
    _var = 'DNAtoRNA'
    hint = "some good hint for this exercise... figure that out later just write the tests"
    

    def check(input, output):
        # I wrote this check function to actually compute the RNA string given the input. important since part of the exercise is to take user input, 
        #  so the values SHOULD be able to be different each time.
        rna_str = ''
        for i in input.upper():
            # the upper() method is used to make our program case insensitive
            if i == 'G':
                rna_str = rna_str + 'C'
            # Continue the "elif" blocks of the "If..elif..else" block for the other letters
            elif i == 'C':
                rna_str = rna_str + 'G'
            elif i == 'A':
                rna_str = rna_str + 'T'
            elif i == 'T':
                rna_str = rna_str + 'A'
            # Complete the "If..elif..else" block with "else" block for an error message assigned to RNA_string 
            # break out of the loop    
            else: 
                rna_str = 'Incorrect DNA string'
                break

        if rna_str == output:
            print("\033[1;32mCorrect!")
        else:
            print("\033[1;31mIncorrect... Something isn't quite right.")
    
    def solution():
        print(DNAtoRNA.__doc__)
        # I have the solution as a docstring to preserve formatting .... idk if this is too hacky or not but it works



