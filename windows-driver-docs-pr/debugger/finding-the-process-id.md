---
title: Finding the Process ID
description: Finding the Process ID
ms.assetid: 963e9b5b-2b88-41b5-a103-dc4611ff41ea
keywords: ["process, process ID (PID)", "PID (process ID)", "TList, related techniques", "Task Manager"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Finding the Process ID


## <span id="ddk_finding_the_process_id_dbg"></span><span id="DDK_FINDING_THE_PROCESS_ID_DBG"></span>


Each process running in Microsoft Windows is assigned a unique decimal number called the *process ID*, or *PID*. This number is used to specify the process when attaching a debugger to it.

There are several ways to determine the PID for a given application: using the Task Manager, using the **tasklist** command, using the TList utility, or using the debugger.

### <span id="task_manager"></span><span id="TASK_MANAGER"></span>Task Manager

The *Task Manager* may be activated in a number of ways, but the simplest is to press CTRL+ALT+DELETE and then click **Task Manager**.

If you select the **Processes** tab, each process and its PID will be listed, along with other useful information.

Some kernel errors may cause delays in Task Manager's graphical interface.

### <span id="the_tasklist_command"></span><span id="THE_TASKLIST_COMMAND"></span>The Tasklist Command

In Windows XP and later versions of Windows, you can use the **tasklist** command from a Command Prompt window. This displays all processes, their PIDs, and a variety of other details.

### <span id="tlist"></span><span id="TLIST"></span>TList

TList (Task List Viewer, tlist.exe) is a command-line utility that displays a list of tasks, or user-mode processes, currently running on the local computer. TList is included in the Debugging Tools for Windows package.

When you run TList from the command prompt, it will display a list of all the user-mode processes in memory with a unique process identification (PID) number. For each process, it shows the PID, process name, and, if the process has a window, the title of that window.

For more information, see [TList](tlist.md).

### <span id="the__tlist_debugger_command"></span><span id="THE__TLIST_DEBUGGER_COMMAND"></span>The .tlist Debugger Command

If there is already a user-mode debugger running on the system in question, the [**.tlist (List Process IDs)**](-tlist--list-process-ids-.md) command will display a list of all PIDs on that system.

### <span id="csrss_and_user_mode_drivers"></span><span id="CSRSS_AND_USER_MODE_DRIVERS"></span>CSRSS and User-Mode Drivers

To debug a user-mode driver running on another computer, debug the Client Server Run-Time Subsystem (CSRSS) process. For more information, see [Debugging CSRSS](debugging-csrss.md).

 

 





