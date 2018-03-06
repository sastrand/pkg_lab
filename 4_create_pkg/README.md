## 4: Create package and import *

Importing evey name from a package is a bad idea almost all the time, but it's useful to know how it works
and how to limit its power in your own package.

So, in this exercise, add an `__init__.py` file to the `driving_pkg` directory with the `__all__` special variable set so that every name in the `driving_pkg` namespace will be imported except those in the module `bad_module`.

### Expected output

```
10 km = 16.09344 mi.
100 miles in 100 minutes averages 60.0 mph.
258 miles on 12 gal of gas is 21.5 mpg.
```
