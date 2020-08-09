# Mental Math

Just a small hacked together routine, with the aim
of having a small program to practice mental math.

There are routines to do addition, subtraction, multiplication
and division, decimal/hex conversion, binary/decimal conversions,
element/symbol conversions, and 2 powers.

Each routine gives you 100 problems to solve, generated
at random.

You can run these as follows

This gives you a highest value of 30 for the addition problems

```python
>>> import mental_math as mm
>>> mm.do_addition(30)
```

If you want to do them all, in a row, you can run
runall() (which will run if you just run the whole module).

```python
>>> import mental_math as mm
>>> mm.runall()
```

runall will do each of them in a row, and log your results.

Each time you play it, it looks at your logged results.  If you
do any one of the routines within a maximum time and without
error, the next time it will increase the amount.

TODO:

1. Write tests - do this before refactoring
2. Refactor, make it more 'DRY'
