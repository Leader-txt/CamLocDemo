# CamLocDemo
Demo of monocular localization and calibration.
## Useage
 - **Calibrate**
    - run `calibrate.py` first, a window of camera live will drop out.
    - put the calibrater board under the camera
    - press `c` to capture
    - move the calibrater board around in the view of camera and press `c` if the capture fits will.
    - press `esc` to start calibrating
    - `dist.bin` and `mtx.bin` will be saved in your folder.
 - **Use**
   - edit `Zc` at line 14 of `main.py`, the distance of the target to your camera in **Z** axis
   - edit `f` at line 15 of `main.py`, the focus length of your camera.
   - run `main.py`
   - right click on the window dropped out, real position will be printed on your console.