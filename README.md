PIseries
========
> A fast converging PI series.
This paper describes one of many possible ways to calculate the value of $\pi$ with a geometrical series. This method will be particulary useful to calculate the value of $\pi$ with iterative approach taking terms as per the required precision.

# Setup
First clone this repository
```
    cd /path/to/clone
    git clone git@github.com/TheDeltaFinders/PISeries.git

```
Then copy the directory   `DFormat` in your tex path. On GNU/Linux
```
    cp -R ./DFormat ~/texmf/tex/latex
```
Do the same for `jpconf` if you dont have.

# Execute
```
    xelatex ./PISeries.tex
````
It spits out the paper `PISeries.pdf`.
Enjoy :)
