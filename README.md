This is an example of a middleware that records profiles for all requests made by authenticated users.

The profile visualizer is shamelessly stolen from the original vmprof release at: [ https://github.com/vmprof/vmprof-python ]

If you're trying to include this in your own work, make sure to pass `real_time=True` to `vmprof.enable()`.

A standalone version of the Django vmprof integration is on Github and PyPi, it's included here for ease of access.

Have fun!

Simple setup:

```
$ ./manage.py migrate
$ ./manage.py createsuperuser
$ ./manage.py runserver --nothreading --noreload
```

1. Go to http://localhost:8000/admin/
2. Log in.
3. Go to http://localhost:8000/
4. Go to http://localhost:8000/profiler/
5. Click around, go wild.

