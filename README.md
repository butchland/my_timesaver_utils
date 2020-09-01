# My Timesaver utilities
> A set of simple utilities I found useful to import 


This is the current list of functions

* Profiling Utilities
    * `@profile_call(fname=None)` - a function or method decorator to record execution times
    * `print_prof_data(fname=None)` - prints out profile data for function `fname` or all functions if `fname` is None
    * `clear_prof_data(fname=None)` - clears out profile data for function `fname` or all functions if `fname` is None
    * `get_prof_data(fname)` - get exec times for `fname`
    * `start_record(fname)` - start recording time for `fname` (alternative to decorator if function cannot decorated)
    * `end_record(fname)` - stop recording and add elapsed time for `fname` 
    * `save_prof_data(file_name)` - save profile data to `file_name`
    * `load_prof_data(file_name)` - load profile data from `file_name`
* Profiling Callback
    * `MyProfileCallback` - a fastai `Callback` that provides a hierarchical view of model training time execution
        * `Learner.to_my_profile` - method added to a fastai `Learner` if `my_timesaver_utils.profiling_callback` is imported. Call it to add a `MyProfileCallback` to the `Learner` instance.
        * `Learner.my_profile` - `MyProfileCallback` instance attached to the fastai `Learner` object if `to_my_profile` method is called.
        * `print_stats` - `MyProfileCallback` method to show a hierarchical view of the training lifecycle execution stats (execution counts, avg time, max time)
        * `get_stats` - `MyProfileCallback` method to get the execution stats as a list
        * `clear_stats` - `MyProfileCallback` method to reset the execution stats
        * `reset` - `MyProfileCallback` attribute to set so each call to `Learner.fit` resets the execution counts before starting the training.

## Install

`pip install git+https://github.com/butchland/my_timesaver_utils.git`

## How to use

### Profiling Utils

Import the utils -- You can either import all the utilities
```
from my_timesaver_utils.all import *
```
Or you can import only the profiling package
```
from my_timesaver_utils.profiling import *
```

Decorate method or function you want to profile

```
#hide_output
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

    Function test_func called 20 times.
    Execution time max: 1.005, average: 1.003


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




    [1.0015828609466553,
     1.0050618648529053,
     1.0031030178070068,
     1.005044937133789,
     1.0005640983581543,
     1.0037250518798828,
     1.005134105682373,
     1.0017268657684326,
     1.0040719509124756,
     1.000154972076416,
     1.0042312145233154,
     1.0004308223724365,
     1.0003941059112549,
     1.004988193511963,
     1.0016610622406006,
     1.000688076019287,
     1.0050456523895264,
     1.0013980865478516,
     1.0050151348114014,
     1.005051851272583]



If you can't add a decorator, you can start and end the recording manually and it will be added to the profile data

```
for i in range(10):
    start_record('my_sleep')
    time.sleep(1.)
    end_record('my_sleep')
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

    Function test_func called 20 times.
    Execution time max: 1.005, average: 1.003
    Function wachacha called 3 times.
    Execution time max: 1.005, average: 1.004
    Function my_sleep called 10 times.
    Execution time max: 1.005, average: 1.002
    Function sleep called 5 times.
    Execution time max: 4.005, average: 2.003
    Function maluman called 3 times.
    Execution time max: 1.003, average: 1.002


You can also get the profile data for the manually recorded calls as well.

```
times2 = get_prof_data('sleep');times2
```




    [1.1920928955078125e-05,
     1.0048019886016846,
     2.0013680458068848,
     3.0050129890441895,
     4.004997253417969]



You can also save the profile data to a file

```
save_file = 'my_profile_data.pickle'
```

```
save_prof_data(save_file)
```

Calling `clear_prof_data` for a function will clear out the data for that function

```
clear_prof_data('sleep')
print_prof_data()
```

    Function test_func called 20 times.
    Execution time max: 1.005, average: 1.003
    Function wachacha called 3 times.
    Execution time max: 1.005, average: 1.004
    Function my_sleep called 10 times.
    Execution time max: 1.005, average: 1.002
    Function maluman called 3 times.
    Execution time max: 1.003, average: 1.002


Calling the `clear_prof_data` with no arguments will clear out all the previously recorded timings.

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

    Function test_func called 20 times.
    Execution time max: 1.005, average: 1.003
    Function wachacha called 3 times.
    Execution time max: 1.005, average: 1.004
    Function my_sleep called 10 times.
    Execution time max: 1.005, average: 1.002
    Function sleep called 5 times.
    Execution time max: 4.005, average: 2.003
    Function maluman called 3 times.
    Execution time max: 1.003, average: 1.002


