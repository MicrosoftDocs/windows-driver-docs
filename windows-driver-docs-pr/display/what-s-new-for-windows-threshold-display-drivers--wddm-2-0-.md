---
title: What's new for Windows 10 display drivers (WDDM 2.0)
description: Describes new features in Windows 10 for display drivers
ms.assetid: 619175D4-98DA-4B17-8F6F-71B13A31374D
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# What's new for Windows 10 display drivers (WDDM 2.0)


### <span id="Memory_Management"></span><span id="memory_management"></span><span id="MEMORY_MANAGEMENT"></span>Memory Management

GPU virtual memory

-   All physical memory is abstracted into virtual segments that can be managed by the graphics processing unit (GPU) memory manager.
-   Each process gets its own GPU virtual address space.
-   Support for swizzling ranges has been removed.

For more details, see [GPU virtual memory in WDDM 2.0](gpu-virtual-memory-in-wddm-2-0.md).

Driver residency

-   The video memory manager makes sure that allocations are resident in memory before submitting command buffers to the driver. To facilitate this functionality, new user mode driver device driver interfaces (DDIs) have been added ([*MakeResident*](https://msdn.microsoft.com/library/windows/hardware/dn906357), [*TrimResidency*](https://msdn.microsoft.com/library/windows/hardware/dn906364), [*Evict*](https://msdn.microsoft.com/library/windows/hardware/dn906355)).
-   The allocation and patch location list is being phased out because it is not necessary in the new model.
-   User mode drivers are now responsible for handling allocation tracking and several new DDIs have been added to enable this.
-   Drivers are given memory budgets and expected to adapt under memory pressure. This allows Universal Windows drivers to function across application platforms.
-   New DDIs have been added for process synchronization and context monitoring.

For more details, see [Driver residency in WDDM 2.0](driver-residency-in-wddm-2-0.md).
 

 





