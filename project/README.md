# you nieed title here

## Issues

Gregor:

* does not leverage cloudmesh you make your life to complex without it
  dockerfile is questionable as mount or git clone not used (either one,
  but the way you do the copy is not appropriate, as you can not easily
  develop in your container and you make life to comples

* docker mongo db container has security flaw as it does not set up
  admin user, look at cloudmesh cmsd developed by TA. As he may not
  have completed this this may be a reason for you to justify an
  incomplete. E.g. his task was to deliver this some month back. I am
  not sure if its usable at thsi time. he claims it is. Last friday it
  was unclear. Get appointment with Ta to make sure this runs on your 
  computer.

* dnspython is somehow internally used by something, but is not
  automatically installed for some reason. this is used for the mongodb
  uri. This has to be further invertigated, as we shoudl not have to
  explicitly include this in the requiremnts. I may be wrng on thsi
  (Gregor)