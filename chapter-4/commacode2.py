# Project Description:

# Say you have a list value like this:
# spam = ['apples', 'bananas', 'tofu', 'cats']
# Write a function that takes a list value as an argument and returns
# a string with all the items separated by a comma and a space, with and
# inserted before the last item. For example, passing the previous spam list to
# the function would return 'apples, bananas, tofu, and cats'. But your function
# should be able to work with any list value passed to it.


#Please check commacode2.py for a more concise version of this program
spam = ['apples', 'bananas', 'tofu', 'cats']

def comma(list):
    result = ''
    for i in range(len(list)):
        #In the following line, list[:-1] will slice the list from begenning till the penultimate item in the list. It will return ['apples', 'bananas', 'tofu']
        result = ", ".join(list[:-1]) + " and " + list[-1] #for more detail on join function, visit http://www.tutorialspoint.com/python/string_join.htm
    return result

print(comma(spam))
