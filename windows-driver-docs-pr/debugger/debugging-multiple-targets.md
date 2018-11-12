---
title: Debugging Multiple Targets
description: Debugging Multiple Targets
ms.assetid: 93eb6b49-e7a0-4f30-ade8-94019a1adf43
keywords: ["multiple targets", "system", "system, overview"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Debugging Multiple Targets


## <span id="ddk_debugging_multiple_targets_dbg"></span><span id="DDK_DEBUGGING_MULTIPLE_TARGETS_DBG"></span>


You can debug multiple dump files or live user-mode applications at the same time. Each target contains one or more processes, and each process contains one or more threads.

These targets are also grouped into *systems*. Systems are sets of targets that are grouped together for easy identification and manipulation. Systems are defined as follows:

-   Each kernel-mode or user-mode dump file is a separate system.

-   When you are debugging live user-mode applications on different computers (by using a [process server](process-servers--user-mode-.md), such as Dbgsrv), each application is a separate system.

-   When you are debugging live user-mode applications on the local computer, the applications are combined into a single system.

The *current* or *active* system is the system that you are currently debugging.

### <span id="acquiring_multiple_targets"></span><span id="ACQUIRING_MULTIPLE_TARGETS"></span>Acquiring Multiple Targets

The first target is acquired in the usual manner.

You can debug additional live user-mode applications by using the [**.attach (Attach to Process)**](-attach--attach-to-process-.md) or [**.create (Create Process)**](-create--create-process-.md) command, followed by the **g (Go)** command.

You can debug additional dump files by using the [**.opendump (Open Dump File)**](-opendump--open-dump-file-.md) command, followed by the **g (Go)** command. You can also open multiple dump files when the debugger is started. To open multiple dump files, include multiple **-z** switches in the command, each followed by a different file name.

You can use the preceding commands even if the processes are on different systems. You must start a process server on each system and then use the -premote parameter with **.attach** or **.create** to identify the proper process server. If you use the **.attach** or **.create** command again without specifying the -premote parameter, the debugger attaches to, or creates, a process on the current system.

### <span id="manipulating_systems_and_targets"></span><span id="MANIPULATING_SYSTEMS_AND_TARGETS"></span>Manipulating Systems and Targets

When debugging begins, the current system is the one that the debugger most recently attached to. If an exception occurs, the current system switches to the system that this exception occurred on.

To close one target and continue to debug the other targets, use the [**.kill (Kill Process)**](-kill--kill-process-.md) command. You can use the [**.detach (Detach from Process)**](-detach--detach-from-process-.md) command or WinDbg's [Debug | Detach Debuggee](debug---detach-debuggee.md) menu command instead. These commands detach the debugger from the target but leave the target running.

To control the debugging of multiple systems, you can use the following methods:

-   The [**|| (System Status)**](----system-status-.md) command displays information about one or more systems

-   The [**||s (Set Current System)**](--s--set-current-system-.md) command enables you to select the current system

-   (WinDbg only) The [Processes and Threads window](processes-and-threads-window.md) enables you display or select systems, processes, and threads

By using these commands to select the current system, and by using the standard commands to [select the current process and thread](controlling-processes-and-threads.md), you can determine the context of commands that display memory and registers.

However, you cannot separate execution of these processes. The [**g (Go)**](g--go-.md) command always causes all targets to execute together.

**Note**   There are complications, when you debug live targets and dump targets together, because commands behave differently for each type of debugging. For example, if you use the **g (Go)** command when the current system is a dump file, the debugger begins executing, but you cannot break back into the debugger, because the break command is not recognized as valid for dump file debugging.


Example
-------

To  work with three dump files at the same time, you can use the -z option to load them when WinDbg is started. 

```console
windbg -z c:\notepad.dmp -z c:\paint.dmp -z c:\calc.dmp
```

For more infomation see [WinDbg Command-Line Options](windbg-command-line-options.md). You can also use the [.opendump](-opendump--open-dump-file-.md)  and the [**g (Go)**](g--go-.md) commands to load additional dump files in the debugger. 

Use the  [|| (System Status)](----system-status-.md) command to confirm that all three systems are present.

```dbgcmd
||0:0:007> ||
.  0 User mini dump: c:\notepad.dmp
   1 User mini dump: C:\paint.dmp
   2 User mini dump: c:\calc.dmp
```

Use the [**g (Go)**](g--go-.md) command to complete loading of the dump files. 
```dbgcmd
||0:0:007> g

************* Path validation summary **************
Response                         Time (ms)     Location
Deferred                                       srv*
Symbol search path is: srv*
Executable search path is: 
Windows 10 Version 15063 MP (4 procs) Free x64
Product: WinNt, suite: SingleUserTS
15063.0.amd64fre.rs2_release.170317-1834
Machine Name:
Debug session time: Fri Jun  9 15:52:04.000 2017 (UTC - 7:00)
System Uptime: not available
Process Uptime: 0 days 0:03:44.000
...............................................................
This dump file has a breakpoint exception stored in it.
The stored exception information can be accessed via .ecxr.
ntdll!DbgBreakPoint:
00007ff8`aada8d70 cc              int     3
```

Then use the  [||s (Set Current System)](--s--set-current-system-.md) command to set the current system to system 1 and then display the current system.

```dbgcmd
||1:1:017> ||1s
||1:1:017> ||
   0 User mini dump: c:\notepad.dmp
.  1 User mini dump: c:\paint.dmp
   2 User mini dump: c:\calc.dmp
```

You can use the [.detach](-detach--detach-from-process-.md) command when you are done looking at the current dump file.

```dbgcmd
||1:1:017> .detach
ntdll!DbgBreakPoint:
00007ff8`aada8d70 cc              int     3
Detached
||0:0:007> ||
.  0 User mini dump: c:\notepad.dmp
   2 User mini dump: c:\calc.dmp
```

Resources
---------

For addtional information on debugging see the following resources.

**Books**

- Advanced Windows Debugging by Mario Hewardt and Daniel Pravat

- Inside Windows Debugging: A Practical Guide to Debugging and Tracing Strategies in Windows by Tarik Soulami

- Windows Internals by Pavel Yosifovich, Alex Ionescu, Mark E. Russinovich and David A. Solomon 

**Video**

The Defrag Tools Show WinDbg Episodes 13-29 [https://channel9.msdn.com/Shows/Defrag-Tools](https://channel9.msdn.com/Shows/Defrag-Tools) 










