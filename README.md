# misc


## collect.py

Remote fetching of data.

Create a suitable folder/directory in your home directory. In the rest of this explanation, I am assuming you are on a Apple and do this on your desktop, and that the directory is called  *remotedata* (hint: don't put blanks into the file name).

In the same directory create a file that has two columns, separated by a tab. The first column is a code that you want to use to name the fetched files (don't put blanks into the code) and  the second column is the URL you want to fetch.

Open up a terminal (from Applications, in the Utilities directory you will find the Terminal Application).

In the terminal sessions
1. Change directory: On my system this would be `cd /Users/scott/Desktop/remotedata`
1. Check that you are in the right place: `pwd` This should echo back what you gave the `cd` command above
1. Run the program. In the example below I am assuming your file is called *sample.csv*. Replace this whatever you have called your data file. Type in the command 
  `python collect.py sample.csv`   followed by return.
1. The program tries to guess the correct ouput type but can't always do that.
1. If the program can't fetch the data : e.g., file no longer available you should get a meaningful error message

