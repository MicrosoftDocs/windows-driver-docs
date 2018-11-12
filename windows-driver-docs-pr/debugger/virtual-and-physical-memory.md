---
title: Virtual and Physical Memory
description: Virtual and Physical Memory
ms.assetid: 346a46ea-9d44-4e12-8623-d118cd0c7e25
keywords: ["memory access, virtual and physical memory", "virtual memory access", "physical memory access"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
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

 

 





