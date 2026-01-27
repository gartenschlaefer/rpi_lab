# --
# pico test

import time
import machine


class OnboardvLED():
  """
  on board led
  """

  def __init__(self):
    """
    init
    """

    # led
    self.onboard_led = machine.Pin("LED", machine.Pin.OUT, value=1)


  def loop(self):
    """
    loop
    """

    # loop
    while True:

      # toggle
      self.onboard_led.toggle()
      time.sleep(0.5)