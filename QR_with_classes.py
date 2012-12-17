import Tkinter
from Gui import *
import copy
import QRprepData_ak
import polynomials
import conversions

#qr_bitstring = polynomials.QRbitstring("JESSICA")
#print qr_bitstring[2:]
qr_bitstring = '0010000001011011000010110111100011010001011100101101110001001101010000110100000011101100000100011110110010101000010010000001011001010010110110010011011010011100000000000010111000001111101101000111101000010000'

top_pt_x = -105
top_pt_y = 115
bottom_pt_x = top_pt_x + 10
bottom_pt_y = top_pt_y - 10

class Point(object):
	def __init__(self, x, y, value = None):
		self.x = x
		self.y = y
		self.display_pts = [[top_pt_x+10*x, top_pt_y-10*y], [bottom_pt_x+10*x, bottom_pt_y-10*y]]
		self.value = value
	def set_value(self, new_value):
		self.value = new_value
	def __str__(self):
		return str([self.x, self.y])
	def __cmp__(self, other):
		if (self.x == other.x):
			if (self.y == other.y):
				return 0
		if (self.x > other.x):
			return 1
		if (self.x < other.x):
			return -1
		if (self.y > other.y):
			return 1
		if (self.y < other.y):
			return -1
	def print_displaypts(self):
		print str(self.display_pts)
	def print_vals(self):
		print str([self.x, self.y, self.value])
	def gen_val_list(self):
		return [self.x, self.y, self.value]

