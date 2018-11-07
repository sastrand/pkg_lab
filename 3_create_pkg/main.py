# add an __init__.py file to driving_pkg and import statements
# to this file so that the following code will run.
# You will need to import each module in driving_pkg separately
# with an alias

# [Add import statement(s) here]

if __name__ == "__main__":
    strs = {
        "km_to_m": "10 km = {} mi.",
        "mph": "100 miles in 100 minutes averages {} mph.",
        "mpg": "258 miles on 12 gal of gas is {} mpg.",
    }
    print(strs["km_to_m"].format(canadian_distances.km_to_m(10)))
    print(strs["mph"].format(distance_rate_time.speedometer(7000, 7100, 100)))
    print(strs["mpg"].format(miles_per_gallon.mpg(10000, 10258, 12)))