### Profiling Callback

Import the utils -- You can either import all the utilities
```
from my_timesaver_utils.all import *
```
Or you can import only the profiling callback package
```
from my_timesaver_utils.profiling_callback import *
```

#### Example Usage

```
from fastai.vision.all import *
```

Import the whole `my_timesaver_utils` package
```
from my_timesaver_utils.all import *
```
or as an alternative, just import the `profiling_callback` package
```
from my_timesaver_utils.profiling_callback import *
```

Setup your path, data, datablock, dataloaders and learner as usual.

```
path = untar_data(URLs.MNIST_TINY)
```

```
Path.BASE_PATH = path
```

```
datablock = DataBlock(
    blocks=(ImageBlock,CategoryBlock),
    get_items=get_image_files,
    get_y=parent_label,
    splitter=GrandparentSplitter(),
    item_tfms=Resize(28),
    batch_tfms=[]
)
```

```
dls = datablock.dataloaders(path)
```

```
learner = cnn_learner(dls,resnet18,metrics=accuracy)
```

Importing the profiling callback adds a method `to_my_profile` to the `learner` object

```
learner.to_my_profile()
```




    <fastai.learner.Learner at 0x139594d10>



Calling the `to_my_profile` method on the `learner` object adds a callback called `MyProfileCallback` which can be accessed through the `learner` attribute `my_profile`.

