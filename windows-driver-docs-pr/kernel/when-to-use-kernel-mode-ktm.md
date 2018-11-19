---
title: When to Use Kernel-Mode KTM
description: When to Use Kernel-Mode KTM
ms.assetid: deb3372d-19c4-4a17-b499-1da485e89276
keywords: ["Kernel Transaction Manager WDK , when to use", "KTM WDK , when to use"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# When to Use Kernel-Mode KTM


You can use kernel-mode KTM with your kernel-mode component to support transacted operations in kernel mode, or to coordinate transacted operations between a kernel-mode component that uses kernel-mode KTM and a user-mode component that uses user-mode KTM.

For example, you might use KTM in the following situations:

-   Your kernel-mode driver must open a file, modify the file's contents, and save the modified file, and it must prevent damage to the file if a write operation fails. If your driver performs these operations within a transaction, the driver does not have to copy and rename the old file, modify the new copy, delete the old file, and then rename the new copy.

-   You are designing a new data storage system that stores information in one or more databases. Components of your system will access the databases in kernel mode, or possibly in both user mode and kernel mode. Transactional clients of your system will encapsulate their database operations within transactions so that all modifications to all databases either succeed or fail as a unit.

 

 




