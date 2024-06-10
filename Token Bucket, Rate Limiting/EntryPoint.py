import time
    
class Limiter:

  def __init__(self, rate, per):
    self.rate = rate
    self.per = per
    self.bucket = rate
    self.last_check = time.time()

  def limit(self, callback_fn):
      current = time.time()
      time_passed = current - self.last_check
      self.last_check = current
           
      bucket = self.bucket + time_passed * (self.rate / self.per)
           
      if (bucket > self.rate):
          self.bucket = self.rate
      if (bucket < 1):
          pass
      else:
          callback_fn()
          self.bucket = bucket - 1
