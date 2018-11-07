# add an __init__.py file to driving_pkg 
# and import statment(s) using the `import *` 
# syntax that will allow the following code will run

from driving_pkg.canada import *
from driving_pkg.drt import *
from driving_pkg.mpg import *

if __name__ == "__main__":
    strs = {
        "km_to_m": "10 km = {} mi.",
        "mph": "100 miles in 100 minutes averages {} mph.",
        "mpg": "258 miles on 12 gal of gas is {} mpg.",
    }
    print(strs["km_to_m"].format(km_to_m(10)))
    print(strs["mph"].format(speedometer(7000, 7100, 100)))
    print(strs["mpg"].format(mpg(10000, 10258, 12)))
