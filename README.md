# Mental Math

Just a small hacked together routine, with the aim
of having a small program to practice mental math.

There are routines to do addition, subtraction, mulitplication
and division.  For each of these routines you give the highest value
that you want to have in your calculations, and it gives
you 100 problems in a row to solve.

These routines are called do_addition(), do_subtraction(),
do_multiplication() and do_division().

You can run these as follows

>>> import mental_math as mm
>>> mm.do_addition(30)

If you want to do them all, in a row, you can run
runall() (which will run if you just run the whole module).

>>> import mental_math as mm
>>> mm.runall()

runall will do each of them in a row, and log your results.

Each time you play it, it looks at your logged results.  If you
do any one of the routines within a maximum time and without
error, the next time it will increase the amount.
