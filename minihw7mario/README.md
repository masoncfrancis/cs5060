# Mini HW 7

To get training to work:

- set up venv with python 3.10. I used Ubuntu 22.04. Don't use conda, I ran into some driver issues while trying to use it. 
- run `pip install "stable-baselines3[extra]"`
- run `pip install -r requirements.txt`
- run `pip install torch==2.2.1` (I only did this because I wanted to use CUDA, and this the `torch` version that matched with my CUDA version)
- obtain compatible game rom (I got mine [here](https://archive.org/details/No-Intro-Collection_2016-01-03_Fixed) and specifically downloaded the NES ones)
- import roms by running `python3 -m retro.import [path to folder with zips of roms]`
- run `python3 Train.py`
