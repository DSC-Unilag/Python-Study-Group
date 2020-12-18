[Project3](https://repl.it/@Zaayzay/Project3)

4834

### Feedback 
Holla. Nice, I like the way you thought about the problem. That said your solution does not work for every case for instance the first example in your script. 8 should have been a part of the consecutives. On inspecting your solution, I noticed that your program ignores the largest number in the array because of the following lines:
```
if num == array[-1]:
  break
```
I understand why you included as ```j+1``` will cause an error at that point but you need to find a way around that issue.

Check out a [solution](https://repl.it/@FortuneAdekogbe/DecemberChallenge3) to the problem. There, focus was placed on the numbers themselves and not the indexes. I think you will find it interesting. If there is any problem with understanding it, let me know.
