---
title: TList
description: TList (Task List Viewer), Tlist.exe, displays the processes running on the local computer along with useful information about each process.
ms.assetid: 4cba525f-12f0-45c9-8dee-c3e0ab9fd944
keywords: ["TList", "Task List Viewer", "Task List Viewer, See "TList""]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20TList%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




