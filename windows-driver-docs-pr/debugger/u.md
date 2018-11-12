---
title: U (Windows Debugger Glossary)
description: Glossary page - U
Robots: noindex, nofollow
ms.assetid: f3866ed9-eb94-4433-8a73-3b37f7e67303
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# U


<span id="user_mode"></span><span id="USER_MODE"></span>**user mode**  
Applications and subsystems run within Windows in *user mode*. Processes that run in user mode do so within their own virtual address spaces. They are restricted from gaining direct access to many parts of the system, including system hardware, memory that was not allocated for their use, and other portions of the system that might compromise system integrity. Because processes that run in user mode are effectively isolated from the system and other user-mode processes, they cannot interfere with these resources.

User-mode processes can be grouped in the following categories:

-   System Processes

    These perform important functions and are integral part of the operating system. System processes include such items as the logon process and the session manager process.

-   Server Processes

    These are operating system services such as the Event Log and the Scheduler. They can be configured to start automatically at boot time.

-   Environment Subsystems

    These are used to create a complete operating system environment for the applications. Windows provides the following three environments: Win32, POSIX, and OS/2.

-   User Applications

    There are five types: Win32, Windows 3.1, Microsoft MS-DOS, POSIX, and OS/2.

<span id="user_mode_debugging"></span><span id="USER_MODE_DEBUGGING"></span>**user-mode debugging**  
A debugger session in which the target is running in user mode.

<span id="user_mode_target"></span><span id="USER_MODE_TARGET"></span>**user-mode target**  
See target application.

 

 





