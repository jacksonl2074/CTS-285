# M2T1 - Webapp #1

## GOALS:
- to learn basic Flask programming
- to be able to repeat a server config
- maybe to have fun

## lessons learned
bash commands you cannot live without:
- ls     <-- what's in this directory
- cd     <-- change directory
- source     <-- run a script (like activate)

## instructions
initial tutorial: https://blog.pythonanywhere.com/121/
but we're using codespaces instead of PA

install library:
first set up virtualenvironment
    - pip install virtualenv
    - virtualenv venv
    - source venv/bin/activate
now we have our "venv" environment so we can install things in it
to turn it off:
- deactivate

start installing requirements:
- pip install flask
- pip freeze > requirements.txt

now we can write our minimal Flask app to test it
TODO: write a Flask app that does something useful!

to start:
- flask --app hello run
- flask --debug --app hello run (can run this in debug mode)

----
starting up again:
- cd M2HW2
- source venv/bin/activate
- flask --debug --app app run

- (make sure virt env is in the folder you're working in, ex: @jacksonl2074 ➜ /workspaces/CTS-285/M2HW2 (main) $ pip install virtualenv)

## M2T2
Next, we start with a "first cut with dummy data"
- add main_page.html
