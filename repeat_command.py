import schedule 
import subprocess


def do_something():
    try:
       subprocess.run(["killall", "pluma"])
    except:
        print("Не запустилось")
def main():
    
    schedule.every(300).seconds.do(do_something)
    while True:
        schedule.run_pending()

if __name__ == "__main__":
    main()
