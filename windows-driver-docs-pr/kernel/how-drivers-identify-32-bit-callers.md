---
title: How Drivers Identify 32-Bit Callers
description: How Drivers Identify 32-Bit Callers
ms.assetid: 9bfe9024-60f1-41ad-a034-160caaaa7801
keywords: ["32-bit I/O support WDK 64-bit , identifying 32-bit callers", "identifying 32-bit callers", "32-bit caller identifications WDK 64-bit", "file system control codes WDK 64-bit", "FSCTL WDK 64-bit", "control codes WDK 64-bit", "I/O control codes WDK kernel , 32-bit I/O in 64-bit drivers", "IOCTLs WDK kernel , 32-bit I/O in 64-bit drivers", "caller identifications WDK 64-bit"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# How Drivers Identify 32-Bit Callers





There are two ways for drivers to determine whether the originator of an IOCTL or FSCTL request is a 32-bit or 64-bit application. The first is for the application to identify itself. The second is for the driver to determine on its own whether the application is 32-bit or 64-bit.

The first technique involves defining a "64Bit" field in the IOCTL or FSCTL control code. This field contains a single bit, which is set only for 64-bit callers. Thus 64-bit callers identify themselves by using a separate set of 64-bit control codes in which this bit is set. 32-bit callers use a similar set of control codes in which this bit is not set.

The second technique permits 32- and 64-bit applications to continue using the same IOCTL or FSCTL codes. Instead, the driver determines whether the user-mode process is 32- or 64-bit by calling [**IoIs32bitProcess**](https://msdn.microsoft.com/library/windows/hardware/ff549372).

The first technique is more efficient, because the driver checks a bit flag instead of calling a kernel-mode routine. However, the second technique requires no changes to user-mode code. Which technique you should use depends on the requirements of your driver and the applications that send I/O requests to it.

 

 




