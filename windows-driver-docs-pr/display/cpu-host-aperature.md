---
title: CPU host aperture
description: For 32bit OS discrete graphics processing units (GPUs), which donâ€™t support resizable BAR or when resizing the frame buffer BAR fails, Windows Display Driver Model (WDDM) v2 will offer an alternative mechanism by which a discrete GPU VRAM can be efficiently accessed. For GPUs, which support a programmable BAR address space, a new CPU Host Aperture functionality is introduced in WDDM v2 to abstract that functionality.
ms.assetid: 0E4D01E4-93AF-4205-A360-0CA3470716D2
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# CPU host aperture


For 32bit OS discrete graphics processing units (GPUs), which donâ€™t support resizable BAR or when resizing the frame buffer BAR fails, Windows Display Driver Model (WDDM) v2 will offer an alternative mechanism by which a discrete GPU VRAM can be efficiently accessed. For GPUs, which support a programmable BAR address space, a new CPU Host Aperture functionality is introduced in WDDM v2 to abstract that functionality.

When exposing a CPU host aperture, the kernel mode driver fills out a new [**DXGK\_CPUHOSTAPERTURE**](https://msdn.microsoft.com/library/windows/hardware/dn894624) caps structure for every segment supporting a CPU host aperture. This defines the size of the CPU host aperture, this allows driver to reserve some of the BAR for internal purposes. The page size is the same as the GPU pages of the memory segment.

The kernel mode driver then exposes two new device driver interfaces (DDIs) to manage the BAR address space, in particular [*DxgkDdiMapCpuHostAperture*](https://msdn.microsoft.com/library/windows/hardware/dn906340) and [*DxgkDdiUnmapCpuHostAperture*](https://msdn.microsoft.com/library/windows/hardware/dn906344).

The memory for the page table behind the CPU host aperture is managed by the driver and setup early during driver initialization. Both [*DxgkDdiMapCpuHostAperture*](https://msdn.microsoft.com/library/windows/hardware/dn906340) and [*DxgkDdiUnmapCpuHostAperture*](https://msdn.microsoft.com/library/windows/hardware/dn906344) are expected to be operational immediately after segment enumeration and are used during the video memory manager initialization to map CPU virtual address to the page directory and page table of the system paging process during adapter initialization.

When CPU access to a memory segment is required, the video memory manager reserves pages in the CPU Host Aperture and maps memory segment pages through it. This is illustrated below.

![cpu host aperture segment mapping](images/cpu-host-aperture.1.png)

In the linked display adapter configuration things look similar except for the following.

-   *Default* or *LinkMirrored* allocation are always mapped to GPU0.
-   *LinkInstanced* allocation have a virtual address range of **AllocationSize**\***NumberOfGPUInLink** associated with them with various part of the allocation being mapped to different GPU.

This is illustrated below:
![cpu host aperture segment mapping for linked display adapter configuration](images/cpu-host-aperture.2.png)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20CPU%20host%20aperture%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




