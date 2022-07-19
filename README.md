# stfc-code-jam
Challenges and starter code for STFC's monthly code jam

## 2022 schedule

We will meet on the fourth Monday of the month from 12:00-13:00, with exceptions for non-STFC events like Hash Code. For now we'll meet both on-site at RAL and online via Zoom for each session.

This year we'll be working through some past Google Kick Start and Code Jam challenges. Note that on the challenge pages, the "Analysis" tab contains solutions for the problem - so don't look at that tab unless you want spoilers! Selected problems are subject to change as we figure out the right difficulty level for the group.

Test data for each problem is included in the relevant dated folder. The test data is provided by Google.

* Feb 24 (evening): [Google Hash Code](https://codingcompetitions.withgoogle.com/hashcode/round/00000000008caae7)
* Mar 28: [Google Kick Start 2020: Plates](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d40bb)
* Apr 25: [Google Kick Start 2020: Robot Path Decoding](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d83dc#problem) (Note for starter code author: parsing the rover program is the challenge, please don't expand brackets etc. within the rover program)
* May 23: [Google Kick Start 2020: Wandering Robot](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d8565#problem)
* Jun 27: [Google Kick Start 2020: Workout](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3f5b)
* Jul 25: [Google Kick Start 2020: Beauty of tree](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff08/0000000000386edd)
* Aug 22: [Google Code Jam 2020: ESAb ATAd](https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209a9e) (Note: This is an [interactive problem](https://codingcompetitions.withgoogle.com/codejam/faq#interactive-problems) which requires more complex starter code)
* Sep 26: [Google Kick Start 2020: Bus Routes](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d83bf)
* Oct 24: [Google Kick Start 2020: Alien Piano](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff08/0000000000387174)
* Nov 28: [Google Kick Start 2020: Candies](https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff43/0000000000337b4d)
* Dec (daily): [Advent of Code](https://adventofcode.com)


## Contributing

### I have a challenge suggestion

Create an issue on this repository or post in the #ideas channel on the STFC code jam Slack. Include a link to the challenge you want to suggest.

Good challenges for the monthly code jam have as many of these qualities as possible:
* easy to understand
* achievable within one hour by a pair working together
* can be approached or solved in multiple ways
* don't require complex maths or other niche background knowledge

### I want to write some starter code

Using starter code saves everyone from spending valuable time individually writing the same input/output functions during the code jam. Anyone can write starter code and submit it as a PR to this repository. Please name the script file `starter` and place it in the folder for that date, e.g. `2022-04-25/starter.py` (create the folder if you need to). You can also post the code on Slack if you aren't comfortable using GitHub.

Starter code should take the input for a challenge and read it into a useful data structure. If the challenge requires output to be in a specific format, the starter code should also provide a function for this. You, as the author of the starter code, can decide what data structures make the most sense for the challenge and your functions.

If the starter code is long or complex, please include comments or type hints to make clear how the code should be used.

The preferred language is Python, as most attendees are familiar with this. Python starter code should be compatible with version 3.7+. You can use the [generic_starter.py](generic_starter.py) file as a template.


