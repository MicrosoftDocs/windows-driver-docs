---
title: Finding the Process ID
description: Finding the Process ID
keywords: ["process, process ID (PID)", "PID (process ID)", "TList, related techniques", "Task Manager"]
ms.date: 01/18/2019
ms.localizationpriority: medium
---

# Finding the process ID


## <span id="ddk_finding_the_process_id_dbg"></span><span id="DDK_FINDING_THE_PROCESS_ID_DBG"></span>


Each process running in Microsoft Windows is assigned a unique decimal number called the process ID (PID). This number is used to specify the process when attaching a debugger to it.

You can determine the PID for a given app using Task Manager, the **tasklist** command, the TList utility, or the debugger.

## <span id="task_manager"></span><span id="TASK_MANAGER"></span>Task Manager

Task Manager can be opened in a number of ways, but the simplest is to select Ctrl+Alt+Delete, and then select **Task Manager**.

On the **Processes** tab, select **Details** to see the PID, along with other useful info.

Some kernel errors may cause delays in Task Manager's graphical interface.

## <span id="the_tasklist_command"></span><span id="THE_TASKLIST_COMMAND"></span>The **tasklist** command

Use the **tasklist** command from a command prompt to display all processes, their PIDs, and a variety of other details.

## <span id="tlist"></span><span id="TLIST"></span>TList utility

Task List Viewer (TList), or tlist.exe, is a command-line utility that displays the list of tasks, or user-mode processes, currently running on the local computer. TList is included in the Debugging Tools for Windows package.

When you run TList from the command prompt, it will display a list of all the user-mode processes in memory with a unique PID number. For each process, it shows the PID, process name, and, if the process has a window, the title of that window.

For more information, see [TList](tlist.md).

## <span id="the__tlist_debugger_command"></span><span id="THE__TLIST_DEBUGGER_COMMAND"></span>The **.tlist** debugger command

If there's already a user-mode debugger running on the system in question, the [**.tlist (List Process IDs)**](-tlist--list-process-ids-.md) command will display a list of all PIDs on that system.

## <span id="csrss_and_user_mode_drivers"></span><span id="CSRSS_AND_USER_MODE_DRIVERS"></span>CSRSS and user-mode drivers

To debug a user-mode driver running on another computer, debug the Client Server Run-Time Subsystem (CSRSS) process. For more information, see [Debugging CSRSS](debugging-csrss.md).

 

 





