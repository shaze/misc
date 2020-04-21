# misc


## figsplit.py

This script is used to render PDF from xfig that is suitable for LaTeX Beamer presentations, where the xfig has multiple depths or layers. I used to generate multimetapost files and then use mpost to generate multiple PDF. However, recent versions of xfig seem to have dropped this.

In the simplest form run

```
figsplit.py picture.fig
```

This produces picture-0.pdf picture-1.pdf picture-2.pdf.... Then, use the xmpmulti package in LaTeX  and use the multiinclude function (perhaps don't use the <+>)

```
  \multiinclude[<+>][format=pdf,graphics={width=9cm}]{picture}
```  

Notice that items with lower depth are above items with higher depth. The default behaviour is that everything that at depth n also occurs in the PDFs for depth below n. So if depth 40 correponds to picture-4.pdf then all items at depth 40 will also occur in picture-5.pdf, picture-6... Usually this is what we want, but sometimes in a dynamic picture you will want avoid this


```
figsplit.py --occlude 30-40:40.41,20-25:28 picture.fig
```

This says -- in the PDFs produced in layers 30-40, don't include items at depth 40 or 41, and in layers 20-25 don't include items at depth 28



## parallel.nf


Run like this

```
nextflow run parallel.nf --script scriptfile 
```

_scriptfile_ should be a bash file with a separate command on each line -- the commands should be run in  the foreground not the backgroud. There are two examples given `sleep.cmd` and `plink.cmd`


Each command will be run in parallel on the system, subject to the maximum capacity of your system. The following options are permitted



* `-profile slurm`  submit each job separately to the head node of the cluster running slurm. NB. This parameter takes a single "-" Note that you need to have the `nextflow.config` file in your directory when you run it. You may need to change the queue name to which your jobs should be submitted
* `-profile pbs` ditto for  a cluster running PBS
* `--cpus` show many CPUs does each job need. The default value is 1. 
* `--mem` how much memory is required. Default is "1GB". The unit should be specified
* `--max_fork` how many jobs should Nextflow allow to be active at a time (default is 30, probably 60-100 would be fine but that would depend on the size of your cluster, how busy it is, and any per-user limits on your job. You  should generally rely on the scheduler to do its job but be aware of others needs -- definitely if you have a thousands of jobs or if each job is very long running, pick a reaonable number not to antagonise your colleagues.)
* `--out_dir` the name of the directory where you want the result to go

For example

```

nextflow run parallel.nf --script plink.cmd -profile slurm --mem 6GB  --cpus 2 --max_fork 20 --out_dir /tmp/result

```

Note that if the number of jobs is much larger than `max_forks` or if the jobs are very long running, you should run a `screen` session for the nextflow run.



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



