# misc


## collect.py

Remote fetching of data.

Here are instructions that will create a folder in your home directory with the necessary set up
In the terminal sessions
1. Open up a Terminal session (on a Mac, you can find *Terminal* in the Utilities folder of your Applications folder).
1. Type `git clone https://github.com/shaze/misc.git`   This will create a directory called *misc* in your home directory. If you already have a file or folder with that name say `git https://github.com/shaze/misc.git mymisc` and then do the following instructions *mutatis mutandis* using *mymisc" ,
1. Change directory: On my system this would be `cd misc`
1. If you type in `ls` (followed by return) you should several files including *sample.csv* and *collect.py*
1. Run the program. In the example below I am assuming your file is called *sample.csv*. Replace this whatever you have called your data file. Type in the command 
  `python collect.py sample.csv`   followed by return.
1. The program tries to guess the correct ouput type but can't always do that.
1. If the program can't fetch the data : e.g., file no longer available you should get a meaningful error message

