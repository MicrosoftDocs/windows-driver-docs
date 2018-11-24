---
title: Asynchronous I/O Programming
description: Asynchronous I/O Programming
ms.assetid: f50c98ab-3aae-43f6-be91-2ae587105767
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Asynchronous I/O Programming


Asynchronous programming does not force everyone else to wait. This is the preferred technique for programming Windows device drivers. Supporting asynchronous I/O is one of the design goals of WDM drivers. For more information about asynchronous I/O in drivers, see [Supporting Asynchronous I/O](supporting-asynchronous-i-o.md). For device drivers, using interrupts is the best way to program asynchronously. You simply send a request to your device and let the system take control. Then when your device wants to tell you something, it triggers an interrupt that the operating system processes by calling an interrupt handler in your driver. This communication is handled through IRPs. For more information about IRPS, see [Handling IRPs](handling-irps.md).

 

 




