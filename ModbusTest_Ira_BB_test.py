
# !/usr/bin/env python
# -*- coding: utf-8 -*-

# read_bit
# read 10 bits and print result on stdout

from pyModbusTCP.client import ModbusClient
import time
import random
import array as arr


# !/usr/bin/env python
# -*- coding: utf-8 -*-

# read_bit
# read 10 bits and print result on stdout

SERVER_HOST = "192.168.0.10"
#SERVER_HOST = "192.168.1.100"
SERVER_PORT = 502
#SERVER_PORT = 7
SERVER_U_ID = 10

c = ModbusClient()

# uncomment this line to see debug message
c.debug(False)

print ('Welcome to PyModbusTCP')

# define modbus server host, port and unit_id
c.host(SERVER_HOST)
c.port(SERVER_PORT)
c.unit_id(SERVER_U_ID)

toggle = True
status = True
addr = 0
number = 2
testIteration = 0


# declare array
#coil_bits_write = arr.array('i', [1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1])
#coil_bits_read = arr.array('i',  [1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1])
coil_bits_write = list((1,0))
coil_bits_read = list((0,1))
#print(coil_bits_write)
#print(coil_bits_read)

while status:
    # open or reconnect TCP to server
    if not c.is_open():
        if not c.open():
            print("unable to connect to "+SERVER_HOST+":"+str(SERVER_PORT))

    #time.sleep(1)
    # pint testIteration
    print(end='\r')
    print('testIteration = ' + str(testIteration), end = '\r')
    testIteration+=1
    # get the number of coils to test
    #numCoilsTest = random.randrange(2, 73)
    numCoilsTest = 72
    #print('numCoilsTest = ' + str(numCoilsTest))


    # get the coil bits data to write
    coil_bits_write.clear()
    for i in range(0, numCoilsTest):
        coil_bits_write.append(bool(random.getrandbits(1)))

    #print(coil_bits_write)

    # write coils
    # if open() is ok, read coils (modbus function 0x01)
    addr=0
    if c.is_open():
        is_ok = c.write_multiple_coils(addr, coil_bits_write)
        if not is_ok:
            print('Dummy')
            print("bit #" + str(addr) + ": unable to write " + str(toggle))
            print('numCoilsTest = ' + str(numCoilsTest), end = '\r')
            break

    #time.sleep(1)
    # if open() is ok, read coils (modbus function 0x01)
    addr=72
    if c.is_open():
        # read 10 bits at address 0, store result in regs list
        coil_bits_read.clear()
        #coil_bits_read = c.read_coils(addr, numCoilsTest)
        coil_bits_read = c.read_discrete_inputs(addr, numCoilsTest)
        # if success display registers
        if not coil_bits_read:
            print('Dummy')
            print("bit ad #0 to : " +str(numCoilsTest) +str(coil_bits_read))
            break

    # compare written with read bits info
    #print(coil_bits_read)

    for i in range(0, numCoilsTest):
    	if i == 23:
    		continue
    	if coil_bits_read[i] != coil_bits_write[i]:
        	print('Error in comparision at Coil ' + str(i))
        	print("Written = " +str(coil_bits_write[i]) + " :: Read :" +str(coil_bits_read[i]))
        	print('numCoilsTest = ' + str(numCoilsTest))
        	print('testIteration = ' + str(testIteration))
        	status = False

c.close()