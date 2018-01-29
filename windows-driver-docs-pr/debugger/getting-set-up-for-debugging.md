---
title: Setting Up Debugging (Kernel-Mode and User-Mode)
description: There are two ways you can set up debugging with the Windows debuggers.
ms.assetid: 3575B850-A0F9-4AAE-9432-E970D40069D2
keywords: ["setup debugging", "configure debugging", "configure debugger", "WinDbg", "Visual Studio debugging", "kernel-mode debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Setting Up Debugging (Kernel-Mode and User-Mode)


There are two ways you can set up debugging with the Windows debuggers. You can use Microsoft Visual Studio (integrated with the Windows Driver Kit (WDK)), or you can do the setup manually. After you set up kernel-mode debugging, you can use Visual Studio, WinDbg, or KD to establish a debugging session. After you set up user-mode debugging, you can use Visual Studio, WinDbg, CDB, or NTSD to establish a debugging session.

**Note**  The Windows debuggers are included in Debugging Tools for Windows. These debuggers are different from the Visual Studio debugger, which is included with Visual Studio. For more information, see [Windows Debugging](index.md).

 

## <span id="in_this_section"></span>In this section


-   [Setting Up Kernel-Mode Debugging Manually](setting-up-kernel-mode-debugging-in-windbg--cdb--or-ntsd.md)
-   [Supported Ethernet NICs for Network Kernel Debugging in Windows 10](supported-ethernet-nics-for-network-kernel-debugging-in-windows-10.md)
-   [Supported Ethernet NICs for Network Kernel Debugging in Windows 8.1](supported-ethernet-nics-for-network-kernel-debugging-in-windows-8-1.md)
-   [Supported Ethernet NICs for Network Kernel Debugging in Windows 8](supported-ethernet-nics-for-network-kernel-debugging-in-windows-8.md)
-   [Setting Up User-Mode Debugging in Visual Studio](setting-up-user-mode-debugging-in-visual-studio.md)
-   [Setting Up Network Debugging of a Virtual Machine Host](setting-up-network-debugging-of-a-virtual-machine-host.md)
-   [Configuring tools.ini](configuring-tools-ini.md)
-   [Using KDbgCtrl](using-kdbgctrl.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Setting%20Up%20Debugging%20%28Kernel-Mode%20and%20User-Mode%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




