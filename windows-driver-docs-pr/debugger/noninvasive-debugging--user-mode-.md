---
title: Noninvasive Debugging (User Mode)
description: Noninvasive Debugging (User Mode)
ms.assetid: 91f09fb1-9f5e-4081-89b3-78c95eada817
keywords: ["process, debugging noninvasively", "noninvasive debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Noninvasive Debugging (User Mode)


## <span id="ddk_noninvasive_debugging_user_mode__dbg"></span><span id="DDK_NONINVASIVE_DEBUGGING_USER_MODE__DBG"></span>


If a user-mode application is already running, the debugger can debug it *noninvasively*. With noninvasive debugging, you do not have as many debugging actions. However, you can minimize the debugger's interference with the target application. Noninvasive debugging is useful if the target application has stopped responding.

In noninvasive debugging, the debugger does not actually attach to the target application. The debugger suspends all of the target's threads and has access to the target's memory, registers, and other such information. However, the debugger cannot control the target, so commands like [**g (Go)**](g--go-.md) do not work.

If you try to execute commands that are not permitted during noninvasive debugging, you receive an error message that states, "The debugger is not attached, so process execution cannot be monitored."

### <span id="selecting_the_process_to_debug"></span><span id="SELECTING_THE_PROCESS_TO_DEBUG"></span>Selecting the Process to Debug

You can specify the target application by the process ID (PID) or process name.

If you specify the application by name, you should use the complete name of the process, including the file name extension. If two processes have the same name, you must use the process ID instead.

For more information about how to determine the process ID and the process name, see [Finding the Process ID](finding-the-process-id.md).

For information about starting and stopping a noninvasive debugging session, see the following topics:

-   [Debugging a User-Mode Process Using Visual Studio](debugging-a-user-mode-process-using-visual-studio.md)
-   [Debugging a User-Mode Process Using WinDbg](debugging-a-user-mode-process-using-windbg.md)
-   [Debugging a User-Mode Process Using CDB](debugging-a-user-mode-process-using-cdb.md)

### <span id="cdb_command_line"></span><span id="CDB_COMMAND_LINE"></span>CDB Command Line

To noninvasively debug a running process from the CDB command line, specify the -pv option, the -p option, and the process ID, in the following syntax.

**cdb -pv -p** *ProcessID*

Or, to noninvasively debug a running process by specifying the process name, use the following syntax instead.

**cdb -pv -pn** *ProcessName*

There are several other useful command-line options. For more information about the command-line syntax, see [**CDB Command-Line Options**](cdb-command-line-options.md).

### <span id="windbg_command_line"></span><span id="WINDBG_COMMAND_LINE"></span>WinDbg Command Line

To noninvasively debug a running process from the WinDbg command line, specify the -pv option, the -p option, and the process ID, in the following syntax.

**windbg -pv -p** *ProcessID*

Or, to noninvasively debug a running process by specifying the process name, use the following syntax instead.

**windbg -pv -pn** *ProcessName*

There are several other useful command-line options. For more information about the command-line syntax, see [**WinDbg Command-Line Options**](windbg-command-line-options.md).

### <span id="windbg_menu"></span><span id="WINDBG_MENU"></span>WinDbg Menu

When WinDbg is in dormant mode, you can noninvasively debug a running process by clicking Attach to a Process on the File menu or by pressing F6.

When the Attach to Process dialog box appears, select the Noninvasive check box. Then, select the line that contains the process ID and name that you want. (You can also enter the process ID in the Process ID box.) Finally, click OK.

### <span id="debugger_command_window"></span><span id="DEBUGGER_COMMAND_WINDOW"></span>Debugger Command Window

If the debugger is already active, you can noninvasively debug a running process by using the [**.attach -v (Attach to Process)**](-attach--attach-to-process-.md) command in the [Debugger Command window](the-debugger-command-window.md).

You can use the .attach command if the debugger is already debugging one or more processes invasively. You can use this command in CDB if it is dormant, but not in a dormant WinDbg.

If the .attach -v command is successful, the debugger debugs the specified process the next time that the debugger issues an execution command. Because execution is not permitted during noninvasive debugging, the debugger cannot noninvasively debug more than one process at a time. This restriction also means that using the .attach -v command might make an existing invasive debugging session less useful.

### <span id="beginning_the_debugging_session"></span><span id="BEGINNING_THE_DEBUGGING_SESSION"></span>Beginning the Debugging Session

For more information about how to begin a debugging session, see [Debugger Operation](debugger-operation-win8.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Noninvasive%20Debugging%20%28User%20Mode%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




