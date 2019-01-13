import scrollphathd as sch
import time
from scrollphathd.fonts import font5x5

sch.clear()
sch.rotate(180)

sch.write_string('>>> COME BACK IN..... ')

for i in range(100):
	sch.scroll(1)
	sch.show()

sch.rotate(180)
sch.show()

time.sleep(3000)
