---
title: Forcing a System Crash
description: Forcing a System Crash
ms.assetid: db93b032-2ca7-4197-87dd-4ae77c328f60
keywords: ["system crash, overview"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Forcing%20a%20System%20Crash%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