```
learner.summary()
```




    Sequential (Input shape: ['64 x 3 x 28 x 28'])
    ================================================================
    Layer (type)         Output Shape         Param #    Trainable 
    ================================================================
    Conv2d               64 x 64 x 14 x 14    9,408      False     
    ________________________________________________________________
    BatchNorm2d          64 x 64 x 14 x 14    128        True      
    ________________________________________________________________
    ReLU                 64 x 64 x 14 x 14    0          False     
    ________________________________________________________________
    MaxPool2d            64 x 64 x 7 x 7      0          False     
    ________________________________________________________________
    Conv2d               64 x 64 x 7 x 7      36,864     False     
    ________________________________________________________________
    BatchNorm2d          64 x 64 x 7 x 7      128        True      
    ________________________________________________________________
    ReLU                 64 x 64 x 7 x 7      0          False     
    ________________________________________________________________
    Conv2d               64 x 64 x 7 x 7      36,864     False     
    ________________________________________________________________
    BatchNorm2d          64 x 64 x 7 x 7      128        True      
    ________________________________________________________________
    Conv2d               64 x 64 x 7 x 7      36,864     False     
    ________________________________________________________________
    BatchNorm2d          64 x 64 x 7 x 7      128        True      
    ________________________________________________________________
    ReLU                 64 x 64 x 7 x 7      0          False     
    ________________________________________________________________
    Conv2d               64 x 64 x 7 x 7      36,864     False     
    ________________________________________________________________
    BatchNorm2d          64 x 64 x 7 x 7      128        True      
    ________________________________________________________________
    Conv2d               64 x 128 x 4 x 4     73,728     False     
    ________________________________________________________________
    BatchNorm2d          64 x 128 x 4 x 4     256        True      
    ________________________________________________________________
    ReLU                 64 x 128 x 4 x 4     0          False     
    ________________________________________________________________
    Conv2d               64 x 128 x 4 x 4     147,456    False     
    ________________________________________________________________
    BatchNorm2d          64 x 128 x 4 x 4     256        True      
    ________________________________________________________________
    Conv2d               64 x 128 x 4 x 4     8,192      False     
    ________________________________________________________________
    BatchNorm2d          64 x 128 x 4 x 4     256        True      
    ________________________________________________________________
    Conv2d               64 x 128 x 4 x 4     147,456    False     
    ________________________________________________________________
    BatchNorm2d          64 x 128 x 4 x 4     256        True      
    ________________________________________________________________
    ReLU                 64 x 128 x 4 x 4     0          False     
    ________________________________________________________________
    Conv2d               64 x 128 x 4 x 4     147,456    False     
    ________________________________________________________________
    BatchNorm2d          64 x 128 x 4 x 4     256        True      
    ________________________________________________________________
    Conv2d               64 x 256 x 2 x 2     294,912    False     
    ________________________________________________________________
    BatchNorm2d          64 x 256 x 2 x 2     512        True      
    ________________________________________________________________
    ReLU                 64 x 256 x 2 x 2     0          False     
    ________________________________________________________________
    Conv2d               64 x 256 x 2 x 2     589,824    False     
    ________________________________________________________________
    BatchNorm2d          64 x 256 x 2 x 2     512        True      
    ________________________________________________________________
    Conv2d               64 x 256 x 2 x 2     32,768     False     
    ________________________________________________________________
    BatchNorm2d          64 x 256 x 2 x 2     512        True      
    ________________________________________________________________
    Conv2d               64 x 256 x 2 x 2     589,824    False     
    ________________________________________________________________
    BatchNorm2d          64 x 256 x 2 x 2     512        True      
    ________________________________________________________________
    ReLU                 64 x 256 x 2 x 2     0          False     
    ________________________________________________________________
    Conv2d               64 x 256 x 2 x 2     589,824    False     
    ________________________________________________________________
    BatchNorm2d          64 x 256 x 2 x 2     512        True      
    ________________________________________________________________
    Conv2d               64 x 512 x 1 x 1     1,179,648  False     
    ________________________________________________________________
    BatchNorm2d          64 x 512 x 1 x 1     1,024      True      
    ________________________________________________________________
    ReLU                 64 x 512 x 1 x 1     0          False     
    ________________________________________________________________
    Conv2d               64 x 512 x 1 x 1     2,359,296  False     
    ________________________________________________________________
    BatchNorm2d          64 x 512 x 1 x 1     1,024      True      
    ________________________________________________________________
    Conv2d               64 x 512 x 1 x 1     131,072    False     
    ________________________________________________________________
    BatchNorm2d          64 x 512 x 1 x 1     1,024      True      
    ________________________________________________________________
    Conv2d               64 x 512 x 1 x 1     2,359,296  False     
    ________________________________________________________________
    BatchNorm2d          64 x 512 x 1 x 1     1,024      True      
    ________________________________________________________________
    ReLU                 64 x 512 x 1 x 1     0          False     
    ________________________________________________________________
    Conv2d               64 x 512 x 1 x 1     2,359,296  False     
    ________________________________________________________________
    BatchNorm2d          64 x 512 x 1 x 1     1,024      True      
    ________________________________________________________________
    AdaptiveAvgPool2d    64 x 512 x 1 x 1     0          False     
    ________________________________________________________________
    AdaptiveMaxPool2d    64 x 512 x 1 x 1     0          False     
    ________________________________________________________________
    Flatten              64 x 1024            0          False     
    ________________________________________________________________
    BatchNorm1d          64 x 1024            2,048      True      
    ________________________________________________________________
    Dropout              64 x 1024            0          False     
    ________________________________________________________________
    Linear               64 x 512             524,288    True      
    ________________________________________________________________
    ReLU                 64 x 512             0          False     
    ________________________________________________________________
    BatchNorm1d          64 x 512             1,024      True      
    ________________________________________________________________
    Dropout              64 x 512             0          False     
    ________________________________________________________________
    Linear               64 x 2               1,024      True      
    ________________________________________________________________
    
    Total params: 11,704,896
    Total trainable params: 537,984
    Total non-trainable params: 11,166,912
    
    Optimizer used: <function Adam at 0x1390a5200>
    Loss function: FlattenedLoss of CrossEntropyLoss()
    
    Model frozen up to parameter group number 2
    
    Callbacks:
      - TrainEvalCallback
      - Recorder
      - ProgressCallback
      - MyProfileCallback



```
learner.my_profile
```




    MyProfileCallback



Call the `print_stats` method on the `my_profile` attribute of the `Learner` object displays a hierarchical list of the training lifecycle events -- in this case with no data yet as the `fit` method has not been called.

```
learner.my_profile.print_stats()
```

    fit has no data
       epoch has no data
          train has no data
             train_batch has no data
                train_pred has no data
                train_loss has no data
                train_backward has no data
                train_step has no data
                train_zero_grad has no data
          valid has no data
             valid_batch has no data
                valid_pred has no data
                valid_loss has no data


```
learner.fit(1)
```


<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: left;">
      <th>epoch</th>
      <th>train_loss</th>
      <th>valid_loss</th>
      <th>accuracy</th>
      <th>time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>0.655225</td>
      <td>0.184525</td>
      <td>0.941345</td>
      <td>00:14</td>
    </tr>
  </tbody>
</table>


The `print_stats` method now prints the execution counts, max time and avg time (in secs) for each part of the training lifecycle.

