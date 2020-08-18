# aops_bkup

This coding is to make a local backup of following mathematics competition problems and solutions provided on AOPS website, in case they do not provide contents in the future, and also for convenience to practice the problems on local.

* AMC 8
* AMC 10
* AMC 12
* AIME
* USAJMO
* USAMO

Step 1:
Run python aops_crawl.py

Step 2:
Do a text replace in files - VS Code can at most replace 10000 occurrences of a string among files, so this step has to run for a bunch of times.

```
src="https://latex.artofproblemsolving.com
```

Replaced by:

```
src="https://latex.artofproblemsolving.com
```

Step 3:
TODO: Remove redundant styles and Google Analytics scripts.
