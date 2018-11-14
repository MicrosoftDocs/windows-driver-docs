---
title: Setting Up Kernel-Mode Debugging in Visual Studio
description: You can use Microsoft Visual Studio to set up and perform kernel-mode debugging of Windows.
ms.assetid: 38E57F45-71D9-4467-BECF-42769563751E
keywords: ["Kernel-mode debugging, Visual Studio", "Setting up kernel-mode debugging, Visual Studio"]
ms.author: domars
ms.date: 04/10/2017
ms.localizationpriority: medium
---

# <span id="debugger.setting_up_kernel-mode_debugging_in_visual_studio"></span>Setting Up Kernel-Mode Debugging in Visual Studio

> [!IMPORTANT]
> This feature is not available in Windows 10, version 1507 and later versions of the WDK.
>


You can use Microsoft Visual Studio to set up and perform kernel-mode debugging of Windows. To use Visual Studio for kernel-mode debugging, you must have the Windows Driver Kit (WDK) integrated with Visual Studio. For information about how to install the integrated environment, see [Windows Driver Development](https://go.microsoft.com/fwlink/p?linkid=301383).
 

As an alternative to using Visual Studio to set up kernel-mode debugging, you can do the setup manually. For more information, see [Setting Up Kernel-Mode Debugging Manually](setting-up-kernel-mode-debugging-in-windbg--cdb--or-ntsd.md).

Kernel-mode debugging typically requires two computers. The debugger runs on the *host computer,* and the code being debugged runs on the *target computer*.

## <span id="in_this_section"></span>In this section


-   [Setting Up Kernel-Mode Debugging over a Network Cable in Visual Studio](setting-up-a-network-debugging-connection-in-visual-studio.md)
-   [Setting Up Kernel-Mode Debugging over a 1394 Cable in Visual Studio](setting-up-a-1394-cable-connection-in-visual-studio.md)
-   [Setting Up Kernel-Mode Debugging over a USB 3.0 Cable in Visual Studio](setting-up-a-usb-3-0-cable-connection-in-visual-studio.md)
-   [Setting Up Kernel-Mode Debugging over a USB 2.0 Cable in Visual Studio](setting-up-a-usb-2-0-cable-connection-in-visual-studio.md)
-   [Setting Up Kernel-Mode Debugging over a Serial Cable in Visual Studio](setting-up-a-null-modem-cable-connection-in-visual-studio.md)
-   [Setting Up Kernel-Mode Debugging using Serial over USB in Visual Studio](setting-up-kernel-mode-debugging-using-serial-over-usb-in-visual-studio.md)
-   [Setting Up Kernel-Mode Debugging of a Virtual Machine in Visual Studio](setting-up-a-connection-to-a-virtual-machine-in-visual-studio.md)

## <span id="related_topics"></span>Related topics


[Setting Up Debugging (Kernel-Mode and User-Mode)](getting-set-up-for-debugging.md)

[Setting Up Kernel-Mode Debugging Manually](setting-up-kernel-mode-debugging-in-windbg--cdb--or-ntsd.md)

 

 






