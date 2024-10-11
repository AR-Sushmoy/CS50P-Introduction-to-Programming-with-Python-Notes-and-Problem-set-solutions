'''
Question: Implement a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to ☹️ (otherwise known as a slightly frowning face). All other text should be returned unchanged.

Then, in that same file, implement a function called main that prompts the user for input, calls convert on that input, and prints the result.
'''


def main():
    userText = input(
        "Say anything using either a sligthly smiling face \":)\" or frowing face \":(\" emoticon at the end: ")
    print(convert(userText))


def convert(emoticon):
    text = emoticon
    text = text.replace(":)", "🙂").replace(":(", "☹️")
    emoticon = text
    return emoticon

main() 

'''
Explanation:
Istead of conditional checks and multiple replace calls:
    > We create a variable new_text to store the updated string.
    > We call replace twice, once for each emoticon, sequentially:
        >> First, we replace all occurrences of ":)" with "🙂".
        >> Then, we replace all remaining occurrences of ":(" with "🙁" in the updated new_text.

By replacing each emoticon separately, we guarantee that the order of the replacements is maintained.
This ensures that ":)" is always replaced with "🙂" and ":(" is always replaced with "🙁", regardless of their original positions in the input string.
'''    
    
    
 

'''
##### An example of Replace multiple characters in a String in Python

string = "boddy!hadz@com"
string = string.replace("!", "-").replace("@", "_")

print(string)
'''

