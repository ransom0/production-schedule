def production():
	a_bph_avg = 217.8719
	z_bph_avg = 178.494
	a_pallets = float(input("How many pallets of Calibrin A do you need to do?"))
	z_pallets = float(input("How many pallets of Calibrin Z do you need to do?"))
	pallet_size = float(input("How many bags per pallet?"))
	a_total_bags = 0.0
	z_total_bags = 0.0
	if pallet_size == 40.0:
		a_total_bags = a_pallets * 40.0
		z_total_bags = z_pallets * 40.0
	elif pallet_size == 48.0:
		a_total_bags = a_pallets * 48.0
		z_total_bags = z_pallets * 48.0
	else:
		a_total_bags = a_pallets * 50.0
		z_total_bags = z_pallets * 50.0
	days = float(input("How many days do you have to do this?"))
	shift = float(input("How many hours will the shifts be?"))*60
	breaks = float(input("How many minutes will be spent the 15 minute and lunch breaks going to be (in minutes)?"))
	workhours = ((days*shift)-(days*breaks))/60
	time_needed = 0.0
	time_needed = (a_total_bags / a_bph_avg) + (z_total_bags / z_bph_avg)
	if time_needed <= workhours:
		print("This can be done this with {0} hours to spare.".format(workhours-time_needed))
	else:
		print("This can't be done. You need {0} more hours.".format(time_needed-workhours))		





