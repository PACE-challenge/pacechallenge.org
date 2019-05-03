Jan from optil informed us that,
 sometimes their system gets stuck after 
killing the submission due to time limit.

If you get an internal error it might be related.
He is look into each Internal Error separately.
For now he suggested to assume that if you got IE_b, 
then it is most likely TLE. 
 
As for "testing" without actually adding 
new results - optil changes submission status after 
compiling, and then, when compilation is successful 
they add to queue runs on all instances. It can often
 happen, that even though submission got compiled and 
changed to Testing..., there are still other submissions
 before it. They will probably add intermiediate status
 "Compilation OK, queued for tests", and set Testing 
when the test on first instance actually starts.
 
They are work on it, after solving the issue with 
docker containers.
