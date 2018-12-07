---
title: User-Mode Driver Framework Frequently Asked Questions
description: Windows Driver Frameworks (WDF) is a set of libraries that you can use to write device drivers that run on the Windows operating system.
ms.assetid: 0c07e514-73f9-4d24-86ad-8ac036fdbcf4
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# User-Mode Driver Framework Frequently Asked Questions


Windows Driver Frameworks (WDF) is a set of libraries that you can use to write device drivers that run on the Windows operating system. WDF defines a single driver model that is supported by two frameworks: Kernel-Mode Driver Framework (KMDF) and User-Mode Driver Framework (UMDF). This topic provides answers to frequently asked questions about UMDF.

## Which operating systems can run UMDF drivers?


You can run UMDF drivers on the following operating systems:

-   Windows 10
-   Windows 8.1
-   Windows 8
-   Windows 7
-   Windows Vista
-   Windows XP

## What is the most recent version of UMDF?


UMDF version 2 (both 2.0 and 2.1) is included in Windows 10 and later.

## What is the difference between UMDF version 2 and the previous version, 1.11 (one dot eleven)?


A driver written in UMDF version 2 is written in the C programming language. This same driver can then be easily compiled for KMDF. Additionally, a UMDF version 1 driver must be written according to the COM programming model. 

For more info, see [Getting Started with UMDF](getting-started-with-umdf-version-2.md).

## Which operating systems support UMDF 2?


UMDF version 2 drivers run on Windows 8.1 and later.

## Which UMDF versions can I build against in Windows Driver Kit (WDK) 10?


You can build UMDF 2.1, 2.0, 1.11, and 1.9 drivers using Windows Driver Kit (WDK) 10 and Microsoft Visual Studio. For information about which versions of Windows can run drivers built using these UMDF versions, see [UMDF Version History](umdf-version-history.md).

## Can I write part of my driver to run in user mode and part in kernel mode?


Yes. Even if your driver requires access to some kernel-mode resources or features, you might be able to split your driver into two parts. This approach enables you to benefit from some of the advantages of developing and running drivers in user mode.

A UMDF driver can receive I/O requests from a kernel-mode driver. For more info about *kernel-mode clients*, see [Supporting Kernel-Mode Clients in UMDF 2 Drivers](supporting-kernel-mode-clients-in-umdf-drivers.md).

As a result of increased parity between KMDF and UMDF, however, you will rarely need to split a driver.

##  Which framework should I start with?


If your driver requires any of the less common features listed in [Comparing UMDF 2 Functionality to KMDF](comparing-umdf-2-0-functionality-to-kmdf.md), you must use KMDF. For all other drivers, your first choice should be UMDF.

If you start with UMDF and decide later to transition to KMDF, you can do so with minimal effort, as described in [How to convert a KMDF driver to a UMDF 2 driver (and vice-versa)](how-to-generate-a-umdf-driver-from-a-kmdf-driver.md).

## How do user-mode drivers handle security?


UMDF drivers run in a driver host process, which runs in the security credentials of a LocalService account, although the host process itself is not a Windows service. Thus, user-mode drivers are as secure as any other user-mode service. When a UMDF driver issues I/O requests, it can optionally impersonate its client process. Impersonation enables the driver thread to run in the security context of the client so that the system performs access checks against the client's identity rather than that of the driver host process.

A user-mode driver can impersonate its client process only for I/O requests, and not for Plug and Play or other system messages.

At driver installation, the INF file sets a maximum impersonation level for the driver. Impersonation should be set at the lowest level possible to prevent "elevation-of-privilege" attacks. When a client application calls the **CreateFile** function, it specifies an impersonation level. The driver then requests this level of impersonation for each individual I/O request.

## Will a user-mode driver be fast enough?


Performance is a high priority in developing UMDF. Although latency and CPU usage both increase somewhat, bus capacity is the primary gating factor for the types of devices that UMDF supports.

## What is the difference between a user-mode driver and an application?


A user-mode driver is started by the Driver Manager and runs in a driver host process. A single instance of the driver can service simultaneous requests from multiple applications. To communicate with the driver, applications issue I/O requests to the driver's device through the Win32 API. The primary entry point in a user-mode driver is the [**IDriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff554885) interface (UMDF 1.11 and earlier) or the [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff540807) routine (starting in UMDF 2.0), rather than a **main()** function.

A driver also includes additional interfaces or callbacks that are invoked in response to I/O requests and Plug and Play and power notifications. A device that is managed by a UMDF driver is integrated into the system and participates in Plug and Play and power management.

## How do I debug a UMDF driver?


You can debug a UMDF driver by using user-mode debuggers or kernel-mode debuggers. For more info, see [Debugging WDF Drivers](debugging-a-wdf-driver.md).

Starting in UMDF version 2.0, you can use many of the commands in the *Wdfkd.dll* debugger extension library to debug your UMDF driver. For a list of commands, see [Debugger Extensions](debugger-extensions-for-kmdf-drivers.md). In addition, UMDF stores the UMDF trace log (or UMDF *IFR*) in kernel non-paged memory. For info about the IFR, see [Using the Framework's Event Logger](using-the-framework-s-event-logger.md).

## Is there a newsgroup for UMDF?


You can find discussion of all aspects of Windows drivers on the following forums:

-   Microsoft maintains the [Windows Hardware WDK and Driver Development](http://social.msdn.microsoft.com/Forums/windowsdesktop/home?forum=wdk) forum.

-   Open Systems Resources (OSR) moderates the [OSR Online NTDEV List](http://www.osronline.com/showlists.cfm?list=ntdev) forum.

 

 





