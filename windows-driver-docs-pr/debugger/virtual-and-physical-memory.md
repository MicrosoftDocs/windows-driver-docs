---
title: Virtual and Physical Memory
description: Virtual and Physical Memory
ms.assetid: 346a46ea-9d44-4e12-8623-d118cd0c7e25
keywords: ["memory access, virtual and physical memory", "virtual memory access", "physical memory access"]
---

# Virtual and Physical Memory


## <span id="ddk_virtual_and_physical_memory_dbx"></span><span id="DDK_VIRTUAL_AND_PHYSICAL_MEMORY_DBX"></span>


The engine provides a number of methods for reading and writing the virtual and physical memory of a target.

### <span id="virtual_memory"></span><span id="VIRTUAL_MEMORY"></span>Virtual Memory

When specifying a location in the virtual memory of a target, the target's virtual address space is used. In user-mode debugging, this is the virtual address space of the current process. In kernel-mode debugging, this is the virtual address space of the implicit process. See [Threads and Processes](controlling-threads-and-processes.md) for more information about the current and implicit process.

The virtual memory (of the target) can be read by using [**ReadVirtual**](https://msdn.microsoft.com/library/windows/hardware/ff554359) and written using [**WriteVirtual**](https://msdn.microsoft.com/library/windows/hardware/ff561468).

Pointers in the target's memory can be read and written by using the convenience methods [**ReadPointersVirtual**](https://msdn.microsoft.com/library/windows/hardware/ff554323) and [**WritePointersVirtual**](https://msdn.microsoft.com/library/windows/hardware/ff561451). These methods will automatically convert between the 64-bit pointers used by the engine and the native pointers used by the target. These methods are useful when requesting memory that contains pointers that will be used for subsequent requests -- for example, a pointer to a string.

The [**SearchVirtual**](https://msdn.microsoft.com/library/windows/hardware/ff554747) and [**SearchVirtual2**](https://msdn.microsoft.com/library/windows/hardware/ff554755) methods can be used to search the target's virtual memory for a pattern of bytes.

The [**FillVirtual**](https://msdn.microsoft.com/library/windows/hardware/ff545395) method can be used to copy a pattern of bytes, multiple times, to the target's virtual memory.

The target's virtual memory can also be read and written in a way that bypasses the debugger engine's virtual memory cache using the methods [**ReadVirtualUncached**](https://msdn.microsoft.com/library/windows/hardware/ff554361) and [**WriteVirtualUncached**](https://msdn.microsoft.com/library/windows/hardware/ff561473). These uncached versions are useful for reading virtual memory that is inherently volatile, such as memory-mapped device areas, without contaminating or invalidating the cache. Uncached memory access should only be used in situations when it is required, as the performance of uncached access can be significantly lower than cached access.

The engine provides some convenience methods to read strings from the target's virtual memory. To read a multibyte string from the target, use [**ReadMultiByteStringVirtual**](https://msdn.microsoft.com/library/windows/hardware/ff554300) and [**ReadMultiByteStringVirtualWide**](https://msdn.microsoft.com/library/windows/hardware/ff554304). To read a Unicode string from the target, use [**ReadUnicodeStringVirtual**](https://msdn.microsoft.com/library/windows/hardware/ff554351) and [**ReadUnicodeStringVirtualWide**](https://msdn.microsoft.com/library/windows/hardware/ff554357).

To find information about a memory location, use [**GetOffsetInformation**](https://msdn.microsoft.com/library/windows/hardware/ff548055). Not all of the virtual address space in the target contains valid memory. To find valid memory within a region, use [**GetValidRegionVirtual**](https://msdn.microsoft.com/library/windows/hardware/ff549471). When manually searching for valid memory in a target, the method [**GetNextDifferentlyValidOffsetVirtual**](https://msdn.microsoft.com/library/windows/hardware/ff547847) will find the next location where the validity may change.

### <span id="physical_memory"></span><span id="PHYSICAL_MEMORY"></span>Physical Memory

The physical memory can only be directly accessed in kernel-mode debugging.

Physical memory on the target can be read by using [**ReadPhysical**](https://msdn.microsoft.com/library/windows/hardware/ff554313) and [**ReadPhysical2**](https://msdn.microsoft.com/library/windows/hardware/ff554311), and written by using [**WritePhysical**](https://msdn.microsoft.com/library/windows/hardware/ff561432) and [**WritePhysical2**](https://msdn.microsoft.com/library/windows/hardware/ff561441).

The [**FillPhysical**](https://msdn.microsoft.com/library/windows/hardware/ff545394) method can be used to copy a pattern of bytes, multiple times, to the target's physical memory.

An address in the target's virtual address space can be translated to a physical address on the target by using the [**VirtualToPhysical**](https://msdn.microsoft.com/library/windows/hardware/ff560335) method. The system's paging structures used to translate a virtual address to a physical address can be found by using [**GetVirtualTranslationPhysicalOffsets**](https://msdn.microsoft.com/library/windows/hardware/ff549498).

### <span id="events"></span><span id="EVENTS"></span>Events

When the virtual or physical memory of the target is changed, the [**IDebugEventCallbacks::ChangeDebuggeeState**](https://msdn.microsoft.com/library/windows/hardware/ff550678) callback method is called.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Virtual%20and%20Physical%20Memory%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




