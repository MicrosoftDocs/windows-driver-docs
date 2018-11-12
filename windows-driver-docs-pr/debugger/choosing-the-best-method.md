---
title: Choosing the Best Method
description: Choosing the Best Method
ms.assetid: d6069c8c-1da1-4930-b75d-efcee9691e6b
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
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

 

 





