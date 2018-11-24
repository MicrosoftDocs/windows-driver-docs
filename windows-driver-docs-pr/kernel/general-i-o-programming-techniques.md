---
title: General I/O Programming Techniques
description: General I/O Programming Techniques
ms.assetid: c310829f-e102-4a96-aa3e-39136b8a641b
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# General I/O Programming Techniques


One of the most important techniques in I/O programming is one that you should avoid: forcing the operating system to wait for your device. Almost everyone has had the experience of seeing Microsoft Windows "freeze up". Sometimes the freeze is due to a crash, but other times the system is simply waiting for a device to respond.

There are two basic programming techniques for dealing with waiting for a device: *synchronous* and *asynchronous*. Synchronous programming waits for the device and should be avoided. Asynchronous programming uses other techniques (such as waiting for interrupt requests). For more information about synchronous and asynchronous programming, see the following topics:

[Synchronous I/O Programming](synchronous-i-o-programming.md)

[Asynchronous I/O Programming](asynchronous-i-o-programming.md)

Microsoft Vista has a new policy for dealing with problems with synchronous programming. For more information about this new policy, see [Restricting Waits in Windows Vista](restricting-waits-in-vista.md) for more information.

In earlier device driver programming, a driver would need to repeatedly request information from a driver until the answer was provided. This technique is called polling and should almost never be used. The best way to handle the problem of polling is to use hardware interrupts. For more information about hardware interrupts, see [Servicing Interrupts](servicing-interrupts.md). For more information on polling and why you should not use it, see [Avoid Device Polling](avoid-polling-devices.md).

 

 




