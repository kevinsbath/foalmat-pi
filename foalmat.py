
import scrollphathd as sch
import time
from scrollphathd.fonts import font5x5

def sch_setup():
	sch.clear()
	sch.rotate(180)



def sch_setup_string(display_string):
	sch.write_string(
		display_string,
		x=50,
		y=0,
		brightness=0.3,
	)

	for i in range(150):
		sch.scroll(1)
		sch.show()
		time.sleep(0.02)


def get_time_left():
	secs = time.time() - start_time
	mins = secs/60
	return mins

def main():
	mins_to_wait = 99
	start_time = time.time()
	sch_setup()
	sch_display_string(">>> Come back in ....")



if __name__ == "__main__":
	main()
	time.sleep(3000)
