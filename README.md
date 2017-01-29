# BOINC on Heroku

This is a simple app that deploys to a Heroku dyno to work on Universe@Home, supporting free plans. Be aware that this currently contributes to my account.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Click [here](http://boincoku.herokuapp.com/) to see how many instances are currently contributing to Universe@Home through this app. (the dashboard is AKA Boincoku)

You can look at the code for the dashboard [here](https://github.com/CrazyPython/boinc-dashboard-heroku).

## Todo
These things can be improved. I may add them in my spare time, but feel free to send a Pull Request.

 - [x] Make the web dyno also perform computation, redirecting root to the Bonicoku dashboard
 - [ ] Support for alternative accounts (other than mine)
 - [ ] Add support for other projects such as SETI@Home and Asteroids@Home
