#PopRank


## Concurrency and Parallelism

Python has many options for creating parallel threads for the functions of our simulation.

Similarly, we could run the functions concurrent with some python libraries.

However, the best option for simulation purposes is stepping through fake units of time and running the functions sequentially. This allows us to be independent of time in our simulation and run fair tests, by allowing us to test multiple algorithms "simultaneously".

## Helpful stuff

exec(open("./main.py").read(), globals()) runs main.py in python interpreter

# Todo

## Goal Algorithm Comparison

To see if we have the best algorithm for sorting this type of data, we need some kind of metric to determine how well each alogirthm sorts data. 
We may need to compare raw data, find trends, and use graphing tools to highlight the differences between the sorting algorithms.
However, the goal at its most basic is just to identify differences between the algorithms.

Below is a list of hypothetical methods we can establish a difference between two algorithms.


## Helpful Info

For the examples below I will be comparing AverageSort and PopRank, but we could compare the effectiveness of other algorithms.
I am just using them to demonstrate the type of difference we need to indentify.

Note that when I say the intrinsic value, I mean the intrinsic value of a post and when I saw determined value, I mean the value calculated by our algorithm.

For instance intrinsic value may be .76857875.

But if 8 people vote on it with 7 upvotes and one downvote. The determined intrinsic value by the AverageSort algorithm will be  (upvotes-downvotes)/TotalVotes=(+7-1)/8= .75

As a Handy Refernce:

x = The Post

y = Intrinsic Value

We needs some function f(x) so that we end up with y.

f(x) could be AvgSort(x) or maybe PopRank(x)

## Time Independent

### Simple Difference 

We measure the difference between the intrinsic value and the determined intrinsic value of each algorithm.

For each post, we find the absolute difference between the determined intrinsic value and the actual intrinsic value.
We then sum this difference to find the total difference

We compare this sum of differences for each algoirthm.
The higher the difference the worse the algorithm is for this type of metric.

metric = sum(abs(f(x)-y))

### Residual Sum of Squares - Literally a Statistics term

This one is very similar to simple difference except after finding the difference, we square it before adding it.

metric = sum( (f(x)-y)^2 )

### Residual Sum of Squares of the best posts

I think we should care more about the good posts than the bad.
The other time independent ones care too equally about the posts

So we should only add the sum of squares of those posts that have high intrinsic value.

## Time Dependent


## Algorithm Design

### Figure out what Algorithm is doing

p-hat = Variable, upvotes/votes
z-alpha/2 = Constant, norm dist value, 1.96
n = constant, but depends on users



### Pseudocode of Algorithm



### Implement Algorithm

### Use metric on algorithm




