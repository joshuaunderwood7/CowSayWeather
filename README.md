CowSayWeather
=============

Cowsay Weather
--------------

I got lonely, so I invited my cow friend to talk to me when I log in.

you can too.

+ install `cowsay` and `fortune`
    - On Ubuntu (Debian) run `sudo apt-get install cowsay fortune`
+ put weather.py in your `~/bin/`
+ add the following to your `.bashrc`
    - `python ~/bin/weather.py [STATION CODE] [Your Name]`
    - if you don't put in a name it will default to your system user name. That can be cold and heartless, 
      and some people like it that way.
    - if you don't put in a station code it defaults to Denver.  Welcome to the Mile High City.
+ That's it.


[So to look up your station code for your area](http://w1.weather.gov/xml/current_obs/)
click the link, and enter your state and find the code in the parens by your city.

This comes from weather.gov, so it may not work outside the US.  sorry about that. :\

---
This is licenced GLPv3 or latter.  Check the licence file if you have any questions.
basically, you are free to take this code and modify it to suit your needs. As long 
as all of your changes are also GPLv3`d

