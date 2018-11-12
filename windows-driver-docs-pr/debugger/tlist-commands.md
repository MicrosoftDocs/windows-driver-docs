---
title: TList Commands
description: The syntax of the TList command is as follows
ms.assetid: d1527ffe-ea80-4e02-9a32-b6eccddc1c6a
keywords: TList Commands, Windows debugging
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- TList Commands
api_type:
- NA
ms.localizationpriority: medium
---

# TList Commands


The syntax of the TList command is as follows:

```dbgcmd
tlist [/p ProcessName | PID | Pattern | /t | /c | /e | /k | /m [Module] | /s | /v
```

## <span id="ddk_tlist_commands_dtools"></span><span id="DDK_TLIST_COMMANDS_DTOOLS"></span>Parameters


<span id="_______tlist______"></span><span id="_______TLIST______"></span> **tlist**   
Without additional parameters, TList displays all running processes, their process identifiers (PIDs), and the title of the window in which they are running, if any.

<span id="________p_______ProcessName______"></span><span id="________p_______processname______"></span><span id="________P_______PROCESSNAME______"></span> **/p** *ProcessName*   
Displays the process identifier (PID) of the specified process.

*ProcessName* is the name of the process (with or without file name extension), not a pattern.

If the value of *ProcessName* does not match any running process, TList displays -1. If it matches more than one process name, TList displays only the PID of the first matching process.

<span id="_______PID______"></span><span id="_______pid______"></span> *PID*   
Displays detailed information about the process specified by the PID. For information about the display, see the "Remarks" section below. To find a process ID, type **tlist** without additional parameter.

<span id="_______Pattern______"></span><span id="_______pattern______"></span><span id="_______PATTERN______"></span> *Pattern*   
Displays detailed information about all processes whose names or window titles match the specified pattern. Pattern can be a complete name or a regular expression.

<span id="________t______"></span><span id="________T______"></span> **/t**   
Displays a task tree in which each process appears as a child of the process that created it.

<span id="________c______"></span><span id="________C______"></span> **/c**   
Displays the command line that started each process.

<span id="________e______"></span><span id="________E______"></span> **/e**   
Displays the session identifier for each process.

<span id="________k______"></span><span id="________K______"></span> **/k**   
Displays the COM components active in each process.

<span id="________m_______Module______"></span><span id="________m_______module______"></span><span id="________M_______MODULE______"></span> **/m** *Module*   
Lists tasks in which the specified DLL or executable module is loaded. Module can be a complete module name or a module name pattern.

<span id="________s______"></span><span id="________S______"></span> **/s**   
Displays the services that are active in each process.

<span id="________v______"></span><span id="________V______"></span> **/v**   
Displays details of running processes including the process ID, session ID, window title, command line, and the services running in the process.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

In its detailed display of a process (**tlist** *PID* or **tlist** *Pattern*), TList displays the following information.

-   Process ID, executable name, friendly name of the program.

-   Current working directory (CWD).

-   The command line that started the process (CmdLine).

-   Current virtual address space values.

-   Number of threads.

-   A list of threads running in the process. For each thread, TList displays the thread ID (TID), the function that the thread is running, the address of the entry point, the address of the last reported error (if any), and the thread state.

-   A list of the modules loaded for the process. For each module, TList displays the version number, attributes, virtual address of the module, and the module name.

When using the **/e** parameter, valid session identifiers appear in the process list only under the following conditions. Otherwise, the session identifier is zero (0).

-   On Windows 2000 and Windows Server 2003, at least one user must be connected to a session other than the console session.

-   On Windows XP, Fast User Switching must be enabled and more than one user must be connected to the non-console session.

-   On Windows Vista, where all processes are associated with two Terminal Services sessions by default, at least one user must be connected to the non-console session.

 

 





