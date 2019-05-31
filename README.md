# Overview
This serves as a minimal reproducible case for [a loguru bug](https://github.com/Delgan/loguru/issues/102)

# Environment
This was discovered using
* Python 3.7.3 via pyenv
* Ubuntu 18.04

# To run
```
./run.sh
```
Running installs the venv (via `./install_venv.sh`, activates the venv, then runs the program)


# Output / Error
The output it produces is:

```
my_id:      0, my_process: <_MainProcess(MainProcess, started)>
2019-05-31 05:51:03.417 | INFO     | __main__:do_something:11 - my_id:      0, my_process: <_MainProcess(MainProcess, started)>
my_id:      1, my_process: <_MainProcess(MainProcess, started)>
2019-05-31 05:51:03.417 | INFO     | __main__:do_something:11 - my_id:      1, my_process: <_MainProcess(MainProcess, started)>
my_id:      2, my_process: <_MainProcess(MainProcess, started)>
2019-05-31 05:51:03.417 | INFO     | __main__:do_something:11 - my_id:      2, my_process: <_MainProcess(MainProcess, started)>
my_id:      3, my_process: <_MainProcess(MainProcess, started)>
2019-05-31 05:51:03.418 | INFO     | __main__:do_something:11 - my_id:      3, my_process: <_MainProcess(MainProcess, started)>
my_id:      4, my_process: <_MainProcess(MainProcess, started)>
2019-05-31 05:51:03.418 | INFO     | __main__:do_something:11 - my_id:      4, my_process: <_MainProcess(MainProcess, started)>
Process ForkPoolWorker-1:
Traceback (most recent call last):
  File "/home/enelson/.pyenv/versions/3.7.3/lib/python3.7/multiprocessing/process.py", line 297, in _bootstrap
    self.run()
  File "/home/enelson/.pyenv/versions/3.7.3/lib/python3.7/multiprocessing/process.py", line 99, in run
    self._target(*self._args, **self._kwargs)
  File "/home/enelson/.pyenv/versions/3.7.3/lib/python3.7/multiprocessing/pool.py", line 110, in worker
    task = get()
  File "/home/enelson/.pyenv/versions/3.7.3/lib/python3.7/multiprocessing/queues.py", line 354, in get
    return _ForkingPickler.loads(res)
AttributeError: 'Logger' object has no attribute 'log_function'
Process ForkPoolWorker-2:
Traceback (most recent call last):
  File "/home/enelson/.pyenv/versions/3.7.3/lib/python3.7/multiprocessing/process.py", line 297, in _bootstrap
    self.run()
  File "/home/enelson/.pyenv/versions/3.7.3/lib/python3.7/multiprocessing/process.py", line 99, in run
    self._target(*self._args, **self._kwargs)
  File "/home/enelson/.pyenv/versions/3.7.3/lib/python3.7/multiprocessing/pool.py", line 110, in worker
    task = get()
  File "/home/enelson/.pyenv/versions/3.7.3/lib/python3.7/multiprocessing/queues.py", line 354, in get
    return _ForkingPickler.loads(res)
AttributeError: 'Logger' object has no attribute 'log_function'
Process ForkPoolWorker-3:
Traceback (most recent call last):
  File "/home/enelson/.pyenv/versions/3.7.3/lib/python3.7/multiprocessing/process.py", line 297, in _bootstrap
    self.run()
  File "/home/enelson/.pyenv/versions/3.7.3/lib/python3.7/multiprocessing/process.py", line 99, in run
    self._target(*self._args, **self._kwargs)
  File "/home/enelson/.pyenv/versions/3.7.3/lib/python3.7/multiprocessing/pool.py", line 110, in worker
    task = get()
  File "/home/enelson/.pyenv/versions/3.7.3/lib/python3.7/multiprocessing/queues.py", line 354, in get
    return _ForkingPickler.loads(res)
AttributeError: 'Logger' object has no attribute 'log_function'
Process ForkPoolWorker-4:
Traceback (most recent call last):
  File "/home/enelson/.pyenv/versions/3.7.3/lib/python3.7/multiprocessing/process.py", line 297, in _bootstrap
    self.run()
  File "/home/enelson/.pyenv/versions/3.7.3/lib/python3.7/multiprocessing/process.py", line 99, in run
    self._target(*self._args, **self._kwargs)
  File "/home/enelson/.pyenv/versions/3.7.3/lib/python3.7/multiprocessing/pool.py", line 110, in worker
    task = get()
  File "/home/enelson/.pyenv/versions/3.7.3/lib/python3.7/multiprocessing/queues.py", line 354, in get
    return _ForkingPickler.loads(res)
AttributeError: 'Logger' object has no attribute 'log_function'
Process ForkPoolWorker-5:
Traceback (most recent call last):
  File "/home/enelson/.pyenv/versions/3.7.3/lib/python3.7/multiprocessing/process.py", line 297, in _bootstrap
    self.run()
  File "/home/enelson/.pyenv/versions/3.7.3/lib/python3.7/multiprocessing/process.py", line 99, in run
    self._target(*self._args, **self._kwargs)
  File "/home/enelson/.pyenv/versions/3.7.3/lib/python3.7/multiprocessing/pool.py", line 110, in worker
    task = get()
  File "/home/enelson/.pyenv/versions/3.7.3/lib/python3.7/multiprocessing/queues.py", line 354, in get
    return _ForkingPickler.loads(res)
AttributeError: 'Logger' object has no attribute 'log_function'
^CProcess ForkPoolWorker-6:
Traceback (most recent call last):
  File "/home/enelson/.pyenv/versions/3.7.3/lib/python3.7/multiprocessing/process.py", line 297, in _bootstrap
    self.run()
  File "/home/enelson/.pyenv/versions/3.7.3/lib/python3.7/multiprocessing/process.py", line 99, in run
    self._target(*self._args, **self._kwargs)
  File "/home/enelson/.pyenv/versions/3.7.3/lib/python3.7/multiprocessing/pool.py", line 110, in worker
    task = get()
  File "/home/enelson/.pyenv/versions/3.7.3/lib/python3.7/multiprocessing/queues.py", line 352, in get
    res = self._reader.recv_bytes()
  File "/home/enelson/.pyenv/versions/3.7.3/lib/python3.7/multiprocessing/connection.py", line 216, in recv_bytes
    buf = self._recv_bytes(maxlength)
  File "/home/enelson/.pyenv/versions/3.7.3/lib/python3.7/multiprocessing/connection.py", line 407, in _recv_bytes
    buf = self._recv(4)
  File "/home/enelson/.pyenv/versions/3.7.3/lib/python3.7/multiprocessing/connection.py", line 379, in _recv
    chunk = read(handle, remaining)
KeyboardInterrupt
Traceback (most recent call last):
  File "src/bugged.py", line 32, in <module>
    main()
  File "src/bugged.py", line 27, in main
    pool.join()
  File "/home/enelson/.pyenv/versions/3.7.3/lib/python3.7/multiprocessing/pool.py", line 556, in join
    self._worker_handler.join()
  File "/home/enelson/.pyenv/versions/3.7.3/lib/python3.7/threading.py", line 1032, in join
    self._wait_for_tstate_lock()
  File "/home/enelson/.pyenv/versions/3.7.3/lib/python3.7/threading.py", line 1048, in _wait_for_tstate_lock
    elif lock.acquire(block, timeout):
KeyboardInterrupt
```