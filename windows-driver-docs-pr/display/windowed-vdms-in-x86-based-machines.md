---
title: Windowed VDMs in x86-Based Machines
description: Windowed VDMs in x86-Based Machines
ms.assetid: 01250cef-1ddb-4b32-a155-0170e1e4517a
keywords:
- video miniport drivers WDK Windows 2000 , VGA, windowed VDMs in x86-based machines
- VGA WDK video miniport , windowed VDMs in x86-based machines
- windowed VDMs in x86-based machines WDK video miniport
- x86-based machines WDK VGA-compatible video miniport
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Windowed VDMs in x86-Based Machines


## <span id="ddk_windowed_vdms_in_x86_based_machines_gg"></span><span id="DDK_WINDOWED_VDMS_IN_X86_BASED_MACHINES_GG"></span>


Each MS-DOS application runs as a Windows [*VDM*](https://msdn.microsoft.com/library/windows/hardware/ff556344#wdkgloss-vdm), which in turn, runs as a console manager application in the Win32 protected subsystem.

In NT-based operating system platforms, a kernel-mode component called the *V86 emulator* traps I/O instructions issued by MS-DOS applications. As long as such an application runs within a window, its attempts to access video adapter ports are trapped and reflected back to the system-supplied video [*VDD*](https://msdn.microsoft.com/library/windows/hardware/ff556344#wdkgloss-vdd), which emulates the behavior of the adapter for the application.

In other words, the display driver retains control of the video adapter while a VDM runs in a window.

 

 





