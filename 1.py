# I am running a catering company and need to know how many eggs I have once
# the delivery order comes in. I've written a program to calculate how many eggs I
# have, given that there are 8 eggs in a box.

egg_boxes = 4
eggs_per_box = 8  # Removed the quotation marks
total_eggs = egg_boxes * eggs_per_box
message = 'I have {} eggs'.format(total_eggs)
print(message)