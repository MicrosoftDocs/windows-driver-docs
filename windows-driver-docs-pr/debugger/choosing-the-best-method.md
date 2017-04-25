---
title: Choosing the Best Method
description: Choosing the Best Method
ms.assetid: d6069c8c-1da1-4930-b75d-efcee9691e6b
---

# Choosing the Best Method


There are several different ways to debug a service application. In order to choose the correct method, you must first make two choices: the time at which the debugger is attached to the service application and what debugging configuration to use.

There are three stages at which the debugger can be attached to the service application:

-   The very beginning of the service startup. The debugger is automatically launched when the service begins. Choose this option if you want to debug the service's initialization code.

-   The first time that the service encounters an exception. The debugger is automatically launched when an exception or crash occurs or if the service application calls the **DebugBreak** function. Choose this option if you want the debugger to appear when a problem is encountered but not before.

-   After the service is running normally. You can manually attach a debugger to a service that is already running at any time. Choose this option if you do not want to make advance preparations for debugging.

There are three debugging configurations you can choose:

-   Local debugging. A single debugger, running on the same computer as the service.

-   Remote debugging. A debugging server running on the same computer as the service, being controlled from a debugging client running on a second computer.

-   Kernel-controlled user-mode debugging. A user-mode debugger running on the same computer as the service, being controlled from a kernel debugger on a second computer.

If your service is running on Windows 2000, Windows XP, or Windows Server 2003, you can combine any of these three attach options with any of these three debugging configuration options.

If your service is running on Windows Vista or a later version of Windows, there is one restriction on how these choices can be combined. If you want to debug from the beginning of the service startup, or from the time that an exception is encountered, you must use either remote debugging or kernel-controlled user-mode debugging.

In other words, on Windows Vista and later, you cannot use local debugging unless you plan to attach the debugger manually after the service is already running. This restriction results from the fact that in these versions of Windows, services run in session 0, and any debugger that is automatically launched and attached to the service is also in session 0, and does not have a user interface on the computer that the service is running on.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Choosing%20the%20Best%20Method%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