class Grid(object):
	def __init__(self, size = 21):
		self.size = size
		self.grid = self.drawAllStaticPatterns()
		emptygrid = []
		for x in range(self.size):
			for y in range(self.size):
				CurrentPt = Point(x,y)
				emptygrid.append(CurrentPt)
				y = y + 1
			x = x + 1
		for i in range(len(self.grid)):
			if (self.grid[i] in emptygrid):
				emptygrid.pop(emptygrid.index(self.grid[i]))
				emptygrid.append(self.grid[i])
			i = i + 1
		self.grid = emptygrid

	
	def __str__(self):
		stringGrid = []
		for i in range(len(self.grid)):
			stringGrid.append(([self.grid[i].x, self.grid[i].y]))
			i = i + 1
		return str(stringGrid)
	
	def print_displaygrid(self):
		stringGrid = []
		for i in range(len(self.grid)):
			stringGrid.append((self.grid[i].display_pts))
			i = i + 1
		print str(stringGrid)
	
	def print_gridvals(self):
		stringGrid = []
		for i in range(len(self.grid)):
			stringGrid.append((self.grid[i].value))
			i = i + 1
		print str(stringGrid)

	def drawPositionRings(self, initial_x, initial_y, length_of_ring, color):
		x = initial_x
		y = initial_y
		pt_array = []
		PointsArray = []

		ct = 0
		for ct in range(length_of_ring):
			pt_array.append([x,y])
			y = y + 1
			ct  = ct + 1
		ct = 0
		y = y - 1
		x = x + 1
		for ct in range(length_of_ring - 1):
			pt_array.append([x,y])
			x = x + 1
			ct = ct + 1
		ct = 0
		x = x - 1
		y = y - 1
		for ct in range(length_of_ring - 1):
			pt_array.append([x,y])
			y = y - 1
			ct = ct + 1
		ct = 0
		x = x - 1
		y = y + 1
		for ct in range(length_of_ring - 2):
			pt_array.append([x,y])
			x = x - 1
			ct = ct + 1
		for i in range(len(pt_array)):
			CurrentPt = Point(pt_array[i][0], pt_array[i][1], color)
			PointsArray.append(CurrentPt)
		return PointsArray

	def drawPositionSquares(self):
		# top left
		MyPoints = []
		posx = 0
		posy = 0
		size = 7
		currcolor = 1
		ct = 0
		for ct in range(4):
			MyPoints.extend(self.drawPositionRings(posx,posy, size, currcolor))
			if (ct != 2):
				if (currcolor == 0):
					currcolor = 1
				else: currcolor = 0
			posx = posx+1
			posy = posy+1
			size = size-2
			ct = ct + 1
		
		# bottom left
		posx = 0
		posy = 14
		size = 7
		currcolor = 1
		ct = 0
		for ct in range(4):
			MyPoints.extend(self.drawPositionRings(posx,posy, size, currcolor))
			if (ct != 2):
				if (currcolor == 0):
					currcolor = 1
				else: currcolor = 0
			posx = posx+1
			posy = posy+1
			size = size-2
			ct = ct + 1
		
		# top right
		posx = 14
		posy = 0
		size = 7
		currcolor = 1
		ct = 0
		for ct in range(4):
			MyPoints.extend(self.drawPositionRings(posx,posy, size, currcolor))
			if (ct != 2):
				if (currcolor == 0):
					currcolor = 1
				else: currcolor = 0
			posx = posx+1
			posy = posy+1
			size = size-2
			ct = ct + 1
			
		return MyPoints

	def drawPositionRims(self):
		MyPoints = []

		# draw top left white rim
		x = 0
		y = 7
		while (x <= 7):
			CurrentPt = Point(x,y,0)
			MyPoints.append(CurrentPt)
			x = x + 1
		x = 7
		y = 6
		while (y >= 0):
			CurrentPt = Point(x,y,0)
			MyPoints.append(CurrentPt)
			y = y - 1

		# draw bottom left white rim
		x = 0
		y = 13
		while (x <=7):
			CurrentPt = Point(x,y,0)
			MyPoints.append(CurrentPt)
			x = x + 1
		x = x - 1
		while (y <= 20):
			CurrentPt = Point(x,y,0)
			MyPoints.append(CurrentPt)
			y = y + 1

		# draw top right white rim
		x = 13
		y = 0
		while (y <= 7):
			CurrentPt = Point(x,y,0)
			MyPoints.append(CurrentPt)
			y = y + 1
		#x = x - 1
		y = y - 1
		while (x <= 20):
			CurrentPt = Point(x,y,0)
			MyPoints.append(CurrentPt)
			x = x + 1
		return MyPoints

	def drawTimingPatterns(self):
		MyPoints = []
		# draw vertical timing pattern
		x = 6
		y = 8
		ct = 5
		color = 1
		while (ct > 0):
			CurrentPt = Point(x,y,color)
			MyPoints.append(CurrentPt)
			y = y + 1
			if (color == 0):
				color = 1
			else: color = 0
			ct = ct - 1

		# draw horizontal timing pattern
		x = 8
		y = 6
		ct = 5
		while (ct > 0):
			CurrentPt = Point(x,y,color)
			MyPoints.append(CurrentPt)
			x = x + 1
			if (color == 0):
				color = 1
			else: color = 0
			ct = ct - 1
		return MyPoints

	def drawBlackDotStabilizer(self):
		BlackDot = Point(8,13,1)
		return BlackDot

	def drawAllStaticPatterns(self):
		AllStaticPts = []
		CurrentPts = self.drawBlackDotStabilizer()
		AllStaticPts.append(CurrentPts)
		CurrentPts = self.drawTimingPatterns()
		AllStaticPts.extend(CurrentPts)
		CurrentPts = self.drawPositionRims()
		AllStaticPts.extend(CurrentPts)
		CurrentPts = self.drawPositionSquares()
		AllStaticPts.extend(CurrentPts)
		return AllStaticPts

	def drawSquares(self, canvas):
		for i in range(len(self.grid)):
			if (self.grid[i].value == 1):
				canvas.rectangle(self.grid[i].display_pts, fill='black')
			if (self.grid[i].value == 0):
				#canvas.rectangle(self.grid[i].display_pts, fill='white')
				i = i + 1

