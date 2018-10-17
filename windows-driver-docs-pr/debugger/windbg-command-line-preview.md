---
title: WinDbg Preview - Command line startup options
description: This section covers the command line startup options for the WinDbg Preview debugger.
ms.author: domars
ms.date: 10/12/2018
ms.localizationpriority: medium
---

> [!NOTE]
> The information in this topic is preliminary. Updated information will be provided in a later release of the documentation. 
>

# WinDbg Preview - Command line startup options

## Starting WinDbg Preview

After WinDbg Preview is installed, WinDbgX.exe is available to run from any directory location. 


## Command line startup options

```dbgsyntax
WinDbgX [options]
```

This following tables summarizes the available command line options.

**General Options**

Option | Description
|------ | -----------|
c | Executes a command line after the debugger is attached. 
v | Enables verbose output in the debugger.
T | Sets the window title.
? | Displays a summary of commands available.

**Kernel Options**

Option | Description
|------ | -----------|
k | Starts a kernel debugging session. 
kqm | Starts KD in quiet mode. 
kl | Starts a kernel debugging session on the same machine as the debugger. 
kx | Starts a kernel debugging session using an EXDI driver.
d | After a reboot, the debugger will break into the target computer as soon as a kernel module is loaded.
 

**User Mode Options**

Option | Description
|------ | -----------|
o | Debugs all processes launched by the target application (child processes). 
g | Ignores the initial breakpoint in target application. 
G |Ignores the final breakpoint in target application. 
pv | Specifies that the debugger should attach to the target process noninvasively.
hd | Specifies that the debug heap should not be used.
cimp | Specifies that any processes created will use an implicit command-line set by the server instead of a user-given command-line string from the client. 


**Target Options**

Option | Description
|------ | -----------|
remote | Connects to a debugging server that is already running
premote | Connects to a process server (dbgsrv) that is already running. 
p| Specifies the decimal process ID to be debugged.
tid | Specifies the thread ID of a thread to be resumed when the debugging session is started. 
psn | Specifies the name of the service contained in the process to be debugged. This is used to debug a process that is already running.
pn | Specifies the name of the process to be debugged.
z | Specifies the name of a crash dump file to debug. 
openPrivateDumpByHandle *Handle* | Specifies the handle of a crash dump file to debug.


**Symbol Options**

Option | Description
|------ | -----------|
y | Specifies the symbol path to use
n | Enables verbose output from symbol handler.
i | Sets the image search path to use.
sdce | Causes the debugger to display 'File access error' messages during symbol load. 
ses | Causes the debugger to perform a strict evaluation of all symbol files and ignore any questionable symbols.
sicv |Causes the symbol handler to ignore the CV record
sins |Causes the debugger to ignore the symbol path and executable image path environment variables.
snc | Causes the debugger to turn off C++ translation.
snul | Disables automatic symbol loading for unqualified names.
sup | Causes the symbol handler to search the public symbol table during every symbol search
sflags| Sets all the symbol handler options at once

For general information on the startup parameters, see [WinDbg Command-Line Options](windbg-command-line-options.md).


You can use /? to list the supported command line options.

![Screen shot of command line help output listing about 50 options](images/windbgx-start-up-options.png)



---

## See Also

[Debugging Using WinDbg Preview](debugging-using-windbg-preview.md)

 





