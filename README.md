# mflova-i3-setup


### Main i3 use
Main use
| Command/Shortcut  | Description |
| ------------- | ------------- |
|mod + number  |Switch between workspaces or created them |
| mod + arrows |Move between windows in same workspace |
| mod+f |Temporary fullscreen a window |
| mod+shift+q |Close window |
| mod+Shift+c|Reload configuration file |
| mod+Shift+r|Restart i3 inplace preserving layout |
| mod+Shift+e |Exit i3 |
| mod+Shift+Numbers | Moves window between different workspaces|
| mod+Shift+Arrows |Moves window between different workspaces|
| mod+r |Resize mode |
| mod+e |Toggle the orientation of the current window|

Setup certain applications to be opened in a fixed workspaced: 

Launch xprop | grep CLASS and select with the mouse the window. The corresponding output will be written in the i3 config file as:

assign [class="outputapp"] $ws3

If it does not work, you can also move them by the window name with:

for_window [class="name"] move to workspace $ws4

But be careful because every single window with this name will be affected.

### Multiple monitors
Follow this link https://fedoramagazine.org/using-i3-with-multiple-monitors/
Summary to connect another monitor in i3:
-  xrandr to check the name of your current built-in monitor and the new one
-  xrandr --output NEW_MONITOR --auto --right-of YOUR_MONITOR
