---
title: Debugging a Stalled System
description: Debugging a Stalled System
ms.assetid: 83679dca-2477-4d03-9a89-5a5aebc7b9d9
keywords: ["stalled system debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20a%20Stalled%20System%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




