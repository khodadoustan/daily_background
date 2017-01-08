# Auto updates your desktop wallpaper daily
Simple script that changes your wallpaper to bings daily image.
Only works on ubuntu.

### Setup
```
pip install -r requirements.txt
```
Add the script to your crontab.
```
0 0 * * * /full_path/main.py
```
Add script to be ran on startup
```
vim /etc/rc.local
/full_path/main.py
```
## Todos:
Find a better API to hit other than bing, it only updates
daily.
