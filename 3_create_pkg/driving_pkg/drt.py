def speedometer(start, end, minutes):
	"""This function takes a starting odometer reading,
	an ending odometer reading, and a time traveled in
	minutes and returns the average mph over that time."""
	return (end - start)/(minutes/60)
	