#PopRank


## Concurrency and Parallelism

Because we are running many different functions simultaneously, we should find a way to separate concerns as we go through the simulation. At first, I figured we could run the functions in parallel, one on each thread. Then I considered running them at the same time using some concurrent python functions. Both of these would rely on time to determine when to do a specific function. However, that would mean that we would be dependent on time for oru simulations. Instead I propose we have a counter that fakes time for us and we run the functions sequentially as the timer ticks forward. We wouldn't be able to run the simulation against real time, but we wouldn't have to worry about time and be able to take snapshots of our data.



