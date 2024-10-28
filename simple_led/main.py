# --
# pico test

from onboard_led import OnboardvLED


if __name__ == "__main__":
  """
  main
  """

  # create on board led
  led = OnboardvLED()

  # loop
  led.loop()