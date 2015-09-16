# AB-Gcode
Transform ABC files into G-code. (ABC music standard)

AB-Gcode will translate your ABC file to G-code to allow it to play music on your CNC machine/3D printer. This uses the m300 command (i.e. you will need a speaker). It does this by converting the notation to frequency/duration and appending the proper G-code.

Example:
  ABC Notation:
    T:Bach
    Q:3/8 120

    dff cee|
  PYTHON MAGIC!
  
  G-code:
    M117 Bach
    M300 293 7500
    M300 349 7500
    M300 349 7500
    M300 261 7500
    M300 329 7500
    M300 329 7500

This program is NOT currently ready for use. 

If you run a file through it, it will translate the notes to a frequency (rounded), but it cannot yet determine the duration of the sound. The program is/will be written Python 2.7, it is intended to be cross-platform, however it has yet to be tested on any OS other than Windows 8.
