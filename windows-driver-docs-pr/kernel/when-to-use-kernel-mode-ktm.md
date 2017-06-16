---
title: When to Use Kernel-Mode KTM
author: windows-driver-content
description: When to Use Kernel-Mode KTM
ms.assetid: deb3372d-19c4-4a17-b499-1da485e89276
keywords: ["Kernel Transaction Manager WDK , when to use", "KTM WDK , when to use"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# When to Use Kernel-Mode KTM


You can use kernel-mode KTM with your kernel-mode component to support transacted operations in kernel mode, or to coordinate transacted operations between a kernel-mode component that uses kernel-mode KTM and a user-mode component that uses user-mode KTM.

For example, you might use KTM in the following situations:

-   Your kernel-mode driver must open a file, modify the file's contents, and save the modified file, and it must prevent damage to the file if a write operation fails. If your driver performs these operations within a transaction, the driver does not have to copy and rename the old file, modify the new copy, delete the old file, and then rename the new copy.

-   You are designing a new data storage system that stores information in one or more databases. Components of your system will access the databases in kernel mode, or possibly in both user mode and kernel mode. Transactional clients of your system will encapsulate their database operations within transactions so that all modifications to all databases either succeed or fail as a unit.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20When%20to%20Use%20Kernel-Mode%20KTM%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


