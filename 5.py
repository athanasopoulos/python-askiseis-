
date=raw_input("Dwse tin imeronia sti morfi dd/mm/yyyy:")
date=date.split("/")
imera=int(date[0])
mhnas=int(date[1])
xronos=int(date[2])
aiwnas=xronos/100
_2sekto=int(date[1])

if (mhnas==2 or mhnas==3 or mhnas==11):
	mhnas=4
elif (mhnas==4 or mhnas==7):
	mhnas=0
elif (mhnas==5):
	mhnas=2
elif (mhnas==6):
	mhnas=5
elif (mhnas==8):
	mhnas=3
elif (mhnas==9 or mhnas==12):
	mhnas=6
elif (mhnas==1 or mhnas==10):
	mhnas=1

	
if (aiwnas==16 or aiwnas==20):
	aiwnas=6
elif (aiwnas==17 or aiwnas==21):
	century=4
elif (aiwnas==18 or aiwnas==22):
	aiwnas=2
elif (aiwnas==19 or aiwnas==23):
	aiwnas=0


etos=(aiwnas+(xronos%100)+(xronos%100)/4)%7
imera=(etos+mhnas+imera)%7	



disekto=1
if (xronos%4==0):
	disekto=2
	
if (disekto==2 and (_2sekto==1 or _2sekto==2)):
	day=day-1


if (imera==0):
	print "Savvato"
elif (imera==1):
	print "Kuriaki"
elif (imera==2):
	print "Deutera"
elif (imera==3):	
	print "Triti"
elif (imera==4):
	print "Tetarti"
elif (imera==5):
	print "Pempti"
elif (imera==6):
	print "Paraskevi"
elif (imera==-1):
	print "Paraskevi"
	
