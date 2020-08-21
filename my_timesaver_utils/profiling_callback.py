# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/02_profiling_callback.ipynb (unless otherwise specified).

__all__ = ['FASTAI_AVAILABLE', 'MyProfileCallback']

# Cell
from .profiling import *

# Cell
import warnings
FASTAI_AVAILABLE = True
try:
    from fastai.callback.core import Callback
    from fastai.learner import Learner
    from fastcore.foundation import patch
except ImportError as e:
    FASTAI_AVAILABLE = False
    warnings.warn('fastai package not installed, callback simulated')

# Cell
if not FASTAI_AVAILABLE:
    class Callback:
        pass
    class Learner:
        pass
    def patch(fn, *args,**kwargs):
        return fn

# Internal Cell
def _print_stat(func_name, level, data, indent_per_level=3):
    indent = ' ' * indent_per_level * level
    if data is None:
        print(f'{indent}{func_name} has no data')
        return
    max_time = max(data)
    avg_time = sum(data) / len(data)
    print(f'{indent}{func_name}  called {len(data)} times. max: {max_time:.3f} avg: {avg_time:.3f}')

# Cell
class MyProfileCallback(Callback):
    'Callback to profile training lifecycle event performance'
    ordered_callbacks = (
        ('fit',0),
        ('epoch',1),
        ('train',2),
        ('train_batch',3),
        ('train_pred',4),
        ('train_loss',4),
        ('train_backward',4),
        ('train_step',4),
        ('train_zero_grad',4),
        ('valid',2),
        ('valid_batch',3),
        ('valid_pred',4),
        ('valid_loss',4)
    )
    def __init__(self, reset=False):
        self._reset = reset

    def before_fit(self):
        if self._reset:
            self.clear_stats()
        start_record('fit')

    def before_epoch(self):
        start_record('epoch')

    def before_train(self):
        start_record('train')

    def before_batch(self):
        if self.learn.training:
            start_record('train_batch')
            start_record('train_pred')
        else:
            start_record('valid_batch')
            start_record('valid_pred')

    def after_pred(self):
        if self.learn.training:
            end_record('train_pred')
            if len(self.learn.yb) > 0:
                start_record('train_loss')
        else:
            end_record('valid_pred')
            if len(self.learn.yb) > 0:
                start_record('valid_loss')

    def after_loss(self):
        if self.learn.training:
            end_record('train_loss')
            start_record('train_backward')
        else:
            end_record('valid_loss')
            # no start train_backward because
            # valid doesnt execute backward

    def after_backward(self):
        end_record('train_backward')
        start_record('train_step')

    def after_step(self):
        end_record('train_step')
        start_record('train_zero_grad')

    def after_cancel_batch(self):
        if self.learn.training:
            if is_recording('train_pred'):
                end_record('train_pred')

            if is_recording('train_loss'):
                end_record('train_loss')

            if is_recording('train_backward'):
                end_record('train_backward')

            if is_recording('train_step'):
                end_record('train_step')

            if is_recording('train_zero_grad'):
                end_record('train_zero_grad')
        else:
            if is_recording('valid_pred'):
                end_record('valid_pred')

            if is_recording('valid_loss'):
                end_record('valid_loss')

            # no more steps after valid_loss

    def after_batch(self):
        if self.learn.training:
            if is_recording('train_zero_grad'):
                end_record('train_zero_grad')
            end_record('train_batch')
        else:
            end_record('valid_batch')

    def after_train(self):
        end_record('train')

    def after_cancel_train(self):
        if is_recording('train_pred'):
            end_record('train_pred')

        if is_recording('train_loss'):
            end_record('train_loss')

        if is_recording('train_backward'):
            end_record('train_backward')

        if is_recording('train_step'):
            end_record('train_step')

        if is_recording('train_zero_grad'):
            end_record('train_zero_grad')

    def before_validate(self):
        start_record('valid')

    def after_cancel_validate(self):
        if is_recording('valid_pred'):
            end_record('valid_pred')
        if is_recording('valid_loss'):
            end_record('valid_loss')

    def after_validate(self):
        end_record('valid')

    def after_epoch(self):
        end_record('epoch')

    def after_cancel_fit(self):
        if is_recording('epoch'):
            end_record('epoch')

        if is_recording('train'):
            end_record('train')

        if is_recording('train_batch'):
            end_record('train_batch')

        if is_recording('train_pred'):
            end_record('train_pred')

        if is_recording('train_loss'):
            end_record('train_loss')

        if is_recording('train_backward'):
            end_record('train_backward')

        if is_recording('train_step'):
            end_record('train_step')

        if is_recording('train_zero_grad'):
            end_record('train_zero_grad')

        if is_recording('valid'):
            end_record('valid')

        if is_recording('valid_batch'):
            end_record('valid_batch')

        if is_recording('valid_pred'):
            end_record('valid_pred')

        if is_recording('valid_loss'):
            end_record('valid_loss')

    def after_fit(self):
        end_record('fit')

    def print_stats(self, fname=None, indent_per_level=3):
        if fname is not None:
            matches = [(func_name,level) for (func_name,level) in self.ordered_callbacks if func_name == fname]
            if len(matches) > 0:
                func_name, level = matches[0]
                data = get_prof_data(func_name)
                _print_stat(func_name, level, data, indent_per_level=indent_per_level)
            else:
                _print_stat(func_name, 0, None, indent_per_level=indent_per_level)
            return

        for func_name,level in self.ordered_callbacks:
            data = get_prof_data(func_name)
            _print_stat(func_name, level, data, indent_per_level=indent_per_level)

    def clear_stats(self, fname=None):
        if fname is not None:
            clear_prof_data(func_name)
            return
        for func_name,_ in self.ordered_callbacks:
            clear_prof_data(func_name)

    def get_stats(self,fname=None):
        if fname is not None:
            matches = [(func_name,level) for (func_name,level) in self.ordered_callbacks if func_name == fname]
            if len(matches) > 0:
                func_name, level = matches[0]
                data = get_prof_data(func_name)
            else:
                func_name = fname
                level = 0
                data = []
            return (func_name, level, data)
        res = []
        for func_name,level in self.ordered_callbacks:
            data = get_prof_data(func_name)
            res.append((func_name,level,data))
        return res

    @property
    def reset(self):
        return self._reset

    @reset.setter
    def reset(self,v):
        self._reset = v

# Cell
@patch
def to_my_profile(self:Learner, reset=False):
    'Add my_profile callback to learner'
    cb = MyProfileCallback(reset=reset)
    if not getattr(self, cb.name, None):
        self.add_cb(cb)
    else:
        self.my_profile.reset = reset
    return self