```
learner.my_profile.print_stats()
```

    fit  called 1 times. max: 14.542 avg: 14.542
       epoch  called 1 times. max: 14.539 avg: 14.539
          train  called 1 times. max: 12.276 avg: 12.276
             train_batch  called 11 times. max: 1.159 avg: 1.076
                train_pred  called 11 times. max: 0.269 avg: 0.236
                train_loss  called 11 times. max: 0.001 avg: 0.001
                train_backward  called 11 times. max: 0.872 avg: 0.828
                train_step  called 11 times. max: 0.012 avg: 0.008
                train_zero_grad  called 11 times. max: 0.005 avg: 0.003
          valid  called 1 times. max: 2.256 avg: 2.256
             valid_batch  called 11 times. max: 0.208 avg: 0.183
                valid_pred  called 11 times. max: 0.201 avg: 0.180
                valid_loss  called 11 times. max: 0.001 avg: 0.001


The stats can also be collected as a list of tuples where each tuple consists of the lifecycle event name, the level, and the elapsed times. 

```
fit_stats = learner.my_profile.get_stats();fit_stats
```




    [('fit', 0, [14.542369842529297]),
     ('epoch', 1, [14.539028882980347]),
     ('train', 2, [12.275759220123291]),
     ('train_batch',
      3,
      [1.1590299606323242,
       1.1047968864440918,
       1.05731201171875,
       1.0566790103912354,
       1.0275590419769287,
       1.0583367347717285,
       1.0706360340118408,
       1.0878362655639648,
       1.0695040225982666,
       1.0548479557037354,
       1.0869989395141602]),
     ('train_pred',
      4,
      [0.2687697410583496,
       0.2391033172607422,
       0.2244129180908203,
       0.2360670566558838,
       0.2223670482635498,
       0.23363089561462402,
       0.23241806030273438,
       0.2404940128326416,
       0.22686195373535156,
       0.22826123237609863,
       0.24588418006896973]),
     ('train_loss',
      4,
      [0.0010721683502197266,
       0.0006809234619140625,
       0.0006620883941650391,
       0.0007491111755371094,
       0.0006761550903320312,
       0.000698089599609375,
       0.0007200241088867188,
       0.0008070468902587891,
       0.0006639957427978516,
       0.0006880760192871094,
       0.0007140636444091797]),
     ('train_backward',
      4,
      [0.8724572658538818,
       0.8547101020812988,
       0.8222289085388184,
       0.8091421127319336,
       0.7942306995391846,
       0.8135287761688232,
       0.8273820877075195,
       0.8366448879241943,
       0.8316769599914551,
       0.8132097721099854,
       0.8283698558807373]),
     ('train_step',
      4,
      [0.011558294296264648,
       0.0077021121978759766,
       0.0075457096099853516,
       0.007853031158447266,
       0.007728099822998047,
       0.00794076919555664,
       0.007550954818725586,
       0.0073511600494384766,
       0.007617950439453125,
       0.009986162185668945,
       0.00926518440246582]),
     ('train_zero_grad',
      4,
      [0.005139350891113281,
       0.0025839805603027344,
       0.002447843551635742,
       0.0028531551361083984,
       0.002541065216064453,
       0.0025222301483154297,
       0.0025501251220703125,
       0.0025250911712646484,
       0.0026650428771972656,
       0.002687215805053711,
       0.002749919891357422]),
     ('valid', 2, [2.2555930614471436]),
     ('valid_batch',
      3,
      [0.20812106132507324,
       0.18181729316711426,
       0.187255859375,
       0.1778090000152588,
       0.18497300148010254,
       0.18157696723937988,
       0.18445587158203125,
       0.18021106719970703,
       0.1816089153289795,
       0.18120694160461426,
       0.16774797439575195]),
     ('valid_pred',
      4,
      [0.20078110694885254,
       0.1788790225982666,
       0.18420696258544922,
       0.17487597465515137,
       0.18212318420410156,
       0.17869901657104492,
       0.18164587020874023,
       0.17727923393249512,
       0.1787278652191162,
       0.1784052848815918,
       0.16483402252197266]),
     ('valid_loss',
      4,
      [0.001481771469116211,
       0.0005438327789306641,
       0.0005319118499755859,
       0.0005309581756591797,
       0.0005328655242919922,
       0.0005371570587158203,
       0.0005366802215576172,
       0.0005400180816650391,
       0.0005350112915039062,
       0.0005319118499755859,
       0.0005390644073486328])]



The `print_stats` can also print just the stats for one lifecycle event 

```
learner.my_profile.print_stats('train_batch')
```

             train_batch  called 11 times. max: 1.159 avg: 1.076


The `get_stats` can also just collect the stats for one lifecycle event

