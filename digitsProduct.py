def digitsProduct(product):
	"""Returns smallest self-digit-multiplied number to return the product."""

	# base conditions.
	if product == 0:
		return 10
	if product == 1:
		return 1

	# Smallest number self-digit-multiplied returns product.
	result = []

	# product equals 1 means all highest factors are done.
	while (product != 1):

		for i in range(9,1,-1):
			print(f"Iteration: {i}")                                # Debugging.

			if (product%i) == 0:
				print(f"product: {product} is divisible by: {i}")	# Debugging.

				# Append to the left of the list.
				result.insert(0,str(i))
				print(f"The result now is: {result}")				# Debugging.

				# Put the next highest factor of product
				product = product//i
				print(f"The product now is: {product}")				# Debugging.

				# Start from the top.
				break

			# Product is a prime number.
			if i == 2 and product != 1:
				print(f"Reached the end of the for loop and nothing is divisible by {product}")	# Debugging.
				return -1

	
	return int("".join(result))

