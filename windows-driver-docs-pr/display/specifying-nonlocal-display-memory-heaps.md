---
title: Specifying Nonlocal Display Memory Heaps
description: Specifying Nonlocal Display Memory Heaps
ms.assetid: 4320b6e7-81ef-4bb4-bda8-680467b6421f
keywords:
- heaps WDK DirectDraw
- display memory WDK DirectDraw , heaps
- nonlocal display memory WDK DirectDraw , heaps
- AGP WDK DirectDraw , heaps
- drawing AGP support WDK DirectDraw , heaps
- DirectDraw AGP support WDK Windows 2000 display , heaps
- memory WDK DirectDraw AGP , heaps
- linear heaps WDK DirectDraw
- physical heaps WDK DirectDraw
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Specifying Nonlocal Display Memory Heaps


## <span id="ddk_specifying_nonlocal_display_memory_heaps_gg"></span><span id="DDK_SPECIFYING_NONLOCAL_DISPLAY_MEMORY_HEAPS_GG"></span>


A DirectDraw driver controls how much AGP memory is available and to which surfaces by returning heaps in the [**DD\_HALINFO**](https://msdn.microsoft.com/library/windows/hardware/ff551627) structure that is passed back to DirectDraw. The driver identifies nonlocal heaps by specifying the VIDMEM\_ISNONLOCAL flag in the **dwFlags** member of the [**VIDEOMEMORY**](https://msdn.microsoft.com/library/windows/hardware/ff570171) data structure that describes the heap. Furthermore, a driver can choose to enable combining of memory writes on a nonlocal heap by specifying the VIDMEM\_ISWC flag in addition to VIDMEM\_ISNONLOCAL.

It is the responsibility of an AGP-compatible DirectDraw driver to describe to DirectDraw the size (linear or rectangular), attributes (write combining), and surface types the heap should not and cannot be used for. However, it is not the driver's responsibility to actually reserve address space for the heap or commit memory to it. This is handled by DirectDraw on the driver's behalf. DirectDraw hides the details of managing AGP memory from the driver.

When specifying a nonlocal display memory heap, the start address specified by the driver has no meaning. The start address, both graphic address remapping table (GART) linear and physical, of a nonlocal heap is determined by the operating system when DirectDraw requests that a heap be created. Therefore, the driver can return any value for the start address. For a rectangular heap, this start address is ignored by DirectDraw. The specified width and height are all that DirectDraw needs to determine memory requirements. For a linear heap, the start address has a meaning, but only to the extent that it is used to compute the size of the heap.

DirectDraw determines the size of a linear heap by (fpEnd - fpStart) + 1 (note that the specified end address is the last byte in the heap, not the first byte after the end of the heap). As such, any start address can be specified as long as when DirectDraw subtracts that address from the end address and adds 1, the result is the maximum size of the heap.

Although physical memory is only committed to the AGP heap when it is needed (that is, as surfaces are allocated), it is important not to specify very large nonlocal heaps. Such heaps consume shared address space and other important resources even before physical memory is committed.

It is also important to note that DirectDraw and the Windows operating system impose policy limits on the amount of AGP memory that can be committed at any given time. This is necessary to prevent resource starvation for the rest of the system. Therefore, it is quite possible for a request for a nonlocal display memory surface to fail even though the nonlocal heaps are not fully committed.

When DirectDraw has determined the correct addresses (linear and physical) of the heap, it stores them in its heap descriptors. DirectDraw also provides a mechanism to notify a driver at initialization time of these addresses. How this is done is platform specific:

-   On Microsoft Windows 2000 and later, this is done with a [**DdGetDriverInfo**](https://msdn.microsoft.com/library/windows/hardware/ff549404) call using the GUID\_UpdateNonLocalHeap GUID. When this GUID is passed to *DDGetDriverInfo*, the heap data is passed in the [**DD\_UPDATENONLOCALHEAPDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551748) data structure.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Specifying%20Nonlocal%20Display%20Memory%20Heaps%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




