Jan from optil.io informed us that their system sometimes gets stuck when a submission is killed due to reaching the time limit.

If you get an "internal error", it might be related.
He is looking into each Internal Error separately.
For now he suggested to assume that if you got IE_b, 
then it is most likely TLE. 
 
As for "testing" without actually adding 
new results - optil changes the submission status after 
the compilation, and when the compilation is successful,
the test runs on all instances are added to the job queue.
Even though a submission got compiled and the status was changed to "Testing",
it is often the case that the tests are only queued up, but not actually running yet.
Optil will probably add a separate status "Compilation OK, queued for tests" to indicate this situation,
and use "Testing" when the test on the first instance actually starts.
 
Optil is actively working to resolve these inconveniences.
