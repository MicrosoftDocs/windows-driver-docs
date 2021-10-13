---
title: Introduction to Crash Dump Filter Drivers
description: Crash Dump Filter Drivers
ms.date: 12/15/2019
ms.localizationpriority: medium
---

# Introduction to Crash Dump Filter Drivers

To extend the usefulness of the crash dump interface, for Windows Vista with Service Pack 1 (SP1) and Windows Server 2008 and later operating systems, Microsoft has defined filter driver support in the crash dump driver stack.

The crash dump driver does not use the typical runtime storage driver stack to write dump data to the disk. By adding filter driver support in the crash dump driver stack, new functionality can be added without changing the kernel. For example, it becomes possible to encrypt the contents of the hibernation or crash dump file.
