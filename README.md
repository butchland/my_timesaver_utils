# My Timesaver utilities
> A set of simple utilities I found useful to import 


This is the current list of functions

* Profiling Utilities
    * `@profile_call(fname=None)` - a function or method decorator to record execution times
    * `print_prof_data(fname=None)` - prints out profile data for function `fname` or all functions if `fname` is None
    * `clear_prof_data()` - clears out profile data
    * `get_prof_data(fname)` - get exec times for `fname`
    * `start_record(fname)` - start recording time for `fname` (alternative to decorator if function cannot decorated)
    * `end_record(fname)` - stop recording and add elapsed time for `fname` 
    * `save_prof_data(file_name)` - save profile data to `file_name`
    * `load_prof_data(file_name)` - load profile data from `file_name`
 

## Install

`pip install git+https://github.com/butchland/my_timesaver_utils.git`

## How to use

### Profiling Utils

Import the utils -- You can either import all the utilities
```
from my_timesaver_utils import *
```
Or you can import only the profiling package
```
from my_timesaver_utils.profiling import *
```

Decorate method or function you want to profile

```
import time

@profile_call
def test_func(t=2.0):
    time.sleep(1)
    
```

Call your method or function

```
for i in range(10):
    test_func(i)
```

You can also add an optional funcname if you want to replace the name its stored in the profile data

```
@profile_call('wachacha')
def test_func2():
    time.sleep(1.0)
```

```
for i in range(3):
    test_func2()
    
```

Print your profile data

```
print_prof_data('test_func')
```

    Function test_func called 10 times.
    Execution time max: 1.005, average: 1.004


Print your profile data for the test_func2 (aka wachacha)

```
print_prof_data('wachacha')
```

    Function wachacha called 3 times.
    Execution time max: 1.005, average: 1.004


Get your profile data (e.g. good for graphing)

```
times = get_prof_data('test_func'); times
```




    [1.0050780773162842,
     1.005082130432129,
     1.0029971599578857,
     1.0050528049468994,
     1.0050477981567383,
     1.005047082901001,
     1.001734972000122,
     1.0003960132598877,
     1.005075216293335,
     1.005049228668213]



If you can't add a decorator, you can start and end the recording manually and it will be added to the profile data

```
for i in range(10):
    start_record('sleep')
    time.sleep(1.)
    end_record('sleep')
```

As an alternative, the decorator can be invoked this way

```
sleep = profile_call(time.sleep)
```

```
for i in range(5):
    sleep(i)
```

You can also pass in an optional function name to replace the func name used in the profile data

```
sleep2 = profile_call(time.sleep, 'maluman')
```

```
for i in range(3): sleep2(1)
```

If you call `print_prof_data` without any arguments, it will print all the timings for all the functions

```
print_prof_data()
```

    Function test_func called 10 times.
    Execution time max: 1.005, average: 1.004
    Function wachacha called 3 times.
    Execution time max: 1.005, average: 1.004
    Function sleep called 15 times.
    Execution time max: 4.005, average: 1.336
    Function maluman called 3 times.
    Execution time max: 1.004, average: 1.004


You can also get the profile data for the manually recorded calls as well.

```
times2 = get_prof_data('sleep')
```

You can also save the profile data to a file

```
save_file = 'my_profile_data.pickle'
```

```
save_prof_data(save_file)
```

Calling the `clear_prof_data` will clear out all the previously recorded timings.

```
clear_prof_data()
```

```
print_prof_data()
```

You can reload the profile data from a previously saved file

```
load_prof_data(save_file)
```

```
print_prof_data()
```

    Function test_func called 10 times.
    Execution time max: 1.005, average: 1.004
    Function wachacha called 3 times.
    Execution time max: 1.005, average: 1.004
    Function sleep called 15 times.
    Execution time max: 4.005, average: 1.336
    Function maluman called 3 times.
    Execution time max: 1.004, average: 1.004

