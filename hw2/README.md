# CS 5060 - HW 2

## Requirements

This code requires `numpy`, `scipy`, and `matplotlib` to run. You may also need to install Tkinter to make 
sure that you can see the graphs. 

## Running the code

1. Make sure your dependencies are installed. You can install them using this command:

```bash
pip install -r requirements.txt
```

2. If you're using Tkinter to display the graphs, feel free to leave line `11` as is. Otherwise, comment it out.

3. Run the main file:

```bash
python3 main.py
```

The program will first show graphs for Part 1, then for Part 2, then for Part 2 Thompson starting at 3000.

## Responses to assignnment questions

### Part 1

- It appears to me that the smaller the epsilon value, the more quickly it converges. So the optimal value out the ones provided is 0.01. But it appears that even smaller values might converge even faster. 
- The Thompson sampling method seems to converge more slowly than the epsilon greedy method, but it was more reliable and consistent than my epsilon greedy graphs.  

**Note:** For some reason, I could not figure out why the epsilon greedy graphs don't converge to around 2, and they are different every time I run them. Each of them do converge individually to their own values, just not to 2.

### Part 2

- The same could be said as in part 1 for smaller epsilon values being quicker to converge here. 
- The Thompson sampling doesn't seem to do as well as the epsilon greedy approach here. In my graphs Thompson doesn't appear to converge, at least not at the number of steps we are using. Also, the drift and change in probability didn't seem to have much of an effect on how quickly the epsilon greedy algorithm converged. 
- If I restart Thompson at 3000, it seems to converge more quickly than with starting at 0.
