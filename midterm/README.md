# Midterm

To run the code in this assignment, you must install the dependencies listed in [requirements.txt](requirements.txt).
It contains the dependencies for all code files.

## Q1

Code for this question is found in [q1.py](q1.py)

### Part 1

In part 1, I generate processor values for 50 days, 100 per day. I calculate the percentage of viable and EHP processors
according to the percentages given. I then count how many processors per day fit that amount, and plot it. This results
in a plot that is in a straight line. The time it takes to find EHP processors each day is plotted for comparison to
part 2.

### Part 2

In part 2, I generate processor values for 50 days just like in part 1, then I make an assumption that I will find at
most 1 EHP processor per day. I calculated the value the processor needed to have to be considered an EHP processor,
Then, if one was found, it stopped immediately and moved on to the next day. It does this repeatedly until it gets
through all 50 days. The time it takes to find an EHP processor each day is plotted.

## Q2

Code for this question is found in [q2.py](q2.py)

### Part 1

In this part I have 2 nested for loops checking for 24 months for each area. I plot for each area and show them all at
once.

### Part 2

I'll be honest, I'm not quite sure when to move them. The yield in each area is quite erratic. Because of this, I can't
say I'd change them from where they are now. If I'm wrong and it would be better to move them, there's a decent chance
I coded the algorithm in Part 1 wrong. In that case, I would move the teams to different areas when that area appears to
have a more consistent yield, but would be watchful in case the yield begins to drop off.

### Part 3

I implemented code similar to what I used in HW 2. The yield seems to be smoother month-to-month than the original code.
While still somewhat erratic, it doesn't seem to make as large of jumps between months as the algorithm used in Part 1
and 2.

### Part 4

I would open a mine in areas 4 and 5. In my limited testing their yields appeared to fairly consistently be in higher
ranges, as shown on the graph. I wouldn't say they were particularly strong compared to the others, but they seemed
slightly stronger. Their trending direction (up/down) on the graph wasn't very consistent between runs, though.
I made this choice by observing the range of values for each graph in repeated test runs. Area 4 in particular
had a more consistently higher high end of the graph than some others did.

## Q3

Code for this question is found in [q3.py](q3.py)

### Part 1

Similarities in TSLA and AAPL stock include that they both trend upwards, including a sharp rise around the end of 2019.
They also both start at less than 50 back in 2010. There are several differences, however. Tesla stock seems to be far
more volatile in both high/low difference and difference at closing from previous day. For closing prices, Tesla could
fluctuate as much as 40 dollars per day or more between days, where Apple would only fluctuate around a max of 25. For
high/low fluctuation, Tesla could fluctuate as much as around 45 dollars during a day, where Apple would only fluctuate
around up to 17 during a day.

I would note that both have increasingly volatile change in day-to-day difference in closing values as they move forward
in time. This can also be said about the difference in high/low values for each day. I can't say I understand the
different distributions enough to say which one each of these graphs is most like. If I were to hazard a guess with
my limited knowledge of each one that we've used during this class, I'd say the difference in closing values is more
like a beta distribution than any other. It's definitely not uniform, and doesn't seem like a normal distribution.

## Q5

I'll be honest, this course is a bit difficult for me. The hardest thing for me is the mathy stuff. I know that's an
important part of this course especially with the types of algorithms we need to learn about, but math isn't something
that comes easily to me. Most of the details surrounding the math behind the algorithms go right over my
head. I know there are definitely people in the class that understand the math, because I see their engagement in class
when we talk about these algorithms. But I'm also sure there are other students like me who have a hard time with this
stuff. I would love it if the presentation of these subjects could take less mathy people into greater consideration.

I very much appreciate the flexibility you have in this course and that you make yourself accessible to people who have
questions through meeting with you in person and via Discord.

Also, one thing I've been wanting to point out for a while is that while you say your English isn't great when students
are confused about what's being asked for assignments, I'd personally say your English is great. I would never have
guessed that English is your second language, even. I think the issue students have would be solved by greater
elaboration in assignment requirements. The language used in assignments thus far is completely understandable, but at
times there is a lack of detail in what is being asked by particular questions. Greater detail would likely solve the
problem. So don't worry, students are not under the impression that this is an issue because of the quality of your
English. I know you mention this in the midterm question prompt, but I thought I'd offer greater detail than I have
previously when discussing this with you. I also understand this is easier said than done, so do what you will with this
feedback. 