```
train_batch_stats = learner.my_profile.get_stats('train_batch'); train_batch_stats
```




    ('train_batch',
     3,
     [1.1590299606323242,
      1.1047968864440918,
      1.05731201171875,
      1.0566790103912354,
      1.0275590419769287,
      1.0583367347717285,
      1.0706360340118408,
      1.0878362655639648,
      1.0695040225982666,
      1.0548479557037354,
      1.0869989395141602])



Call the `clear_stats` to clear the stats. You can also pass a lifecycle event to clear a single event

```
learner.my_profile.clear_stats()
```

```
learner.my_profile.print_stats()
```

    fit has no data
       epoch has no data
          train has no data
             train_batch has no data
                train_pred has no data
                train_loss has no data
                train_backward has no data
                train_step has no data
                train_zero_grad has no data
          valid has no data
             valid_batch has no data
                valid_pred has no data
                valid_loss has no data


```
learner.my_profile.print_stats('train')
```

          train has no data


```
learner.fine_tune(1)
```


<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: left;">
      <th>epoch</th>
      <th>train_loss</th>
      <th>valid_loss</th>
      <th>accuracy</th>
      <th>time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>0.283507</td>
      <td>0.242971</td>
      <td>0.896996</td>
      <td>00:14</td>
    </tr>
  </tbody>
</table>



<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: left;">
      <th>epoch</th>
      <th>train_loss</th>
      <th>valid_loss</th>
      <th>accuracy</th>
      <th>time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>0.282430</td>
      <td>0.160309</td>
      <td>0.944206</td>
      <td>00:22</td>
    </tr>
  </tbody>
</table>


```
learner.my_profile.print_stats()
```

    fit  called 2 times. max: 22.964 avg: 18.613
       epoch  called 2 times. max: 22.960 avg: 18.609
          train  called 2 times. max: 20.698 avg: 16.336
             train_batch  called 22 times. max: 2.011 avg: 1.460
                train_pred  called 22 times. max: 0.280 avg: 0.232
                train_loss  called 22 times. max: 0.001 avg: 0.001
                train_backward  called 22 times. max: 1.540 avg: 1.165
                train_step  called 22 times. max: 0.195 avg: 0.057
                train_zero_grad  called 22 times. max: 0.010 avg: 0.005
          valid  called 2 times. max: 2.277 avg: 2.267
             valid_batch  called 22 times. max: 0.217 avg: 0.184
                valid_pred  called 22 times. max: 0.209 avg: 0.181
                valid_loss  called 22 times. max: 0.002 avg: 0.001


##### My Profile Reset Attribute

Setting the `reset` attribute to true on the `my_profile` attribute will cause the stats to be reset each time the `fit` method of the `Learner` is called. So only the accumulated stats for the last call to `fit` (e.g `fine_tune` calls `fit` twice, but setting the `reset` attribute to true will show only the stats for the second `fit` call.
The default value of `reset` is `False`.

```
learner.my_profile.reset = True
```

```
learner.fine_tune(1)
```


<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: left;">
      <th>epoch</th>
      <th>train_loss</th>
      <th>valid_loss</th>
      <th>accuracy</th>
      <th>time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>0.170414</td>
      <td>0.168443</td>
      <td>0.945637</td>
      <td>00:14</td>
    </tr>
  </tbody>
</table>



<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: left;">
      <th>epoch</th>
      <th>train_loss</th>
      <th>valid_loss</th>
      <th>accuracy</th>
      <th>time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>0.146039</td>
      <td>0.141219</td>
      <td>0.951359</td>
      <td>00:22</td>
    </tr>
  </tbody>
</table>


```
learner.my_profile.print_stats()
```

    fit  called 1 times. max: 22.159 avg: 22.159
       epoch  called 1 times. max: 22.154 avg: 22.154
          train  called 1 times. max: 19.886 avg: 19.886
             train_batch  called 11 times. max: 1.939 avg: 1.784
                train_pred  called 11 times. max: 0.264 avg: 0.231
                train_loss  called 11 times. max: 0.001 avg: 0.001
                train_backward  called 11 times. max: 1.483 avg: 1.440
                train_step  called 11 times. max: 0.182 avg: 0.104
                train_zero_grad  called 11 times. max: 0.010 avg: 0.008
          valid  called 1 times. max: 2.263 avg: 2.263
             valid_batch  called 11 times. max: 0.205 avg: 0.184
                valid_pred  called 11 times. max: 0.198 avg: 0.180
                valid_loss  called 11 times. max: 0.002 avg: 0.001


```
learner.my_profile.reset
```




    True


