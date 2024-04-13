---
title: Virtual and Physical Memory
description: Virtual and Physical Memory
keywords: ["memory access, virtual and physical memory", "virtual memory access", "physical memory access"]
ms.date: 05/23/2017
---

# Virtual and Physical Memory


## <span id="ddk_virtual_and_physical_memory_dbx"></span><span id="DDK_VIRTUAL_AND_PHYSICAL_MEMORY_DBX"></span>


The engine provides a number of methods for reading and writing the virtual and physical memory of a target.

### <span id="virtual_memory"></span><span id="VIRTUAL_MEMORY"></span>Virtual Memory

When specifying a location in the virtual memory of a target, the target's virtual address space is used. In user-mode debugging, this is the virtual address space of the current process. In kernel-mode debugging, this is the virtual address space of the implicit process. See [Threads and Processes](controlling-threads-and-processes.md) for more information about the current and implicit process.

The virtual memory (of the target) can be read by using [**ReadVirtual**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugdataspaces4-readvirtual) and written using [**WriteVirtual**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugdataspaces4-writevirtual).

Pointers in the target's memory can be read and written by using the convenience methods [**ReadPointersVirtual**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugdataspaces4-readpointersvirtual) and [**WritePointersVirtual**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugdataspaces4-writepointersvirtual). These methods will automatically convert between the 64-bit pointers used by the engine and the native pointers used by the target. These methods are useful when requesting memory that contains pointers that will be used for subsequent requests -- for example, a pointer to a string.

The [**SearchVirtual**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugdataspaces4-searchvirtual) and [**SearchVirtual2**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugdataspaces4-searchvirtual2) methods can be used to search the target's virtual memory for a pattern of bytes.

The [**FillVirtual**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugdataspaces4-fillvirtual) method can be used to copy a pattern of bytes, multiple times, to the target's virtual memory.

The target's virtual memory can also be read and written in a way that bypasses the debugger engine's virtual memory cache using the methods [**ReadVirtualUncached**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugdataspaces4-readvirtualuncached) and [**WriteVirtualUncached**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugdataspaces4-writevirtualuncached). These uncached versions are useful for reading virtual memory that is inherently volatile, such as memory-mapped device areas, without contaminating or invalidating the cache. Uncached memory access should only be used in situations when it is required, as the performance of uncached access can be significantly lower than cached access.

The engine provides some convenience methods to read strings from the target's virtual memory. To read a multibyte string from the target, use [**ReadMultiByteStringVirtual**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugdataspaces4-readmultibytestringvirtual) and [**ReadMultiByteStringVirtualWide**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugdataspaces4-readmultibytestringvirtualwide). To read a Unicode string from the target, use [**ReadUnicodeStringVirtual**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugdataspaces4-readunicodestringvirtual) and [**ReadUnicodeStringVirtualWide**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugdataspaces4-readunicodestringvirtualwide).

To find information about a memory location, use [**GetOffsetInformation**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugdataspaces4-getoffsetinformation). Not all of the virtual address space in the target contains valid memory. To find valid memory within a region, use [**GetValidRegionVirtual**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugdataspaces4-getvalidregionvirtual). When manually searching for valid memory in a target, the method [**GetNextDifferentlyValidOffsetVirtual**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugdataspaces4-getnextdifferentlyvalidoffsetvirtual) will find the next location where the validity may change.

### <span id="physical_memory"></span><span id="PHYSICAL_MEMORY"></span>Physical Memory

The physical memory can only be directly accessed in kernel-mode debugging.

Physical memory on the target can be read by using [**ReadPhysical**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugdataspaces4-readphysical) and [**ReadPhysical2**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugdataspaces4-readphysical2), and written by using [**WritePhysical**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-writephysical) and [**WritePhysical2**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugdataspaces4-writephysical2).

The [**FillPhysical**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugdataspaces4-fillphysical) method can be used to copy a pattern of bytes, multiple times, to the target's physical memory.

An address in the target's virtual address space can be translated to a physical address on the target by using the [**VirtualToPhysical**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugdataspaces4-virtualtophysical) method. The system's paging structures used to translate a virtual address to a physical address can be found by using [**GetVirtualTranslationPhysicalOffsets**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugdataspaces4-getvirtualtranslationphysicaloffsets).

### <span id="events"></span><span id="EVENTS"></span>Events

When the virtual or physical memory of the target is changed, the [**IDebugEventCallbacks::ChangeDebuggeeState**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugeventcallbacks-changedebuggeestate) callback method is called.

 

