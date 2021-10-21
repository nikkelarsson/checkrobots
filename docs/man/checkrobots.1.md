% CHECKROBOTS(1) checkrobots 1.0
% Niklas Larsson
% September 6, 2021

# NAME
checkrobots – Fetch and observe websites' robots.txt files.

# SYNOPSIS
**checkrobots** \[*–q* | *––quiet*\] \[*–s* | *––sort*\] \[*–H* | *––headers*\] \<*website*\> \
**checkrobots** \[*–q* | *––quiet*\] \[*–s* | *––sort*\] \[*–d* | *––disallowed*\] \<*website*\> \
**checkrobots** \[*–q* | *––quiet*\] \[*–s* | *––sort*\] \[*–a* | *––all*\] \<*website*\> \
**checkrobots** \[*–q* | *––quiet*\] \[*–r* | *––raw*\] \<*website*\> \
**checkrobots** \[*–h* | *––help*\] \
**checkrobots** \[*–V* | *––version*\]

# DESCRIPTION
checkrobots is a small and simple utility to observe various websites'
robots.txt files. Thinking about the question "Is web-scraping legal and
ethical?", checkrobots was written for the purpose of exploring this question,
by letting the user / developer to make decisions, whether to perform any sort
of webscraping on a certain site or not.

# OPTIONS
**–q** | **––quiet**
: Print only the endpoints (and headers if -H or --headers is specified).

**–s** | **––sort**
: Alphabetically sort the output (if -H or --headers is specified, headers will
be sorted too).

**–r** | **––raw**
: Print the robots.txt as "as is".

**–H** | **––headers**
: Print the headers in addition to the other data.

**–d** | **––disallowed**
: Print only the fields labeled as "disallowed".

**–a** | **––all**
: Print all the fields, including both "allowed" and "disallowed".

**–h** | **––help**
: Print help-pages.

**–V** | **––version**
: Print **checkrobots** version.
