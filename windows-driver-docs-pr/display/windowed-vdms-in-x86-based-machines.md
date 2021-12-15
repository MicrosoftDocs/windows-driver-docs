---
title: Windowed VDMs in x86-Based Machines
description: Windowed VDMs in x86-Based Machines
keywords:
- video miniport drivers WDK Windows 2000 , VGA, windowed VDMs in x86-based machines
- VGA WDK video miniport , windowed VDMs in x86-based machines
- windowed VDMs in x86-based machines WDK video miniport
- x86-based machines WDK VGA-compatible video miniport
ms.date: 04/20/2017
---

# Windowed VDMs in x86-Based Machines


## <span id="ddk_windowed_vdms_in_x86_based_machines_gg"></span><span id="DDK_WINDOWED_VDMS_IN_X86_BASED_MACHINES_GG"></span>


Each MS-DOS application runs as a Windows *VDM*, which in turn, runs as a console manager application in the Win32 protected subsystem.

In NT-based operating system platforms, a kernel-mode component called the *V86 emulator* traps I/O instructions issued by MS-DOS applications. As long as such an application runs within a window, its attempts to access video adapter ports are trapped and reflected back to the system-supplied video *VDD*, which emulates the behavior of the adapter for the application.

In other words, the display driver retains control of the video adapter while a VDM runs in a window.

 

 





