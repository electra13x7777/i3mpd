# i3mpd
Enhanced fork of spotify.py

### Controls
* LeftMouseButton : prev
* CenterMouseButton : play/pause
* LeftMouseButton : next

### Features
* Reformats metadata to be compliant with what can be outputed in i3blocks
* Displays song controls `❲ ⏮  (⏵) ⏭ ❳` dynamically depending on playback state
* Displays Current Song *(Artist : Album - Song)*
* Displays Song Length *(MM:SS)*

### Status Bar Support
* i3blocks
* Polybar

### Music Player Support
* *Spotify*

### i3blocks
```
[i3mpd]
label=
command= python /lib64/i3blocks/i3mpd.py
color=#21b089
interval=1
```

### Polybar
```
[module/i3mpd]
type = custom/script
exec = ~/i3mpd.sh
interval = 1
```

### Output
* **Artist : Album - Song (Mins:Secs) ❲Controls❳**
`Talking Heads : Remain In Light - The Great Curve (6:28) ❲ ⏮  (⏸) ⏭ ❳`
