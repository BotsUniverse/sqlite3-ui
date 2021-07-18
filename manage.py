import sys
import subprocess
import _thread




def main(args):
    if len(args) < 1:
        print("Use 'py manage.py -help' for help.")
        print("Usage: 'py manage.py [command] [options]'")
    

    if args[0] == "start":
        print("- Starting server with python and app with javascript")
        commands = ["py main.py", "npm start"]
        procs = [ subprocess.Popen(i, shell=True) for i in commands ]

        print("Press Ctrl-C to terminate.")
        for p in procs:
            p.wait()

        print("# Process finished.")

    if args[0] == "install":
        print("- installing required python packages")
        subprocess.run(["pip", "install", "-r", "requirements.txt"], shell=True)
        print("* Successfully installed python packages")


    if args[0] == "env":
        print("Starting env")
        subprocess.run(["env\\Scripts\\activate"], shell=True)
        subprocess.run(["echo", "%PYTHONPATH%"], shell=True)



if __name__ == '__main__':
    main(sys.argv[1:])