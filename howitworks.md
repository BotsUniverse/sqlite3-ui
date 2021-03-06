# How It Works?

### Intro
> Well, its not that complicated. That has two languages running at the same time. One is the python's [flask framework](https://pypi.org/project/Flask/) running on localhost, and other is the [electronjs framework](https://electronjs.org) that interacts with the user (in short, the application).

#### Why Python?
> Python is one of the best backend language that is almost used in all the fields and is constantly updated. It has a vast list of modules that are opensource and has almost all access that a developer needs in an OS.

#### Why Flask?
> Flask is a web development framework that is very simple and neat. It has simple routing and is perfect for light weight web apps.

#### Why Javascript, HTML and CSS?
> When it comes to UI or Frontend, there is no other language like HTML, CSS and JAVASCRIPT that can make a user admire the look. So to make users feel comfortable with the SQILITE3-UI, which is a UI-less database language we use HTML, CSS, JAVASCRIPT.

#### Why Electronjs?
> Now, our goal is to create an app (`executable file`) that can run offline too. We also need a good UI and the use of backend. So, we have JAVASCRIPT that is a language hanging between frontend and backend. And Electronjs is a framework that can be used to create application with HTML, CSS and JAVASCRIPTS along with [nodejs](https://nodejs.org). And JAVSCRIPT can send requests to servers, change and interact with the userinterface. So the elctronjs is the solutaion for creating an application for SQLITE3-UI.

#### How to bring Python with Javascript?
> The next problem is that, we are going to use node modules and python function together, which might seem impossible, but when we want PYTHON to do some small works, we can put those function in the flask framework and make some request with JAVASCRIPT and interact with the user in HTML

#### So what is done?
> Now, we have a server running and an app running. That is two commands at a time. The user might get complicated with the commands. So, there is a `manage.py` file which takes care of all the stuffs that are to be done by the user. Some commands for `manage.py`:
```bash
# Install all the required stuffs for the program to run.
py manage.py install
# Run both the server and the electron together with single command
py manage.py start
```
