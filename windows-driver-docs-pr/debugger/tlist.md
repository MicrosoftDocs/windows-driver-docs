---
title: TList
description: TList (Task List Viewer), Tlist.exe, displays the processes running on the local computer along with useful information about each process.
ms.assetid: 4cba525f-12f0-45c9-8dee-c3e0ab9fd944
keywords: TList, Task List Viewer, Task List Viewer, See TList
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# TList


## <span id="ddk_tlist_dtools"></span><span id="DDK_TLIST_DTOOLS"></span>


TList (Task List Viewer), Tlist.exe, is a command-line tool that displays the processes running on the local computer along with useful information about each process.

TList displays:

-   All processes running on the computer, along with their process IDs (PIDs).

-   A tree showing which processes created each process.

-   Details of the process, including its virtual memory use and the command that started the process.

-   Threads running in each process, including their thread IDs, entry points, last reported error, and thread state.

-   The modules running in each process, including the version number, attributes, and virtual address of the module.

You can use TList to search for a process by name or PID, or to find all processes that have loaded a specified module.

In Windows XP and later versions of Windows, TList was replaced by TaskList (Tasklist.exe), which is described in Help and Support for those systems. TList is included in Debugging Tools for Windows to support users who do not have access to TaskList.

This section includes:

[**TList Commands**](tlist-commands.md)

[TList Examples](tlist-examples.md)

 

 





