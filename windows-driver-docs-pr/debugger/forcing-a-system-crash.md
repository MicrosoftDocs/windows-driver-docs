---
title: Forcing a System Crash
description: Forcing a System Crash
ms.assetid: db93b032-2ca7-4197-87dd-4ae77c328f60
keywords: ["system crash, overview"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Forcing a System Crash


## <span id="ddk_forcing_a_system_crash_dbg"></span><span id="DDK_FORCING_A_SYSTEM_CRASH_DBG"></span>


Once kernel-mode dump files have been [enabled](enabling-a-kernel-mode-dump-file.md), most system crashes should cause a crash file to be written and the blue screen to be displayed.

However, there are times that a system freezes without actually initiating a kernel crash. Possible symptoms of such a freeze include:

-   The mouse pointer moves, but can't do anything.

-   All video is frozen, the mouse pointer does not move, but paging continues.

-   There is no response at all to the mouse or keyboard, and no use of the disk.

If an experienced debugging technician is present, he or she can hook up a kernel debugger and analyze the problem. For some tips on what to look for when this situation occurs, see [Debugging a Stalled System](debugging-a-stalled-system.md).

However, if no technician is present, you may wish to create a kernel-mode dump file and send it to an off-site technician. This dump file can be used to analyze the cause of the error.

There are two ways to deliberately cause a system crash:

[Forcing a System Crash from the Debugger](forcing-a-system-crash-from-the-debugger.md)

[Forcing a System Crash from the Keyboard](forcing-a-system-crash-from-the-keyboard.md)

 

 





