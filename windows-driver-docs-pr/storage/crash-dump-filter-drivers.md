---
title: Crash Dump Filter Drivers
description: Crash Dump Filter Drivers
ms.assetid: d91c00d7-ad17-4fa8-9e78-fee0698d9049
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Crash Dump Filter Drivers


To extend the usefulness of the crash dump interface, for Windows Vista with Service Pack 1 (SP1) and Windows Server 2008 and later operating systems, Microsoft has defined filter driver support in the crash dump driver stack.

The crash dump driver does not use the typical runtime storage driver stack to write dump data to the disk. By adding filter driver support in the crash dump driver stack, new functionality can be added without changing the kernel. For example, it becomes possible to encrypt the contents of the hibernation or crash dump file.

 

 




