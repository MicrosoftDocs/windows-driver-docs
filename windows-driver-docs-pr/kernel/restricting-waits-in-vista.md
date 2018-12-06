---
title: Restricting Waits in Vista
description: Restricting Waits in Vista
ms.assetid: edcc25d0-bcf6-48f0-832e-3f911bd42142
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Restricting Waits in Vista


Because many device driver developers use [Synchronous I/O Programming Techniques](synchronous-i-o-programming.md), Windows can slow down or "freeze up" while a device is taking time to respond. To reduce this problem, the I/O Manager in Vista will stop execution of programs that are "stuck" waiting for a device to respond after a few moments.

**Note**   It is strongly recommended that [Synchronous I/O Programming Techniques](synchronous-i-o-programming.md) are avoided in your device driver. If Vista stops execution of your driver code because your driver is waiting for a device, your device may be left in an unknown state.

 

 

 




