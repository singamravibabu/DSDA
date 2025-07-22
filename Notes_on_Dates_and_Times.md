# WORKING WIT DATES AND TIMES
> The `datetime` module contains constructors for constructing date and time objects (values).

- From the `datetime` module, we can use the following constructors to create date, time and datetime objects:
    - date(year, month, day)
    - time(hour, minute, second, microsecond)
    - datetime(year, month, day, hour, minute, second, microsecond)
    - timedelta(days, seconds, microseconds)


> Two common methods of the date and datetime classes

1. date.today()
    - Returns a date object for the current date.

2. datetime.now()
    - Returns a datetime object for the current date and time.


> The constructors for creating date, time, and datetime objects

1. date(year, month, day)
    - Returns a date object for the specified date.

2. time([hour][, minute][, second][, microsecond])
    - Returns a time object for the specified time.

3. datetime(year, month, day[, hour][, minute][, second][, microsecond])
    - Returns a datetime object for the specified date and time.


#### Timezone awareness
- Both datetime and time objects can be either aware or naive.
- Aware objects account for time zones and daylight saving time.
- Naive objects don't account for time zones and daylight saving time.
- By default, datetime objects and time objects naive.
- We can make them aware by providing an optional tzinfo argument.
- We can't make date objects aware because they don't store time info.


#### The strptime() method: create datetime objects by parsing strings.
- The p in the strptime() method stands for parse.
- We can use this method to create a datetime object by parsing a string.

```
datetime.strptime(string, format)
```

- Uses the specified format string to convert the datetime string to a datetime object.

- Common format string codes:
    %d  Day of month as a number
    %m  Month as a number
    %Y  Year with century as a decimal number
    %y  Year without century as a decimal number
    %H  Hour (24-hour clock) as a decimal number
    %I  Hour (12-hour clock) as a decimal number
    %M  Minute as a decimal number
    %S  Second as a decimal number
    %p  AM or PM specifier
    %f  Microsecond as a decimal


#### The strftime() method: formatting dates and times

```
datetime.strftime(format_str)
```
- The f in the strftime() method stands for format.
- We can use this method to get a string for the datetime object with the specified format.
- Common format string codes:
    %a  Abbreviated weekday name
    %A  Full weekday name
    %b  Abbreviated month name
    %B  Full month name
    %c  Full date and time
    %d  Day of month as a decimal number
    %H  Hour (24-hour clock) as a decimal number
    %I  Hour (12-hour clock) as a decimal number
    %j  Day of year as a decimal number
    %m  Month as a decimal number
    %M  Minute as a decimal number
    %p  AM or PM specifier
    %S  Second as a decimal number
    %U  Week number of year (Sunday as the first day of the week) as a decimal number
    %w  Weekday as a decimal number
    %W  Week number of year (Monday as the first day of the week) as a decimal number
    %x  Locale's appropriate date and time representation
    %X  Locale's appropriate date representation
    %y  Year without century as a decimal number
    %Y  Year with century as a decimal number
    %z  Time zone name
    %Z  Time zone name
    %%  A literal % character


## WORKING WITH SPANS OF TIME