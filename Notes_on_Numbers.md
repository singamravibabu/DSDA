# WORKING WITH NUMBERS
- Floating-point nubmers have limit significant digits.
- Floating-point number is an approximate vaue that can yeild unexpected results known as floating-point errors.

### math module
- Students should explore this module

- The math module function
    pow()
    sqrt()
    ceil()
    floor()
    pi (constant)

## Formatting numbers
- The `format()` method of string is used to format a single value or a series of values by converting them to strings.

### The format() method
Syntax:
```
"...{:format_specification}...".format(data_item, ...)
```

#### The syntax for the format_specification
[field_width][comma][.decimal_places][type_code]

- command type codes
    - d (integer)
    - f (float)
    - s (string)
    - % (percentage)
    - e (exponential)

< is for left-alignment
> is for right-alignment
^ is for center-alignment


## The locale module
## The currency() function


## WORKING WITH DECIMAL NUMBERS
- Use the `decimal` module to create decimal numbers that are exact when and don't yield unexpected results.
- We use `Decimal` class from `decimal` module to create decimal numbers, and also we import rounding constants that we need from the decimal module.
- To create a Decimal object that a stores a decimal number, pass a string for the decimal nubmer to the constructor ('Decimal(string)') of the Decimal class.
- Its legal to code expressions mixing Decimal with int values. However, its illegal to code expressions that mix Decimal objects with float values.

