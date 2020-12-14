##week4 assessment1

[my submission](https://repl.it/@iOghenetega/LustrousUnselfishDonateware)

5115

### Lo Shu Magic Square

- Firstly, your code was unexpectedly verbose and I was at first afraid of running it. There were a lot of **repetitions, redundancies, unused variables** in your code (redundancy intended).
- Secondly, the way your code was written it could easily break. Infact, I changed the input to your function to a wrong value and it raised an error (`UnboundLocalError: local variable 'flag_a' referenced before assignment`) instead of printing that it was not a magic square.
- There are positives about your code though. Breaking problems the way you did (a function checking each plane, vertical, diagonal, etc) was brilliant and a good way to code, I was mind-blown when I saw it, keep it up.
- Your code works when the input is correct but breaks otherwise.


### Summary

- When you break tasks down the way you did, try to remove repetitions occassionally and wherever you can. For example, a single function `flag_check` can replace the 3 functions `flag_checkh`, `flag_checkv` and `flag_checkd` as they are all doing the same thing.
- Also, hard-coding checks the way you did it would break your code easily. Find a way of using loops effectively instead of hard-coding "all possibilities".
- In all, you did a great and verbose job!!!
