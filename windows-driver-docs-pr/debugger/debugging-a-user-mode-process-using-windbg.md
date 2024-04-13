---
title: Debugging a User-Mode Process Using WinDbg
description: You can use WinDbg Classic to attach to a running process or to spawn and attach to a new process.
ms.date: 11/28/2017
---

# Debugging a User-Mode Process Using WinDbg Classic

You can use WinDbg to attach to a running process or to spawn and attach to a new process.

## Attaching to a Running Process

There are several ways you can use WinDbg to attach to a running process. Regardless of the method you choose, you will need the process ID or the process name. The process ID is a number assigned by the operating system. For more information about how to determine the process ID and the process name, see [Finding the Process ID](finding-the-process-id.md).

### WinDbg Menu

When WinDbg is in dormant mode, you can attach to a running process by choosing **Attach to a Process** from the **File** menu or by pressing **F6**.

In the **Attach to Process** dialog box, select the process you want to debug, and select **OK**.

### Command Prompt

In a Command Prompt window, you can attach to a running process when you launch WinDbg. Use one of the following commands:

- **windbg -p** *ProcessID*
- **windbg -pn** *ProcessName*

where *ProcessID* is the Process ID of a running process or *ProcessName* is the name of a running process.

For more information about the command-line syntax, see [**WinDbg Command-Line Options**](windbg-command-line-options.md).

### Debugger Command Window

If WinDbg is already debugging one or more processes, you can attach to a running process by using the [**.attach (Attach to Process)**](../debuggercmds/-attach--attach-to-process-.md) command in the [Debugger Command window](debugger-command-window.md).

The debugger always starts multiple target processes simultaneously, unless some of their threads are frozen or suspended.

If the [**.attach**](../debuggercmds/-attach--attach-to-process-.md) command is successful, the debugger attaches to the specified process the next time the debugger issues an execution command. If you use this command several times in a row, execution has to be requested by the debugger as many times as you use this command.

## Attaching to a Running Process Noninvasively

If you want to debug a running process and interfere only minimally in its execution, you should debug the process [noninvasively](noninvasive-debugging--user-mode-.md).

### WinDbg Menu

When WinDbg is in dormant mode, you can noninvasively debug a running process by choosing **Attach to a Process** from the **File** menu or by pressing **F6**.

When the **Attach to Process** dialog box appears, select the **Noninvasive** check box. Then, select the line that contains the process ID and name that you want. (You can also enter the process ID in the **Process ID** box.) Finally, select **OK**.

### Command Prompt

In a Command Prompt window, you can attach to a running process noninvasively when you launch WinDbg. Use one of the following commands:

- **windbg -pv -p** *ProcessID*
- **windbg -pv -pn** *ProcessName*

There are several other useful command-line options. For more information about the command-line syntax, see [**WinDbg Command-Line Options**](windbg-command-line-options.md).

### Debugger Command Window

If the debugger is already active, you can noninvasively debug a running process by using the [**.attach -v (Attach to Process)**](../debuggercmds/-attach--attach-to-process-.md) command in the [Debugger Command window](debugger-command-window.md).

You can use the **.attach** command if the debugger is already debugging one or more processes invasively. You cannot use this command if WinDbg is dormant.

If the **.attach -v** command is successful, the debugger debugs the specified process the next time that the debugger issues an execution command. Because execution is not permitted during noninvasive debugging, the debugger cannot noninvasively debug more than one process at a time. This restriction also means that using the **.attach -v** command might make an existing invasive debugging session less useful.

## Spawning a New Process

WinDbg can start a user-mode application and then debug the application. The application is specified by name. The debugger can also automatically attach to child processes (additional processes that the original target process started).

Processes that the debugger creates (also known as spawned processes) behave slightly differently than processes that the debugger does not create.

Instead of using the standard heap API, processes that the debugger creates use a special debug heap. You can force a spawned process to use the standard heap instead of the debug heap by using the \_NO\_DEBUG\_HEAP [environment variable](general-environment-variables.md) or the **-hd** command-line option.

Also, because the target application is a child process of the debugger, it inherits the debugger's permissions. This permission might enable the target application to perform certain actions that it could not perform otherwise. For example, the target application might be able to affect protected processes.

### WinDbg Menu

When WinDbg is in dormant mode, you can spawn a new process by choosing **Open Executable** from the **File** menu or by pressing CTRL+E.

When the Open Executable dialog box appears, enter the full path of the executable file in the **File name** box, or use the **Look in** list to select the path and file name that you want.

If you want to use any command-line parameters with the user-mode application, enter them in the **Arguments** box. If you want to change the starting directory from the default directory, enter the directory path in the **Start** directory box. If you want WinDbg to attach to child processes, select the **Debug child processes also** check box.

After you make your selections, select **Open**.

### Command Prompt

In a Command Prompt window, you can spawn a new process when you launch WinDbg. Use the following command:

**windbg \[-o\]** *ProgramName* **\[**<em>Arguments</em>**\]**

The **-o** option causes the debugger to attach to child processes. There are several other useful command-line options. For more information about the command-line syntax, see [**WinDbg Command-Line Options**](windbg-command-line-options.md).

### Debugger Command Window

If WinDbg is already debugging one or more processes, you can create a new process by using the [**.create (Create Process)**](../debuggercmds/-create--create-process-.md) command in the [Debugger Command window](debugger-command-window.md).

The debugger will always start multiple target processes simultaneously, unless some of their threads are frozen or suspended.

If the [**.create**](../debuggercmds/-create--create-process-.md) command is successful, the debugger creates the specified process the next time that the debugger issues an execution command. If you use this command several times in a row, execution has to be requested by the debugger as many times as you use this command.

You can control the application's starting directory by using the [**.createdir (Set Created Process Directory)**](../debuggercmds/-createdir--set-created-process-directory-.md) command before [**.create**](../debuggercmds/-create--create-process-.md). You can use the **.createdir -I** command or the **-noinh** command-line option to control whether the target application inherits the debugger's handles.

You can activate or deactivate the debugging of child processes by using the [**.childdbg (Debug Child Processes)**](../debuggercmds/-childdbg--debug-child-processes-.md) command.

## Reattaching to a Process

If the debugger stops responding or freezes, you can attach a new debugger to the target process. For more information about how to attach a debugger in this situation, see [Reattaching to the Target Application](reattaching-to-the-target-application.md).
