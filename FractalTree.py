import pygame, math, pygame.gfxdraw

# Some constants
surface_height = 1000
surface_width = 1600
surface_background = (53, 70, 92)
color = (127, 138, 152)
scale_ratio = 0.29
default_theta = .30 # 60 degree rotations in radians
default_recursion_depth = 15

# Draws the fractal tree. order = drawings left, depth = drawings completed
def draw_tree( order, theta, size, position, orientation, depth = 0 ) :
	# Scale the size of the branch
	branch_size = size * scale_ratio

	# Rotate the branch
	dx = branch_size * math.cos( orientation )
	dy = branch_size * math.sin( orientation )

	# Calculate drawing coordinates
	(x, y) = position
	end_position = (x + dx, y + dy)

	# Draw the branch
	pygame.draw.line(drawing_surface, color, position, end_position)

	# If we haven't reached the bottom yet...
	if order > 0 :
		# Recursively draw two new sub trees
		next_size = size * (1 - scale_ratio)
		draw_tree( order - 1, theta, next_size, end_position, orientation - theta, depth + 1 )
		draw_tree( order - 1, theta, next_size, end_position, orientation + theta, depth + 1 )


# Draw the fractal and wait for user input to quit
def run( ) :
	drawing_surface.fill( surface_background )
	draw_tree( default_recursion_depth, default_theta, surface_height * 0.9, (surface_width // 2, surface_height - 50), -math.pi / 2 )

	pygame.display.flip( )

	while True :
		# Grab user input to quit
		ev = pygame.event.poll( )
		if ev.type == pygame.QUIT :
			break

# Create the drawing surface
drawing_surface = pygame.display.set_mode( (surface_width, surface_height) )

# PyGame Life Cycle
pygame.init( )
run( )
pygame.quit( )
