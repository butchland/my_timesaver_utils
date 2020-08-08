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
    Execution time max: 1.005, average: 1.003


Get your profile data (e.g. good for graphing)

```
times = get_prof_data('test_func'); times
```




    [1.0051040649414062,
     1.005079746246338,
     1.0044150352478027,
     1.0005950927734375,
     1.0044729709625244,
     1.0028409957885742,
     1.0004441738128662,
     1.0036230087280273,
     1.0050239562988281,
     1.0049309730529785]



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

    Function test_func called 10 times.
    Execution time max: 1.005, average: 1.004
    Function wachacha called 3 times.
    Execution time max: 1.005, average: 1.003
    Function my_sleep called 10 times.
    Execution time max: 1.005, average: 1.002
    Function sleep called 5 times.
    Execution time max: 4.005, average: 2.003
    Function maluman called 3 times.
    Execution time max: 1.005, average: 1.002


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

Calling `clear_prof_data` for a function will clear out the data for that function

```
clear_prof_data('sleep')
print_prof_data()
```

    Function test_func called 10 times.
    Execution time max: 1.005, average: 1.004
    Function wachacha called 3 times.
    Execution time max: 1.005, average: 1.003
    Function my_sleep called 10 times.
    Execution time max: 1.005, average: 1.002
    Function maluman called 3 times.
    Execution time max: 1.005, average: 1.002


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

    Function test_func called 10 times.
    Execution time max: 1.005, average: 1.004
    Function wachacha called 3 times.
    Execution time max: 1.005, average: 1.003
    Function my_sleep called 10 times.
    Execution time max: 1.005, average: 1.002
    Function sleep called 5 times.
    Execution time max: 4.005, average: 2.003
    Function maluman called 3 times.
    Execution time max: 1.005, average: 1.002


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
from fastai2.vision.all import *
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




    <fastai2.learner.Learner at 0x130955f90>



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
    
    Optimizer used: <function Adam at 0x12fe710e0>
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
      <td>0.646651</td>
      <td>0.224889</td>
      <td>0.909871</td>
      <td>00:14</td>
    </tr>
  </tbody>
</table>


The `print_stats` method now prints the execution counts, max time and avg time (in secs) for each part of the training lifecycle.

```
learner.my_profile.print_stats()
```

    fit  called 1 times. max: 14.688 avg: 14.688
       epoch  called 1 times. max: 14.678 avg: 14.678
          train  called 1 times. max: 12.425 avg: 12.425
             train_batch  called 11 times. max: 1.170 avg: 1.081
                train_pred  called 11 times. max: 0.304 avg: 0.236
                train_loss  called 11 times. max: 0.001 avg: 0.001
                train_backward  called 11 times. max: 0.848 avg: 0.834
                train_step  called 11 times. max: 0.011 avg: 0.008
                train_zero_grad  called 11 times. max: 0.006 avg: 0.003
          valid  called 1 times. max: 2.245 avg: 2.245
             valid_batch  called 11 times. max: 0.195 avg: 0.181
                valid_pred  called 11 times. max: 0.188 avg: 0.178
                valid_loss  called 11 times. max: 0.001 avg: 0.001


The stats can also be collected as a list of tuples where each tuple consists of the lifecycle event name, the level, and the elapsed times. 

