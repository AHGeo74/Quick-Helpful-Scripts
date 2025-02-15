# Quick-Helpful-Scripts
These are small tools that I made for very specific problems that I have encountered in my lab work. For each script, a description will be added to the README that say what the program is, what problem prompted it's creation and how it works.

**ASCII Code 39 Barcode Translator**

**_Problem:_** We had some barcodes on sample vials that were read just fine by a certain barcode scanner, but then that scanner was lost and other scanners only output a ridiculously long string of numbers that didn't seem to match any of the barcodes in the accompanying spreadsheet.  After some reasearch into how barcodes work in the first place, I found the ASCII 39 barcodes and noticed that in the scanner outputs, there was a zero at every third position, starting with the first (0th) position.  I then translated one by hand and it matched one of the barcodes in the spreadsheet, so I wrote this bit of code to allow me to paste numbers into the program for quick translations.

**_Use:_** This program is used for translating barcodes that have been translated into it's raw ASCII Code 39 format with segments of three integers (0xx).  It can only translate numbers 0-9.  All you need to do is run the program on a computer with Python installed and paste your strings of numbers into it and it will output the translated barcode.

**_Further Improvements (if revisited):_** Some possible modifications to make include a full ASCII Code 39 translation table, a CSV reading option, and a 2-sequence or 3-sequence selection.
