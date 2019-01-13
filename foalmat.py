import scrollphathd as sch
import time
from scrollphathd.fonts import font5x5

def get_time_left():
	secs = time.time() - start_time
	mins = secs/60
	return mins

mins_to_wait = 99
start_time = time.time()

sch.clear()
sch.rotate(180)

sch.write_string(
	'>>> COME BACK IN..... ',
	x=50,
	y=0,
	brightness=0.3,
)

for i in range(150):
	sch.scroll(1)
	sch.show()
	time.sleep(0.02)

sch.clear()




sch.write_string(
	"88m",
	x=0,
	y=0,
	brightness=0.1,
)
sch.show()

print get_time_left()

sch.rotate(180)
sch.show()

time.sleep(3000)
