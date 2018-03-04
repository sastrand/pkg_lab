from driving_pkg import canada, drt, mpg

if __name__ == "__main__":
	strs = {
	    "km_to_m":"10 km = {} mi.",
	    "mph": "100 miles in 100 minutes averages {} mph.",
	    "mpg": "258 miles on 12 gal of gas is {} mpg.",
	}
	print(strs["km_to_m"].format(canada.km_to_m(10)))
	print(strs["mph"].format(drt.speedometer(7000, 7100, 100)))
	print(strs["mpg"].format(mpg.mpg(10000, 10258, 12)))
