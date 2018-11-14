---
title: Finding a Kernel-Mode Memory Leak
description: Finding a Kernel-Mode Memory Leak
ms.assetid: 7e707b89-8614-46d7-9c2e-bea2ddf16164
keywords: ["memory leak, kernel-mode", "memory leak, kernel-mode, overview"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Finding a Kernel-Mode Memory Leak


Use the following techniques to determine the cause of a kernel-mode memory leak:

[Using PoolMon to Find a Kernel-Mode Memory Leak](using-poolmon-to-find-a-kernel-mode-memory-leak.md)

[Using the Kernel Debugger to Find a Kernel-Mode Memory Leak](using-the-kernel-debugger-to-find-a-kernel-mode-memory-leak.md)

[Using Driver Verifier to Find a Kernel-Mode Memory Leak](using-driver-verifier-to-find-a-kernel-mode-memory-leak.md)

If you do not know which kernel-mode driver or component is responsible for the leak, you should use the PoolMon technique first. This technique reveals the pool tag associated with the memory leak; the driver or component that uses this pool tag is responsible for the leak.

If you have already identified the responsible driver or component, use the second and third techniques in the preceding list to determine the cause of the leak more specifically.

 

 





