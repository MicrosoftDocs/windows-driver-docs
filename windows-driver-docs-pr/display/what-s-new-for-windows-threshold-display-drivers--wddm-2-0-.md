---
title: What's new for Windows 10 display drivers (WDDM 2.0)
description: .
ms.assetid: 619175D4-98DA-4B17-8F6F-71B13A31374D
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# What's new for Windows 10 display drivers (WDDM 2.0)


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
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20What's%20new%20for%20Windows%C2%A010%20display%20drivers%20%28WDDM%202.0%29%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




