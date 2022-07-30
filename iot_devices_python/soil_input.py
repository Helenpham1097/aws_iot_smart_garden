from subprocess import Popen, PIPE

# process = Popen(["stdbuf", "-oL", "./a.out"], stdout=PIPE, bufsize=1)
# for line in iter(process.stdout.readline,''):
#     print ((line.decode("utf-8")).strip()),
# process.communicate()

def pipe():
    process = Popen(["stdbuf", "-oL", "./a.out"], stdout=PIPE, bufsize=1)
    for line in iter(process.stdout.readline,''):
        return ((line.decode("utf-8")).strip()),
    process.communicate()

def mqtt_connection():
    print("MQTT connected")

if __name__ == '__main__':
	mqtt_connection()
	try:
		pipe()
	except KeyboardInterrupt:  
		print("Subprocess interrupted by keyboard input")