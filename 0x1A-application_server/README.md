# 0x1A. Application server

## Resources:books:
Read or watch:
* [Application server vs web server](https://intranet.hbtn.io/rltoken/RerpYBxsgrpIorHjbDgulw)
* [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](https://intranet.hbtn.io/rltoken/uosy5QXdMbDPA1tFTR1eoA)
* [Running Gunicorn](https://intranet.hbtn.io/rltoken/QTnnkj6vfQV9ovW_eYWWDQ)
* [Be careful with the way Flask manages slash](https://intranet.hbtn.io/rltoken/whE8do28ZiJJoJLyb1ACwA)
* [route](https://intranet.hbtn.io/rltoken/JLjrXD4MLS3rUkQr5QyxtA)
* [Upstart documentation](https://intranet.hbtn.io/rltoken/oQPs-o5UUcZkxOw5sNIM0g)

---
## Learning Objectives:bulb:
What you should learn from this project:

---

### [0. Set up development with Python](./README.md)
* Let’s serve what has been built for AirBnB clone v2 - Web framework on web-01. This task is an exercise in setting up development environment, which is used for testing and debugging code before deploying it to production.


### [1. Set up production with Gunicorn](./2-app_server-nginx_config)
* Now that you have a working development environment, we can go on to configuring the Gunicorn application server on web-01, port 5000, as the live server. Gunicorn, along with any other libraries your programme may need, must be installed. The object you create in Flask will be the WSGI entry point for your app. This is where your final product will be assembled. So that the circumstances for providing your dynamic content are consistent throughout the production and development environments, we need that you utilise the same port for both.


### [2. Serve a page with Nginx](./3-app_server-nginx_config)
* Building on the work in the previous tasks, configure Nginx to serve your page from the route /airbnb-onepage/


### [3. Add a route with query parameters](./4-app_server-nginx_config)
* Let's build upon your past work and give Gunicorn more to do by adding a new service to our web app. The route /number_odd_or_even/int:n> should already be created in AirBnB_clone_v2/web_flask/6-number_odd_or_even to display a page indicating if an integer is odd or even. A Gunicorn instance listening on port 5001 must be configured to receive HTTP requests for the route /airbnb-dynamic/number_odd_or_even/(any integer) through a Nginx proxy. Nginx must be set up in a certain way so that it proxies requests to processes that are listening on two separate ports. It is not required that you maintain active application server processes. See below for advice on running several instances of Gunicorn without needing to switch between terminal windows.


### [4. Let's do this for your API](./5-app_server-nginx_config)
* Let’s serve what you built for AirBnB clone v3 - RESTful API on web-01.


### [5. Serve your AirBnB clone](./gunicorn.service)
* Let's put everything you've made available on web-01 for our AirBnB clone..


### [6. Deploy it!](./4-reload_gunicorn_no_downtime)
* Once your application server is ready to go, you may have it start automatically every time Linux boots. This manner, if you need to restart your server (shut it down or restart it) for any reason, the Gunicorn process (or processes) will begin running automatically as soon as the server is up and running again. Systemd will be used for this purpose. More information on systemd may be found in the project's README file, but in brief, it is a daemon that performs several system startup tasks for the Linux operating system. You'll need to create a systemd script to automatically launch your application server for this assignment. You may skip creating a Unix socket to bind the process to as it's shown in the video at the start of the project.


---

## Author
* **Adebanji Adeniyi** - [deniyibanji2@gmail.com](https://github.com/ADETOLA01)