```
fit_stats = learner.my_profile.get_stats();fit_stats
```




    [('fit', 0, [14.687530994415283]),
     ('epoch', 1, [14.67847228050232]),
     ('train', 2, [12.425010204315186]),
     ('train_batch',
      3,
      [1.1697580814361572,
       1.0837702751159668,
       1.0729010105133057,
       1.0813207626342773,
       1.0650250911712646,
       1.0707719326019287,
       1.087137222290039,
       1.0528171062469482,
       1.0657010078430176,
       1.0718588829040527,
       1.0731070041656494]),
     ('train_pred',
      4,
      [0.3040790557861328,
       0.23769092559814453,
       0.2236030101776123,
       0.23487424850463867,
       0.22310113906860352,
       0.22788310050964355,
       0.23348093032836914,
       0.23145484924316406,
       0.21995902061462402,
       0.22831082344055176,
       0.2304689884185791]),
     ('train_loss',
      4,
      [0.0010890960693359375,
       0.0006949901580810547,
       0.0007219314575195312,
       0.0006780624389648438,
       0.0010340213775634766,
       0.0007722377777099609,
       0.0006699562072753906,
       0.0006821155548095703,
       0.0007212162017822266,
       0.0006709098815917969,
       0.0006799697875976562]),
     ('train_backward',
      4,
      [0.8481080532073975,
       0.8349168300628662,
       0.8384270668029785,
       0.8354089260101318,
       0.8305647373199463,
       0.8319101333618164,
       0.8415019512176514,
       0.8106880187988281,
       0.8350062370300293,
       0.8329300880432129,
       0.8316891193389893]),
     ('train_step',
      4,
      [0.01085805892944336,
       0.007528781890869141,
       0.007549762725830078,
       0.007534980773925781,
       0.007409095764160156,
       0.007349967956542969,
       0.009161949157714844,
       0.007405996322631836,
       0.007421016693115234,
       0.007613182067871094,
       0.007512092590332031]),
     ('train_zero_grad',
      4,
      [0.005597829818725586,
       0.0029211044311523438,
       0.002583026885986328,
       0.002810239791870117,
       0.002899169921875,
       0.0028409957885742188,
       0.0023050308227539062,
       0.0025720596313476562,
       0.0025682449340820312,
       0.0023169517517089844,
       0.0027413368225097656]),
     ('valid', 2, [2.2446630001068115]),
     ('valid_batch',
      3,
      [0.19499421119689941,
       0.17691898345947266,
       0.18032121658325195,
       0.17589092254638672,
       0.17492890357971191,
       0.17957305908203125,
       0.1777338981628418,
       0.18741679191589355,
       0.17940211296081543,
       0.1895129680633545,
       0.17221283912658691]),
     ('valid_pred',
      4,
      [0.18814992904663086,
       0.17379498481750488,
       0.17746996879577637,
       0.17304277420043945,
       0.17206573486328125,
       0.17669415473937988,
       0.17478203773498535,
       0.18450498580932617,
       0.17637085914611816,
       0.1866168975830078,
       0.16930532455444336]),
     ('valid_loss',
      4,
      [0.0013051033020019531,
       0.0005512237548828125,
       0.0005471706390380859,
       0.0005497932434082031,
       0.0005450248718261719,
       0.0005440711975097656,
       0.0005459785461425781,
       0.0005478858947753906,
       0.0005469322204589844,
       0.0005431175231933594,
       0.0005438327789306641])]



The `print_stats` can also print just the stats for one lifecycle event 

```
learner.my_profile.print_stats('train_batch')
```

             train_batch  called 11 times. max: 1.170 avg: 1.081


The `get_stats` can also just collect the stats for one lifecycle event

```
train_batch_stats = learner.my_profile.get_stats('train_batch'); train_batch_stats
```




    ('train_batch',
     3,
     [1.1697580814361572,
      1.0837702751159668,
      1.0729010105133057,
      1.0813207626342773,
      1.0650250911712646,
      1.0707719326019287,
      1.087137222290039,
      1.0528171062469482,
      1.0657010078430176,
      1.0718588829040527,
      1.0731070041656494])



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
      <td>0.370858</td>
      <td>0.235521</td>
      <td>0.912732</td>
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
      <td>0.231076</td>
      <td>0.167055</td>
      <td>0.939914</td>
      <td>00:22</td>
    </tr>
  </tbody>
</table>


```
learner.my_profile.print_stats()
```

    fit  called 2 times. max: 22.034 avg: 18.256
       epoch  called 2 times. max: 22.030 avg: 18.252
          train  called 2 times. max: 19.765 avg: 16.002
             train_batch  called 22 times. max: 2.025 avg: 1.429
                train_pred  called 22 times. max: 0.302 avg: 0.232
                train_loss  called 22 times. max: 0.001 avg: 0.001
                train_backward  called 22 times. max: 1.520 avg: 1.132
                train_step  called 22 times. max: 0.222 avg: 0.058
                train_zero_grad  called 22 times. max: 0.011 avg: 0.005
          valid  called 2 times. max: 2.258 avg: 2.244
             valid_batch  called 22 times. max: 0.211 avg: 0.180
                valid_pred  called 22 times. max: 0.204 avg: 0.177
                valid_loss  called 22 times. max: 0.002 avg: 0.001


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
      <td>0.158287</td>
      <td>0.196981</td>
      <td>0.929900</td>
      <td>00:16</td>
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
      <td>0.090954</td>
      <td>0.162717</td>
      <td>0.944206</td>
      <td>00:23</td>
    </tr>
  </tbody>
</table>


```
learner.my_profile.print_stats()
```

    fit  called 1 times. max: 23.094 avg: 23.094
       epoch  called 1 times. max: 23.091 avg: 23.091
          train  called 1 times. max: 20.766 avg: 20.766
             train_batch  called 11 times. max: 2.104 avg: 1.863
                train_pred  called 11 times. max: 0.265 avg: 0.231
                train_loss  called 11 times. max: 0.001 avg: 0.001
                train_backward  called 11 times. max: 1.648 avg: 1.519
                train_step  called 11 times. max: 0.180 avg: 0.104
                train_zero_grad  called 11 times. max: 0.011 avg: 0.008
          valid  called 1 times. max: 2.318 avg: 2.318
             valid_batch  called 11 times. max: 0.212 avg: 0.187
                valid_pred  called 11 times. max: 0.209 avg: 0.183
                valid_loss  called 11 times. max: 0.002 avg: 0.001


```
learner.my_profile.reset
```




    True


