# def the view function
	# check if user is staff. If he's cleard, continue.

	# check the GET method. If GET
		# give context
		# generate template
		# return
	# check the GET method. If POST
		# check the source site through regular expression matching.
			# if youtube is found, source_site is 'youtube'
			# if soundcloud is found, source_site is 'soundcloud'
			# if vimeo is found, source_site is 'soundcloud'
			# if nothing is found
				# add a message instance
				# return redirect to frontpage
		# initiate the form object with POST data
		# if the form is not valid
			# add a message instance
			# return redirect to frontpage
		# if the form is valid
			# continue
		# initiate a new Son
		# populate with manually added title, thumbnail, 
		# populate with automatic source_site, source_id_string

			
