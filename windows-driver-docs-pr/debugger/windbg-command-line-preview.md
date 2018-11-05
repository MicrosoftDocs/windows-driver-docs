---
title: WinDbg Preview - Command line startup options
description: This section covers the command line startup options for the WinDbg Preview debugger.
ms.author: domars
ms.date: 10/12/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# WinDbg Preview - Command line startup options

## Starting WinDbg Preview

After WinDbg Preview is installed, WinDbgX.exe is available to run from any directory location. 


## Command line startup options

```dbgsyntax
WinDbgX [options]
```

This following tables summarizes the available command line options.

**General Options**


|     Option      |                                                                          Description                                                                          |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -c  *"command"* | Executes a command line after the debugger is attached. This command must be enclosed in quotation marks. Multiple commands can be separated with semicolons. |
|       -v        |                                                            Enables verbose output in the debugger.                                                            |
|   -T *Title*    |                                                                    Sets the window title.                                                                     |
| logo *LogFile*  |                                Log Open. Begins logging information to a log file. If the file exists, it will be overwritten.                                |
| loga *LogFile*  |                               Log Append. Begins logging information to a log file. If the file exists, it will be appended to.                               |
| e *EventHandle* |                                         Signals the event with the given handle after the next exception in a target.                                         |
|       -?        |                                                           Displays a summary of commands available.                                                           |

**Kernel Options**


|       Option       |                                                                      Description                                                                      |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| -k \[ConnectType\] | Starts a kernel debugging session.  If **-k** is used without any *ConnectType* options following it, it must be the final entry on the command line. |
|        -kqm        |                                                               Starts KD in quiet mode.                                                                |
|        -kl         |                                        Starts a kernel debugging session on the same machine as the debugger.                                         |
| -kx *ExdiOptions*  |                                                Starts a kernel debugging session using an EXDI driver.                                                |
|         -d         |                        After a reboot, the debugger will break into the target computer as soon as a kernel module is loaded.                         |

**User Mode Options**

Option | Description
|------ | -----------|
-o | Debugs all processes launched by the target application (child processes). 
-g | Ignores the initial breakpoint in target application. 
-G |Ignores the final breakpoint in target application. 
-pv | Specifies that the debugger should attach to the target process noninvasively.
-hd | Specifies that the debug heap should not be used.
-cimp | Specifies that any processes created will use an implicit command-line set by the server instead of a user-given command-line string from the client. 


**Target Options**


|              Option              |                                                                                                                                  Description                                                                                                                                  |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|    -remote *ClientTransport*     | Connects to a debugging server that is already running. For an explanation of the possible *ClientTransport* values, see [Activating a Debugging Client](activating-a-debugging-client.md). When this parameter is used, it must be the first parameters on the command line. |
|    -server *ServerTransport*     |                                    Creates a debugging server that can be accessed by other debuggers. For an explanation of the possible *ServerTransport* values, see [Activating a Debugging Server](activating-a-debugging-server.md).                                    |
| -premote *SmartClientTransport*  |                               Creates a smart client, and connects to a process server that is already running. For an explanation of the possible SmartClientTransport values, see [Activating a Smart Client](activating-a-smart-client.md).                                |
|             -p *PID*             |                                                                                                               Specifies the decimal process ID to be debugged.                                                                                                                |
|            -tid *TID*            |                                                                                           Specifies the thread ID of a thread to be resumed when the debugging session is started.                                                                                            |
|        -psn *ServiceName*        |                                                                      Specifies the name of the service contained in the process to be debugged. This is used to debug a process that is already running.                                                                      |
|        -pn *ProcessName*         |                                                                                                               Specifies the name of the process to be debugged.                                                                                                               |
|          -z *DumpFile*           |                                                                    Specifies the name of a crash dump file to debug. If the path and file name contain spaces, this must be surrounded by quotation marks.                                                                    |
| openPrivateDumpByHandle *Handle* |                                                                                              *Microsoft internal use only*. Specifies the handle of a crash dump file to debug.                                                                                               |
|    -debugArch x86 -or- amd64     |                                                                                                 Override the autodetect behavior and set the target bitness for the debugger.                                                                                                 |

**Symbol Options**

Option | Description
|------ | -----------|
-y *SymbolPath* | Specifies the symbol path to use. Separate multiple paths with a semicolon (**;**). If the path contains spaces, it should be enclosed in quotation marks. For details, and for other ways to change this path, see [Symbol Path](symbol-path.md).
-n | Noisy symbol load. Enables verbose output from symbol handler.
-i *ImagePath* | Sets the image search path to use.
-sdce | Causes the debugger to display 'File access error' messages during symbol load. 
-ses | Causes the debugger to perform a strict evaluation of all symbol files and ignore any questionable symbols.
-sicv |Causes the symbol handler to ignore the CV record
-sins |Causes the debugger to ignore the symbol path and executable image path environment variables.
-snc | Causes the debugger to turn off C++ translation.
-snul | Disables automatic symbol loading for unqualified names.
-sup | Causes the symbol handler to search the public symbol table during every symbol search
-sflags| Sets all the symbol handler options at once.

For general information on the startup parameters, see [WinDbg Command-Line Options](windbg-command-line-options.md).

You can use /? to list the supported command line options.

![Screen shot of command line help output listing about 50 options](images/windbgx-start-up-options.png)



---

## See Also

[Debugging Using WinDbg Preview](debugging-using-windbg-preview.md)







