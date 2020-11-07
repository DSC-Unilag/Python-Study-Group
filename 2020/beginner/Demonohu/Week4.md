## My week 4 Submission

(https://repl.it/@demonohu/Week4#main.py)

I couldn't answer questions 1 and 3.

6849

### Charge Account Validation

- Firstly, your code for this task didn't run and I had to modify it before I could test it. 
- Secondly, you didn't provide the file containing the list of valid charge account numbers.
- Thirdly, the variable `charge_accounts` what is it? You never gave it a value though I guess and assume it is meant to be a list of lines of the above file.
- You made good use of comments which made reading your code easy to understand and pleasant to read, great job on that.
- Aside not opening a file and using an uninitialised variable, your solution for this task is correct so great job on that.
- One way you could improve your code is to convert each line in the file to integers instead of leaving them as a string. The same should be done to the user's input.


### File Analysis

- The way you created the set objects (both of them) was wrong. What you did, `set1 = set(line.strip() for line in open(file1))` would create a set of "characters" which i believe was not the intention.
- A valid way of doing this would be `set1 = set(word for word in open(file1).read().split())
- Again, you made good use of comments, thumbs up.
- Aside the above issue, your solution for this task is correct so great job.


### Summary

- Your code had proper comments (short, precise, understandable, etc) which was very brilliant for me.
- In all, you did a great job!!!
