## README: Teddie/Jessica, you want to list of decimal integers in the last line
        ## of this script that is # printed with 'For Teddie ...'
        ## also, i used Python 3.0, so you'll have to change the # print()
        ## statements to remove the parenthesis, if running it in Python 27


### QR code encoding

###We are using alpha-numeric mode - bitstring 0010
###We are encoding "Hello World"
# alphanumeric = '0010'
# text = "HELLO WORLD"

def GenerateMessage(alphanumeric, text):
	text_list = list(text)
	# print 'text is',text_list,'\n'
	text_size = len(text_list)

	###convert size of text to binary
	#text_size_binary = bin(text_size)
	## print(text_size_binary)

	###Encode length of data with VERSION 1
	###Version 1: alphanumeric mode: 9 Bits Long
	# print 'Step 2: Encode length of data'

	text_9bits_binary = '{0:0>9b}'.format(text_size)
	# print 'text_size_binary (9bits): ',text_9bits_binary

	##Our bit string so far
	bit_string = alphanumeric + text_9bits_binary
	# print 'End of Step 2 (version1 and alphanumeric): ', bit_string,'\n'

	#========
	# print('Step 3: Encode the Data')

	## Make dictionary of the alpha-numeric values this tutorial person uses (it's not ascii!!)
	alphanumeric_list = (0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,'A',10,'B',11,'C',12,'D',13,'E',14,'F',15,'G',16,'H',17,'I',18,'J',19,'K',20,'L',21,'M',22,'N',23,'O',24,'P',25,'Q',26,'R',27,'S',28,'T',29,'U',30,'V',31,'W',32,'X',33,'Y',34,'Z',35,' ',36,'$',37,'%',38,'*',39,'+',40,'-',41,'.',42,'/',43,':',44)
	alphanumeric_dict = dict(alphanumeric_list[i:i+2] for i in range(0, len(alphanumeric_list), 2)); #makes dictionary of above list

	def split_string(n, bit_string):  #split string into groups of 'n'
			L = bit_string
			list_of_lists = [L[i:i+n] for i in range(0, len(L), n)]
			# print  'list split by ',n, 'here: ',list_of_lists 
			return list_of_lists

	#now split string into groups of 2
	n = 2
	encoded_pairs = split_string(2,text_list)

	#For each pair of characters, we take the ASCII value of the first character
	#and multiply it by 45. Then we add that number to the ASCII value of the second
	#character. Then we convert the result into an 11-bit binary string. 
	#If you are encoding an odd number of characters, as we are here,
	#take the ASCII value of the final character and convert it into a 6-bit binary string.

	for i in encoded_pairs:
			# print 'list',i 
			if len(i)==1:  #last list has one element only
				encoded= alphanumeric_dict[i[0]]
				encoded_binary = '{0:0>6b}'.format(encoded)
				## print(encoded)
				bit_string += encoded_binary  #add onto bitstring
				
			else:
				encoded = alphanumeric_dict[i[0]]*45 + alphanumeric_dict[i[1]]
				## print(encoded)
				encoded_binary = '{0:0>11b}'.format(encoded)
				bit_string += encoded_binary

	# print 'bit string is\n', bit_string, '\n' 

	#===========

	# print "Step 4: Terminate the Bits" 


	#We have chosen to use QR code version 1 with level Q error
	#correction. For this, we must generate 104 data bits (refer to the
	#Denso-Wave version capacity table for this information.) If our bit
	#string is shorter than 104, then we must add up to four 0s to the
	#end. If adding four zeroes would make the string longer than 104,
	#though, then we would only add the number of zeroes necessary to make
	#the string 104 bits long.  \ Since our string is 59 bits long, we add
	#four 0s to the end. If our string had ended up being 102 bits long
	#(just as an example) we would only add two 0s to the end, for a total
	#of 104 bits.

	# print 'length of bit string',len(bit_string) 

	if(len(bit_string)>99):
		bit_string ='{0:0<104}'.format(bit_string)
	else:
		bit_string += '0000'
	# print 'string is now padded with length ', len(bit_string), 'and is\n',bit_string,'\n'



	## HERE, we can also do bit_string%8 and add as many zeroes as needed at the end!
	# print "Step 5: Delimit into 8-bit words, then pad with 0s"

	new_zeros = (8-(len(bit_string)%8))  # find how many zeroes needed at the end
	# print "number of zeroes to add",new_zeros 

	for i in range(0,new_zeros):  #add those zeros; could be done better than for loop
			bit_string +='0'

	# print "padded bit string\n", bit_string,'\n' 


	# print "Step 6: Add words at the end if the string is too short\n"
	special_string1 ='11101100'
	special_string2 = '00010001'

	while(len(bit_string) < 104):
		bit_string+=special_string1
		if (len(bit_string) < 104):
			bit_string+=special_string2

	# print "After special strings" 
	# print 'final bit string is length',len(bit_string),':\n',(bit_string) 

	#################
	#################

	## Broken up for Teddie
	bit_string_broken = split_string(8,bit_string)
	print bit_string_broken
	decimal_string = [int(string,base=2) for string in bit_string_broken]
	# # print '\nFor Teddie:\n',decimal_string 
	return decimal_string