class Mask(Grid):
	def __init__(self, mask, bitstring, size = 21, pen= 0):
		self.size = size
		self.grid = self.drawAllStaticPatterns()
		self.grid.extend(self.draw_type_bits(mask))
		self.mask = mask
		self.bitstring = bitstring
		self.grid.extend(self.fill_empty_points(mask))
		self.pen = pen

	def set_grid(self, new_value):
		self.grid = new_value

	def fill_empty_points(self, mask):
		OrderedPoints = self.order_empty_points()
		for i in range(len(self.bitstring)):
			currentbit = int(self.bitstring[i])
			updatedbit = self.design_mask(OrderedPoints[i], currentbit, mask)
			OrderedPoints[i].set_value(updatedbit)
			i = i + 1
		return OrderedPoints


	def order_empty_points(self):
		PathPoints = self.create_data_coord()
		OrderedPoints = []
		for i in range(len(PathPoints)):
			CurrentPt = Point(PathPoints[i][0], PathPoints[i][1])
			OrderedPoints.append(CurrentPt)
			i = i + 1
		return OrderedPoints


	def move_up_med(self, start):
		x = start[0]
		y = start[1]
		current_rows = []
		while (y >= 9):
			current_rows.append([x,y])
			x = x - 1
			current_rows.append([x,y])
			x = x + 1
			y = y - 1
		return current_rows


	def move_down_med(self, start):
		x = start[0]
		y = start[1]
		current_rows = []
		while (y <= 20):
			current_rows.append([x,y])
			x = x - 1
			current_rows.append([x,y])
			x = x + 1
			y = y + 1
		return current_rows

	def move_up_avoid_timing(self, start):
		x = start[0]
		y = start[1]
		current_rows = []
		while (y >= 0):
			if (y != 6):
				current_rows.append([x,y])
				x = x - 1
				current_rows.append([x,y])
				x = x + 1
			y = y - 1
		return current_rows

	def move_down_avoid_timing(self, start):
		x = start[0]
		y = start[1]
		current_rows = []
		while (y <= 20):
			if (y != 6):
				current_rows.append([x,y])
				x = x - 1
				current_rows.append([x,y])
				x = x + 1
			y = y + 1
		return current_rows


	def move_up_small(self, start):
		x = start[0]
		y = start[1]
		current_rows = []
		while (y >= 9):
			current_rows.append([x,y])
			x = x - 1
			current_rows.append([x,y])
			x = x + 1
			y = y - 1
		return current_rows

	def move_down_small(self, start):
		x = start[0]
		y = start[1]
		current_rows = []
		while (y <= 12):
			current_rows.append([x,y])
			x = x - 1
			current_rows.append([x,y])
			x = x + 1
			y = y + 1
		return current_rows

	def create_data_coord(self):
		data_coord = self.move_up_med([20,20])
		data_coord.extend(self.move_down_med([18,9]))
		data_coord.extend(self.move_up_med([16,20]))
		data_coord.extend(self.move_down_med([14,9]))

		data_coord.extend(self.move_up_avoid_timing([12,20]))
		data_coord.extend(self.move_down_avoid_timing([10,0]))

		data_coord.extend(self.move_up_small([8,12]))
		data_coord.extend(self.move_down_small([5,9]))
		data_coord.extend(self.move_up_small([3,12]))
		data_coord.extend(self.move_down_small([1,9]))
		return data_coord


	def draw_type_bits(self, mask):
		type_bits = self.get_type_bits(mask)
		type_inputs = type_bits + type_bits

		x = 0
		y = 8
		MyPoints = []
		while (x <= 20):
			if (x<=7):
				if (x != 6):
					MyPoints.append(Point(x,y))
			if (x>=13):
				MyPoints.append(Point(x,y))
			x = x + 1
		x = 8
		y = 0
		while (y <= 20):
			if (y <= 8):
				if (y != 6):
					MyPoints.append(Point(x,y))
			if (y>=14):
				MyPoints.append(Point(x,y))
			y = y + 1


		for i in range(len(MyPoints)):
			MyPoints[i].set_value(type_inputs[i])
			i = i + 1

		return MyPoints

	def get_type_bits(self, mask):
		if (mask==0):
			type_info_bits= [0,1,1,0,1,0,1,0,1,0,1,1,1,1,1]
		if (mask==1):
			type_info_bits= [0,1,1,0,0,0,0,0,1,1,0,1,0,0,0]
		if (mask==2):
			type_info_bits= [0,1,1,1,1,1,1,0,0,1,1,0,0,0,1]
		if (mask==3):
			type_info_bits= [0,1,1,1,0,1,0,0,0,0,0,0,1,1,0]
		if (mask==4):
			type_info_bits= [0,1,0,0,1,0,0,1,0,1,1,0,1,0,0]
		if (mask==5):
			type_info_bits= [0,1,0,0,0,0,1,1,0,0,0,0,0,1,1]
		if (mask==6):
			type_info_bits= [0,1,0,1,1,1,0,1,1,0,1,1,0,1,0]
		if (mask==7):
			type_info_bits= [0,1,0,1,0,1,1,1,1,1,0,1,1,0,1]
		return type_info_bits


	def design_mask(self, point, input_bit, mask):
		x = point.x
		y = point.y
		output_bit = input_bit
		if (mask == 0):
			if ( (y+x)%2 == 0):
				if (input_bit == 0):
					output_bit = 1
				if (input_bit == 1):
				 	output_bit = 0
		if (mask == 1):
			if ( y%2 == 0):
				if (input_bit == 0):
					output_bit = 1
				if (input_bit == 1):
				 	output_bit = 0
		if (mask == 2):
			if ( y%3 == 0):
				if (input_bit == 0):
					output_bit = 1
				if (input_bit == 1):
				 	output_bit = 0
		if (mask == 3):
			if ( (y+x)%3 == 0):
				if (input_bit == 0):
					output_bit = 1
				if (input_bit == 1):
				 	output_bit = 0
		if (mask== 4):
			if ( ((y/2)+(x/3))%3 == 0):
				if (input_bit == 0):
					output_bit = 1
				if (input_bit == 1):
				 	output_bit = 0
		if (mask == 5):
			if ( ((y*x)%2)+((y*x)%3) == 0):
				if (input_bit == 0):
					output_bit = 1
				if (input_bit == 1):
				 	output_bit = 0
		if (mask == 6):
			if ( (((y*x)%2)+((y*x)%3))%2 ==0):
				if (input_bit == 0):
					output_bit = 1
				if (input_bit == 1):
				 	output_bit = 0
		if (mask == 7):
			if ( (((y+x)%2)+((y*x)%3))%2 ==0):
				if (input_bit == 0):
					output_bit = 1
				if (input_bit == 1):
				 	output_bit = 0
		return output_bit
	def add_penalty(self, new_penalty):
		self.penalty = self.penalty + new_penalty
	def ordergrid_h(self):
		i = 0
		j = 0
		tarray = []
		for i in range(20):
			tarray.append(self.grid[i].gen_val_list())
		print tarray
		




def display():
	def display_QR():
		qr_bitstring = polynomials.QRbitstring(entry.get().upper())
		i = 0
		for i in range(8):
			canvas = mygui.ca(width=300, height=300)
			canvas.config(bg='white')
			g = Mask(i, qr_bitstring)
			g.drawSquares(canvas)
	

	g = Mask(0, qr_bitstring)

	mygui = Gui()
	mygui.title('QR Encoder')
	label = mygui.la(text='Enter the text to encode here:')
	entry = mygui.en()
	button = mygui.bu(text='Make QR Code', command=display_QR)
	mygui.gr(cols=4)
	mygui.mainloop()
display()
