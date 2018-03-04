## 4: Create package and import *

Importing evey name from a package is a bad idea almost all the time, but it's useful to know how it works
to manage other people's code where it may be used and for the occation when a fast, easy bulk import of a
namespace is all you need (like when working in the interpreter's interactive mode).

So, in this part, add an `__init__.py` file to the `driving_pkg` directory with the `__all__` special variable set
that will allow you to import every name in the `driving_pkg` namespace, as has been done in the `main.py` code.

### Expected output

```
10 km = 16.09344 mi.
100 miles in 100 minutes averages 60.0 mph.
258 miles on 12 gal of gas is 21.5 mpg.
```
