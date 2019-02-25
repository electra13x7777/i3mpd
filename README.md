# i3mpd
Enhanced fork of spotify.py

### Controls
* LeftMouseButton : prev
* CenterMouseButton : play/pause
* LeftMouseButton : next

### Features
* Reformats metadata to be complient with what can be outputed in i3blocks
* Displays song controls `❲ ⏮  (⏵) ⏭ ❳` dynamically depending on playback state
* Displays Current Song (Artist : Album - Song)

### Music Player Support
* *Spotify*

### Block
```
[i3mpd]
label=
command= python /lib64/i3blocks/i3mpd.py
color=#21b089
interval=1
```
