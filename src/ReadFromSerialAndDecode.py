import serial
import sys
import time
import msvcrt
current_time_in_micro = lambda: int(round(time.time() * 1000000))

def tohex(s):
	o = ''
	for c in s:
		t = hex(ord(c))
		if ord(c) < 16:
			t = '0' + str(t)[-1:]
		else:
			t = t[-2:]
		o += '\\x' + t
	return o # + '--------' + s
	
	
	
ser = serial.Serial(
	port='COM4',\
	baudrate=2000000,\
	parity=serial.PARITY_NONE,\
	stopbits=serial.STOPBITS_ONE,\
	bytesize=serial.EIGHTBITS,\
		timeout=0)

print("Serial connected to: " + ser.portstr)

#print("{}".format(tohex(ser.readline())))

READ_OUTPUT = False
TRIGGER = False
TRIGGERED = False

print "WAITING FOR SERIAL TO BE READY..."
time.sleep(2)
print "PRESS ENTER TO START READING FROM SERIAL..."

cont = 0
loopN = 0
out = ''
while True:
	v = ser.readline()
#	tmp = "{};{}#".format(current_time_in_millis(), tohex(v))
	tmp = "{};{}#".format(loopN, v)
	#print tmp
	if READ_OUTPUT:
		# print tmp
		if (len(v) > 0 and v != ''):
			try:
				if int(v,10) < 100:
					TRIGGER = True
					cont = 0
				else:
					cont += 1
				
				if TRIGGER:
					out += tmp
					if not TRIGGERED:
						TRIGGERED = True
						print "TRIGGER OK!"
					if cont > 100:
						print "END OF SIGNAL..."
						break;
			except:
				pass
	loopN += 1
	# QUIT ON ESC
	if msvcrt.kbhit():
		x = msvcrt.getch()
		if ord(x) == 13:	# enter			START READING
			READ_OUTPUT = not READ_OUTPUT
			if READ_OUTPUT:
				print "WAITING FOR TRIGGER... (PRESS A BUTTON ON THE REMOTE CONTROL)"
				print "READING FROM SERIAL..."
			else:
				print "STOP READING SERIAL..."
		
		if ord(x) == 32:	# space		STOP  READING
			READ_OUTPUT = False
			break

# with open("output.txt","w") as f:
# 	f.write(out.replace('\r','').replace('\n',''))

ser.close()

LastBitReceived = 1
CountSeqOnes 	= 0
CountSeqZeros 	= 0
decoded 		= ''


LowValue = out.split('#')[0].split(';')[0]

InitParsing = False

out = out.replace('\r','').replace('\n','')
	
for row in out.split('#'):
	
	tmp = row.split(';')
	
	if len(tmp) == 2:
	
		LoopNumber = int(tmp[0],10)
		AnalogValue = int(tmp[1],10)
		
		# DEBUG
		#print "LoopNumber: {}".format(LoopNumber)
		#print "AnalogValue: {}".format(AnalogValue)
	
		# ASSUME VALUE BIGGER THAN 50 ZERO
		if( AnalogValue > 50):
			CurrentBit = 0		                   # DIGITAL 0
		else:
			CurrentBit = 1		                   # DIGITAL 1
		
		# DEBUG
		#print "CURRENT BIT: {}".format(CurrentBit)
		
		# IF InitParsing
		if(InitParsing):
		
			if(CurrentBit == 1):
				# IF TRIGGERING NEW PULSATION
			
			
				if(LastBitReceived == 0):	                # EDGE TRIGGER FROM 0 TO 1
				
					if(CountSeqZeros > 4):
						decoded += "0"	                   	# LONG PULSE IS 0
					else:
						decoded += "1"	                   	# SHORT PULSE IS 1
					
					CountSeqZeros 	= 0;
					CountSeqOnes 	= 1;
					
				else:	                   					# PULSATION 1 CONTINUES
					CountSeqOnes += 1
				
			
			else:
				
				if(LastBitReceived == 0):	                   # PULSATION 0 CONTINUES
					CountSeqZeros += 1
					
					# WHEN WE REACH 10 ZEROS CONSECUTIVELY THE SIGNAL IS COMPLETELY SENT.
					if(CountSeqZeros == 10):
						decoded += "0"	                   			# LONG PULSE IS 0
					
				else:	                   # EDGE TRIGGER FROM 1 TO 0
					CountSeqZeros 	= 1
					CountSeqOnes 	= 0
				
			
		else:		                   # CHECK FOR PARSE
			if(LastBitReceived == 1):
			
				if(CurrentBit == 1):		# NOW IT IS WAITING FOR TRIGGER
					CountSeqOnes += 1
				elif(CurrentBit == 0 and CountSeqOnes > 7):
					# NOW REMOTE CONTROL IS TRANSMITTING SIGNAL.
					# IT SENDING SOME ZEROS TO WAKE UP DEVICE.
					CountSeqOnes 	= 0
					CountSeqZeros 	= 1
					# WAITING FOR NEXT 1 TO TRIGGER UP
				
			else:
			
				if(CurrentBit == 1 and CountSeqZeros > 7):   # NOW IT IS TIME TO START PARSING THE SIGNAL
					CountSeqOnes = 1
					CountSeqZeros = 0
					InitParsing = True
				elif(CurrentBit == 0):
					CountSeqZeros += 1

		# END IF InitParsing
		
		LastBitReceived = CurrentBit;


		
decoded = " ".join(decoded[i:i+8] for i in range(0, len(decoded), 8))
decoded_hex = ' '.join(  str(hex( int(s, 2) ) ) for s in decoded.split(' ')  )

print ""
print "DECODED:     {}".format( decoded )
print "HEX DECODED: {}".format( decoded_hex )
	
exit()
