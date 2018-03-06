## Part 0: Import a module that's not in a package

By default, any module in the same directory as the function named `__main__` 
can be imported directly without being part of a package.

In this section, add an import statement to the `main.py` file
to import the `hello()` and `bye()` functions in `salutations.py`.

Note that there are many ways to import the contents of a module,
but only one will allow `hello()` and `bye()` to be called with
the syntax used in `main.py`.

Find a way to import `salutations.py` that allows this syntax to work.

### Expected output

Something like:

```
Please enter your name.
Bax
hello, Bax.
and
goodbye, Bax.
```
