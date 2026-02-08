<h1 align="center">macro</h1>

<div align="center">
  
  <strong>A collection of macros! Install it once on your RPI Pico 1, use it on most computers! </strong>
</div>


<div align="center">
  
![GitHub License](https://img.shields.io/github/license/numycode/chrome-macro)
![GitHub forks](https://img.shields.io/github/forks/numycode/chrome-macro)
![GitHub Repo stars](https://img.shields.io/github/stars/numycode/chrome-macro)

</div>


# Requirements:
             
  Browser:

    Most (if not all) browsers that support CTRL-T and CTRL-L
  
  Device that will be plugged into the other device:
  
    Has to be a Raspberry Pi Pico 1
    
    Matching version of CircuitPython and Adafruit_HID lib
  

This project was inspired by an old version of Pico-Ducky.


### Update Mode 

To enter Update Mode, first, make sure caps lock is enabled on your keyboard. Then, plug in the macro device. This will stop the macro from starting, making it easy to update the code.py file.

# Info on all the variables: 

### start_delay  

Var Type: Int

Range: 0 - ∞ 

This variable controls the delay before the program starts.

### link

Var Type: str 

Options: Any valid thing you can put in your adress bar.

If you don't set this, this program can't do much! Make sure to set this before running!


### slowdown_level 

Var Type: str 

Options: “off”, “low”, “min”, “max” 

On some low power devices (for example ) the actions for the macro are sent too fast for it to register so this should fix the issue.


## How powerful actually is it?: 

### For vDEV:

Unknown
