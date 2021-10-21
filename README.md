# About
**checkrobots** is a small and simple utility to observe various websites'
robots.txt files. Thinking about the question "Is webscraping legal and
ethical?", **checkrobots** was written for the purpose of exploring this
question, by letting the user / developer to make decisions, whether to perform
any sort of webscraping on a certain site or not.

# How it works
With **checkrobots**, user can explore the robots.txt's contents, which will
usually display endpoints, from which some might be labeled as "allowed" and some
as "disallowed". Then, with user's own consideration, user can try and do some stuff
with these endpoints, whether the endpoints chosen are labeled as "allowed" or
"disallowed".

# Installation
**checkrobots** can be installed using **make**. If you want to do some exploration
with the sourcecode and change it and test your changes easily without having to
**make install** after each change, you can install the **editable** version of **checkrobots**.
Otherwise, you can install the **regular** version. To start off, go to the root of the
project and run either of the following.

To install the **regular** version, run:
``` bash
make install
```

To install the **editable** version, run:
``` bash
make install-editable
```

To uninstall:
``` bash
make uninstall
```
