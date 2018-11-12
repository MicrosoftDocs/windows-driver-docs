---
title: Debugging a Stalled System
description: Debugging a Stalled System
ms.assetid: 83679dca-2477-4d03-9a89-5a5aebc7b9d9
keywords: ["stalled system debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Debugging a Stalled System


## <span id="ddk_debugging_a_stalled_system_dbg"></span><span id="DDK_DEBUGGING_A_STALLED_SYSTEM_DBG"></span>


There are times when the computer can stop responding without actually initiating a bug check. This "freeze" can appear in a variety of forms:

-   The mouse pointer can be moved, but does not affect any windows on the screen.

-   The entire screen is still and the mouse pointer does not move, but paging continues between the memory and the disk.

-   The screen is still and the disk is silent.

If the mouse pointer moves or there is paging to the disk, this is usually due to a problem within the Client Server Run-Time Subsystem (CSRSS).

If NTSD is running on CSRSS, press F12 and dump out each thread to see if there is anything out of the ordinary. (See [Debugging CSRSS](debugging-csrss.md) for more details.)

If an examination of CSRSS reveals nothing, then the problem may be with the kernel after all.

If there is no mouse movement or paging, then it is almost certainly a kernel problem.

Analyzing a kernel crash of this sort is generally a difficult task. To begin, break into KD (with [**CTRL+C**](ctrl-c--break-.md)) or WinDbg (with **CTRL+BREAK**). You can now use the debugger commands to examine the situation.

Some useful techniques in this case include:

[Finding the Failed Process](finding-the-failed-process.md)

[Debugging an Interrupt Storm](debugging-an-interrupt-storm.md)

 

 





