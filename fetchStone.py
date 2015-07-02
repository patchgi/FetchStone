# coding: utf-8

# Python2.X encoding wrapper (Windows dedicated processing)
import codecs
import sys
import time

sys.stdout = codecs.getwriter('cp932')(sys.stdout)
turn =True
LIMIT=21
stone=LIMIT
def canFetch(_num):
	if _num<4 and _num>0:
		return True
	return False


def fetch(_num):
	global stone
	stone-=_num




if __name__=="__main__":
	print "TOTAL STONE"+str(stone)
	while (True):
	
		if turn:
			data=int(raw_input())
		
			if data!=None:
				if canFetch(data):
					fetch(data)
					if stone<=0:
						break
					turn = not turn
				else:
					print "more fetchable stone"
		else:

			edata=4-data
			print edata
			fetch(edata)


			if stone<=0:
				break

			turn =not turn
		

		print "TOTAL STONE"+str(stone)
		
		

		time.sleep(1)

	if turn:
		print "LOSE"
	else:
		print "WIN"




