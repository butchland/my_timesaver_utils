# My Timesaver utilities
> A set of simple utilities I found useful to import 


This is the current list of functions

* Profiling Utilities
    * `@profile_call` - a function or method decorator to record execution times
    * `print_prof_data(fname=None)` - prints out profile data for function `fname` or all functions if `fname` is None
    * `clear_prof_data()` - clears out profile data
    * `get_prof_data(fname)` - get exec times for `fname`
    * `start_record(fname)` - start recording time for `fname` (alternative to decorator if function cannot decorated)
    * `end_record(fname)` - stop recording and add elapsed time for `fname` 
 

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
    time.sleep(t)
    
```

Call your method or function

```
for i in range(10):
    test_func(i)
```

Print your profile data

```
print_prof_data('test_func')
```

    Function test_func called 10 times.
    Execution time max: 9.005, average: 4.504


Get your profile data (e.g. good for graphing)

```
times = get_prof_data('test_func'); times
```




    [1.0967254638671875e-05,
     1.005072832107544,
     2.0050249099731445,
     3.0050220489501953,
     4.0050060749053955,
     5.003612995147705,
     6.004514932632446,
     7.004956960678101,
     8.004937887191772,
     9.004918098449707]



If you can't add a decorator, you can start and end the recording manually and it will be added to the profile data

```
for i in range(10):
    start_record('sleep')
    time.sleep(i)
    end_record('sleep')
```

If you call `print_prof_data` without any arguments, it will print all the timings for all the functions

```
print_prof_data()
```

    Function test_func called 10 times.
    Execution time max: 9.005, average: 4.504
    Function sleep called 10 times.
    Execution time max: 9.005, average: 4.504


You can also get the profile data for the manually recorded calls as well.

```
times2 = get_prof_data('sleep')
```

Calling the `clear_prof_data` will clear out all the previously recorded timings.

```
clear_prof_data()
```

```
print_prof_data()
```
