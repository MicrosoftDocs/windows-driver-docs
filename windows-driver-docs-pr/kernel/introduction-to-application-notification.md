---
title: Introduction to Application Notification
description: Introduction to Application Notification
ms.assetid: c115eb29-8bd2-40f7-b979-cff386bdc9aa
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Introduction to Application Notification


Starting with Windows Server 2008, processors and memory modules are considered Plug and Play (PnP) devices. Therefore, the operating system uses the PnP notification mechanism for application notification. The PnP notification mechanism sends WM\_DEVICECHANGE window messages to user-mode applications to notify the applications about changes to the hardware in the hardware partition.

When a new processor or memory module is added to the hardware partition, the operating system sends this notification to user-mode applications after the operating system has started the new processor or memory device. In the case of a new processor, the operating system does not send this message to user-mode applications until after it has started scheduling threads on the new processor.

**Note**   All PnP notifications are asynchronous. Therefore, these notifications might not be received by a user-mode application until sometime after the operating system has started the processor or memory module.

 

When a user-mode application receives this notification, it can adjust some or all of the following items accordingly:

-   Per processor memory allocations

-   The number of threads in the thread pools of the application

-   Memory buffer allocations

-   Load balancing algorithms

A user-mode application can get the amount of physical memory that is in the hardware partition by calling the [GlobalMemoryStatusEx](http://go.microsoft.com/fwlink/p/?linkid=97891) function. For more information about the **GlobalMemoryStatusEx** function, see the Microsoft Windows SDK documentation.

A user-mode application must register itself with the operating system to receive application notification. For more information, see [Registering for Application Notification](registering-for-application-notification.md).

 

 




