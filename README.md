<p align="center"><img src="pic/screenshot.gif" width="500px"></p>

<h1 align="center">
    <strong>Time Limit</strong>
</h1>
<h3 align="center">
    <p>Limit computer usage(screentime) in Python.</p>
</h3>

<hr>

### Contents
- [Usage](#usage)
- [Step by step](#step-by-step)

<hr>

### Usage

This small pgrogram is designed to limit daily computer usage or screen time.
Current version is limiting daily time in 180 minutes or 3 hours.
When time limit runs out then Computer shuts down.
Program keeps track daily and resets when date changes.
Computer can be restarted when counter is on. On startup time tracking starts wehre it was left on last run.

<hr>

### Step by step

Meant to use on hidden/stealth mode when computer starts.

1. First of all allow this program on Windows Defender and antivirus programs. Current application could be taken as a threat.
2. Set the program propertie as hidden.
3. Press Win+R
4. Type 

```
shell:startup
```

5. On opened windows create new text file and add following code.
In this example our program location is 'C:\time\time.exe'.
If you save it to somewhere else then edit code accordingly.

```
Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "C:\Batch Files\syncfiles.bat" & Chr(34), 0
Set WshShell = Nothing
```
6. Save the file and close Notepad.
7. Rename the text file to VB Script. For example 'time.vb'. Thats it. Next time you restart your computer our time counter will start invisibly.
