# Mini HW 7

To get this to work:

- set up venv with python 3.10, I used Ubuntu 22.04. Don't use conda.
- run `pip install "stable-baselines3[extra]"`
- run `pip install -r requirements.txt`
- run `pip install torch==2.2.1` (I only did this because I wanted to use CUDA, and this the `torch` version that matched with my CUDA version)
- obtain compatible game rom
- import roms by running `python3 -m retro.import [path to zip of rom]`
- run `python3 Train.py`
