# Mini HW 7 Report

by Mason Francis

## Implementation Process

My implementation process was pretty simple. I based my code off the repo given, and made the following changes:

- Used `stable-retro` instead of `gym-retro` because of out-of-date software
- Used `gymnasium` instead of `gym` because of out-of-date software
- Used `torch` 2.2 because I wanted to use CUDA, but I think the original `torch` version specified should do fine
- Got rid of areas where the `seed` parameter is used. Current versions of the packages don’t use it

Steps to run are included inside my README.md file. I had to make the changes above to make the code run under modern versions of Python (3.10) and with some modern packages. The code has to be run under specific environment conditions or else it won’t work. The starter code trained using PPO, so I was able to switch that out for A2C without too much effort.

## Instructions To Run Code

To get training to run:

- set up venv with python 3.10. I used Ubuntu 22.04. Don't use conda, I ran into some driver issues while trying to use it.
- run `pip install "stable-baselines3[extra]"`
- run `pip install -r requirements.txt`
- run `pip install torch==2.2.1` (I only did this because I wanted to use CUDA, and this the `torch` version that matched with my CUDA version)
- obtain compatible game rom (I got mine [here](https://archive.org/details/No-Intro-Collection_2016-01-03_Fixed) and specifically downloaded the NES ones)
- import roms by running `python3 -m retro.import [path to folder with zips of roms]`
- run `python3 TrainPPO.py` or `python3 TrainA2C.py` depending on which one you want

I chose 452000 timesteps because that's what my PPO got to before I got tired of waiting for it because I had other homework to do.

## Algorithm Comparisons

I was not able to get Run.py to work, so I couldn't really compare the outcomes of the algorithms. I did, however notice that A2C trained decently faster than PPO, taking probably 2/3 the time to train. 

Since I'm not able to compare outcomes, I did some reading [here](https://www.linkedin.com/advice/3/how-do-you-handle-exploration-exploitation-trade-off)
about the differences between A2C and PPO. 

A2C tends to be simpler, but it requires more data. PPO is more efficient, yet more complex than A2C. I would say that my understanding of how A2C works is more clear than for PPO, particularly because PPO is more complex. 


## Challenges Faced

I faced a few challenges with the starter code, primarily it’s age. Although it’s not that old, some of the packages have had breaking changes since it was written. Luckily, most affected packages have had replacements written for them, so I was able to use those. These packages were:

- gym-retro -> stable-retro
- gym -> gymnasium
- stable-baselines3 -> newer version compatible with gymnasium

I also was unable to get [Run.py](Run.py) to work, so unfortunately I was not able to view the outcomes of the training. 

## Key Takeaways

I had a few different key takeaways from this assignment. I learned that different types of training take different amounts of time.
I learned that A2C involve different levels of complexity. I also learned firsthand why GPUs are so useful for this type of work. 
As soon as I installed the CUDA toolkit and drivers for use with PyTorch, the speed of training increased dramatically. 
In speaking with my other classmates, this type of performance improvement was experienced by them as well. 
