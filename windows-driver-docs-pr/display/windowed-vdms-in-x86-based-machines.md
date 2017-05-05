---
title: Windowed VDMs in x86-Based Machines
description: Windowed VDMs in x86-Based Machines
ms.assetid: 01250cef-1ddb-4b32-a155-0170e1e4517a
keywords:
- video miniport drivers WDK Windows 2000 , VGA, windowed VDMs in x86-based machines
- VGA WDK video miniport , windowed VDMs in x86-based machines
- windowed VDMs in x86-based machines WDK video miniport
- x86-based machines WDK VGA-compatible video miniport
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Windowed VDMs in x86-Based Machines


## <span id="ddk_windowed_vdms_in_x86_based_machines_gg"></span><span id="DDK_WINDOWED_VDMS_IN_X86_BASED_MACHINES_GG"></span>


Each MS-DOS application runs as a Windows [*VDM*](https://msdn.microsoft.com/library/windows/hardware/ff556344#wdkgloss-vdm), which in turn, runs as a console manager application in the Win32 protected subsystem.

In NT-based operating system platforms, a kernel-mode component called the *V86 emulator* traps I/O instructions issued by MS-DOS applications. As long as such an application runs within a window, its attempts to access video adapter ports are trapped and reflected back to the system-supplied video [*VDD*](https://msdn.microsoft.com/library/windows/hardware/ff556344#wdkgloss-vdd), which emulates the behavior of the adapter for the application.

In other words, the display driver retains control of the video adapter while a VDM runs in a window.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Windowed%20VDMs%20in%20x86-Based%20Machines%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




