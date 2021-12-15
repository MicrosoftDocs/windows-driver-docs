---
title: IOMMU-based GPU isolation
description: In the IOMMU model each process has a single virtual address space that is shared between the CPU and graphics processing unit (GPU) and is managed by the OS memory manager.
ms.date: 07/22/2021
---

# IOMMU model

This page describes the IOMMU-based GPU isolation feature for IOMMU-capable devices, which was introduced in Windows 10 version 1803 (WDDM 2.4).

## Overview

IOMMU-based GPU isolation allows *Dxgkrnl* to restrict access to system memory from the GPU by making use of IOMMU hardware. The OS can provide logical addresses, instead of physical addresses, which can be used to restrict the device’s access of system memory to only the memory it should be able to access by ensuring that memory accesses over PCIe are translated by the IOMMU to valid and accessible physical pages.

If the logical address accessed by the device is not valid, the device will not get access to the physical memory. This prevents a range of exploits that allow an attacker to gain access to physical memory via a compromised hardware device and read the contents of system memory that are not needed for the device’s operation.

Starting in Windows 10 version 1803, this feature is, by default, only enabled for PCs where Windows Defender Application Guard is enabled for Microsoft Edge (i.e. container virtualization). We plan to measure the performance impact of the feature, and if the cost is determined to be low enough, we will investigate the possibility of enabling the feature even on native systems where virtualization is not enabled.

For development purposes, the actual IOMMU remapping functionality is enabled or disabled through the following registry key:

``` registry
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers
DWORD: IOMMUFlags

0x01 Enabled
     * Enables creation of domain and interaction with HAL

0x02 EnableMappings
     * Maps all physical memory to the domain
     * EnabledMappings is only valid if Enabled is also set. Otherwise no action is performed

0x04 EnableAttach
     * Attaches the domain to the device(s)
     * EnableAttach is only valid if EnableMappings is also set. Otherwise no action is performed

0x08 BypassDriverCap
     * Allows IOMMU functionality regardless of support in driver caps. If the driver does not indicate support for the IOMMU and this bit is not set, the enabled bits are ignored.

0x10 AllowFailure
     * Ignore failures in IOMMU enablement and allow adapter creation to succeed anyway.
     * This value cannot override the behavior when created a secure VM, and only applies to forced IOMMU enablement at device startup time using this registry key.
```

If this feature is enabled, the IOMMU is enabled shortly after the adapter starts. All driver allocations made prior to this time will be mapped when it does get enabled.

Additionally, if the velocity staging key 14688597 is set to enabled, the IOMMU is activated when a secure virtual machine is created. For now, this staging key is disabled by default to allow self-hosting without proper IOMMU support.

While enabled, starting a secure virtual machine will fail if the driver does not provide IOMMU support.

There is currently no way to disable the IOMMU after it has been enabled.

## Memory access

*Dxgkrnl* ensures that all memory accessible by the GPU will be remapped through the IOMMU to ensure that this memory is accessible. The physical memory that the GPU needs to access can currently be broken down into four categories:

* Driver specific allocations made through MmAllocateContiguousMemory- or MmAllocatePagesForMdl-style functions (including the SpecifyCache and extended variations) must be mapped to the IOMMU prior to being accessed by the GPU. Instead of calling the *Mm* APIs, *Dxgkrnl* provides callbacks to the kernel-mode driver to allow the allocation and remapping in one step. Any memory intended to be GPU-accessible must go through these callbacks, or the GPU will not be able to access this memory.

* All memory accessed by the GPU during paging operations, or mapped via the GpuMmu must be mapped to the IOMMU. This process is entirely internal to the Video Memory Manager (VidMm), which is a sub-component of *Dxgkrnl*. VidMm handles mapping and unmapping the logical address space any time the GPU is expected to access this memory. This includes mapping the backing store of an allocation for the entire duration during a transfer to or from VRAM or the entire time in which it is mapped to the sysmem or aperture segments, and mapping/unmapping monitored fences.

* During power transitions, the driver might need to save portions of hardware-reserved memory. To handle this, *Dxgkrnl* provides a mechanism for the driver to specify how much memory will be needed up front to store this data. The exact amount of memory required by the driver can change dynamically, but *Dxgkrnl* will take a commit charge on the upper bound at the time the adapter is initialized to ensure that physical pages can be obtained when required. *Dxgkrnl* is responsible for ensuring this memory is locked and mapped to the IOMMU for the transfer during power transitions.

* For any hardware reserved resources, VidMm ensures that the IOMMU resources are correctly mapped by the time the device is attached to the IOMMU. This includes memory reported by memory segments reported with [**PopulatedFromSystemMemory**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_segmentflags). For reserved memory (e.g. firmware/BIOD reserved) that is not exposed via VidMm segments, *Dxgkrnl* will make a[**DXGKDDI_QUERYADAPTERINFO**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryadapterinfo) call to query all reserved memory ranges that the driver will need mapped ahead of time. See [Hardware reserved memory](#hardware-reserved-memory) for details.

## Domain assignment

During initialization of the hardware, *Dxgkrnl* creates a domain for each logical adapter on the system. The domain manages the logical address space and tracks page tables and other necessary data for the mappings. All physical adapters in a single logical adapter will all belong to the same domain. *Dxgkrnl* will track all mapped physical memory through the new allocation callback routines, as well as any memory allocated by VidMm itself.

The domain will be attached to the device the first time a secure virtual machine is created, or shortly after the device is started if the above registry key is used.

## Exclusive access

Some chip sets do not support atomically swapping the logical address domain when there are pending PCI transactions on the bus. To accommodate this, *Dxgkrnl* has two DDIs for exclusive hardware access. These DDIs form a begin/end pairing where *Dxgkrnl* requests that the hardware be completely silent over the bus. *Dxgkrnl* will ensure that any pending work scheduled on the hardware completes, and then enter this exclusive access region. During this time, *Dxgkrnl* will assign the domain to the device. *Dxgkrnl* will not make any requests of the driver or hardware between these calls.
Both DDIs are documented below.

## DDI Changes

The following DDI changes were made to support IOMMU-based GPU isolation:

* The **IoMmuSecureModeSupported** cap was added to [**DXGK_VIDMMCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidmmcaps)
* The [**DXGKQAITYPE_FRAMEBUFFERSAVESIZE**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_queryadapterinfotype) enum value and [**DXGK_FRAMEBUFFERSAVEAREA**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_framebuffersavearea) structure were added
* The [**DXGKQAITYPE_HARDWARERESERVEDRANGES**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_queryadapterinfotype) enum value and [**DXGK_HARDWARERESERVEDRANGE**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_hardwarereservedranges) structure were added
* The [**DXGK_MEMORY_CACHING_TYPE**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_memory_caching_type) was added
* The following [*Dxgkrnl* callbacks](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_dxgkrnl_interface) and callback parameter structures were added:

  | Callback | Associated callback structure |
  | -------- | ----------------------------- |
  | [**DXGKCB_ALLOCATECONTIGUOUSMEMORY**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_allocatecontiguousmemory) | [**DXGKARGCB_ALLOCATECONTIGUOUSMEMORY**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkargcb_allocatecontiguousmemory) |
  | [**DXGKCB_FREECONTIGUOUSMEMORY**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_freecontiguousmemory) | [**DXGKARGCB_FREECONTIGUOUSMEMORY**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkargcb_freecontiguousmemory) |
  | [**DXGKCB_ALLOCATEPAGESFORMDL**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_allocatepagesformdl)   | [**DXGKARGCB_ALLOCATEPAGESFORMDL**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkargcb_allocatepagesformdl) |
  | [**DXGKCB_FREEPAGESFROMMDL**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_freepagesfrommdl)         | [**DXGKARGCB_FREEPAGESFROMMDL**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkargcb_freepagesfrommdl) |
  | [**DXGKCB_MAPMDLTOIOMMU**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_mapmdltoiommu)               | [**DXGKARGCB_MAPMDLTOIOMMU**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkargcb_mapmdltoiommu) |
  | [**DXGKCB_UNMAPMDLFROMIOMMU**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_unmapmdlfromiommu)       | [**DXGKARGCB_UNMAPMDLFROMIOMMU**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkargcb_unmapmdlfromiommu) |
  | [**DXGKCB_PINFRAMEBUFFERFORSAVE**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_pinframebufferforsave) | [**DXGKARGCB_PINFRAMEBUFFERFORSAVE**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkargcb_pinframebufferforsave) |
  | [**DXGKCB_UNPINFRAMEBUFFERFORSAVE**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_unpinframebufferforsave) | [**DXGKARGCB_UNPINFRAMEBUFFERFORSAVE**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkargcb_unpinframebufferforsave) |
  | [**DXGKCB_MAPFRAMEBUFFERPOINTER**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_mapframebufferpointer) | [**DXGKARGCB_MAPFRAMEBUFFERPOINTER**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkargcb_mapframebufferpointer) |
  | [**DXGKCB_UNMAPFRAMEBUFFERPOINTER**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_unmapframebufferpointer) | [**DXGKARGCB_UNMAPFRAMEBUFFERPOINTER**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkargcb_unmapframebufferpointer) |

## Memory allocation and mapping to IOMMU

*Dxgkrnl* provides the first six callbacks in the above table to the kernel-mode driver to allow it to allocate memory and remap it to the IOMMU’s logical address space. These callback functions mimic the routines provided by the *Mm* API interface. They provide the driver with MDLs, or pointers that describe memory that is also mapped through to the IOMMU. These MDLs continue to describe physical pages, but the IOMMU’s logical address space will be mapped in at the same address.

*Dxgkrnl* tracks requests to these callbacks to help ensure there are no leaks by the driver. The allocation callbacks provide an additional handle as part of the output which must be provided back to the respective free callback.

For memory that cannot be allocated through one of the provided allocation callbacks, the [**DXGKCB_MAPMDLTOIOMMU**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_mapmdltoiommu) callback is provided to allow driver-managed MDLs to be tracked and used with the IOMMU. A driver that uses this callback is responsible for ensuring that the lifetime of the MDL exceeds the corresponding unmap call. Otherwise the unmap call has undefined behavior that might lead to compromised security of the pages from the MDL get repurposed by Mm by the time they are unmapped.

Any allocations created through VidMm (e.g. DdiCreateAllocationCb, monitored fences, etc) in system memory are automatically managed by VidMm and the driver does not need to do anything to make these work.

## Frame buffer reservation

For drivers that must save reserved portions of the frame buffer to system memory during power transitions, *Dxgkrnl* will take a commit charge on required memory at initialization time for the adapter. If the driver reports [IOMMU isolation support](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidmmcaps), *Dxgkrnl* will issue a call to [**DXGKDDI_QUERYADAPTERINFO**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryadapterinfo) with the following immediately after querying the physical adapter caps:

* **Type** is [**DXGKQAITYPE_FRAMEBUFFERSAVESIZE**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_queryadapterinfotype)
* The input is of the type UINT, which is the physical adapter index.
* The output is of the type [**DXGK_FRAMEBUFFERSAVEAREA**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_framebuffersavearea), and should be the maximum size required by the driver to save the frame buffer reserve area during power transitions.

*Dxgkrnl* will take a commit charge on the amount specified by the driver to ensure that it can always get physical pages upon request. This is done by creating a unique section object for each physical adapter which specifies a non-zero value for the maximum size.

The maximum size reported by the driver must be a multiple of PAGE_SIZE.

Performing the transfer to and from the frame buffer can be done at a time of the driver’s choice. To aid in the transfer, *Dxgkrnl* provides the last four callbacks in the above table to the kernel-mode driver. These callbacks can be used to map the appropriate portions of the section object that was created when the adapter was initialized.

When calling these four callback functions, the driver must always provide the *hAdapter* for the master/lead device in an LDA chain.

The driver has two options to implement the frame buffer reservation:

1. (Preferred method) The driver should allocate space per physical adapter using the above [**DXGKDDI_QUERYADAPTERINFO**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryadapterinfo) call to specify the amount of storage that is needed per adapter. At the time of the power transition, the driver should save or restore the memory one physical adapter at a time. This memory will be split across multiple section objects, one per physical adapter.

2. Optionally, the driver can save or restore all data into a single shared section object. This can be done by specifying a single large maximum size in the [**DXGKDDI_QUERYADAPTERINFO**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryadapterinfo) call for physical adapter 0, and then a zero value for all other physical adapters. The driver can then pin down the entire section object once for use across all save/restore operations, for all of the physical adapters. This method has the primary drawback that it requires locking a larger amount of memory at once, since it does not support pinning only a subrange of the memory into an MDL. As a result, this operation is more likely to fail under memory pressure. The driver would also be expected to map the pages in the MDL to the GPU using the correct page offsets.

The driver should perform the following tasks to complete a transfer to or from the frame buffer:

* During initialization, the driver should preallocate a small chunk of GPU accessible memory using one of the allocation callback routines. This memory will be used to help ensure forward progress if the entire section object cannot be mapped/locked down at once.

* At the time of the power transition, the driver should first call *Dxgkrnl* to pin down the frame buffer. On success, *Dxgkrnl* will provide the driver with an MDL to locked pages which are mapped to the IOMMU. The driver can then perform a transfer directly to these pages in whatever means is most efficient for the hardware. The driver should then call *Dxgkrnl* to unlock/unmap the memory.

* If *Dxgkrnl* cannot pin down the entire frame buffer at once, the driver must attempt to make forward progress using the preallocated buffer allocated during initialization. In this case, the driver will perform the transfer in small chunks. During each iteration of the transfer (for each chunk), the driver must ask *Dxgkrnl* to provide a mapped range of the section object which they can copy the results into. The driver must then unmap the portion of the section object before the next iteration.

Below is an example pseudocode implementation of the above algorithm.

``` Cpp

#define SMALL_SIZE (PAGE_SIZE)

PMDL PHYSICAL_ADAPTER::m_SmallMdl;
PMDL PHYSICAL_ADAPTER::m_PinnedMdl;

NTSTATUS PHYSICAL_ADAPTER::Init()
{
    DXGKARGCB_ALLOCATEPAGESFORMDL Args = {};
    Args.TotalBytes = SMALL_SIZE;
    
    // Allocate small buffer up front for forward progress transfers
    Status = DxgkCbAllocatePagesForMdl(SMALL_SIZE, &Args);
    m_SmallMdl = Args.pMdl;

    ...
}

NTSTATUS PHYSICAL_ADAPTER::OnPowerDown()
{    
    Status = DxgkCbPinFrameBufferForSave(&m_pPinnedMdl);
    if(!NT_SUCCESS(Status))
    {
        m_pPinnedMdl = NULL;
    }
    
    if(m_pPinnedMdl != NULL)
    {        
        // Normal GPU copy: frame buffer -> m_pPinnedMdl
        GpuCopyFromFrameBuffer(m_pPinnedMdl, Size);
        DxgkCbUnpinFrameBufferForSave(m_pPinnedMdl);
    }
    else
    {
        SIZE_T Offset = 0;
        while(Offset != TotalSize)
        {
            SIZE_T MappedOffset = Offset;
            PVOID pCpuPointer;
            Status = DxgkCbMapFrameBufferPointer(SMALL_SIZE, &MappedOffset, &pCpuPointer);
            if(!NT_SUCCESS(Status))
            {
                // Driver must handle failure here. Even a 4KB mapping may
                // not succeed. The driver should attempt to cancel the
                // transfer and reset the adapter.
            }
            
            GpuCopyFromFrameBuffer(m_pSmallMdl, SMALL_SIZE);
            
            RtlCopyMemory(pCpuPointer + MappedOffset, m_pSmallCpuPointer, SMALL_SIZE);
            
            DxgkCbUnmapFrameBufferPointer(pCpuPointer);
            Offset += SMALL_SIZE;
        }
    }
}

NTSTATUS PHYSICAL_ADAPTER::OnPowerUp()
{
    Status = DxgkCbPinFrameBufferForSave(&m_pPinnedMdl);
    if(!NT_SUCCESS(Status))
    {
        m_pPinnedMdl = NULL;
    }
    
    if(pPinnedMemory != NULL)
    {
        // Normal GPU copy: m_pPinnedMdl -> frame buffer
        GpuCopyToFrameBuffer(m_pPinnedMdl, Size);
        DxgkCbUnpinFrameBufferForSave(m_pPinnedMdl);
    }
    else
    {
        SIZE_T Offset = 0;
        while(Offset != TotalSize)
        {
            SIZE_T MappedOffset = Offset;
            PVOID pCpuPointer;
            Status = DxgkCbMapFrameBufferPointer(SMALL_SIZE, &MappedOffset, &pCpuPointer);
            if(!NT_SUCCESS(Status))
            {
                // Driver must handle failure here. Even a 4KB mapping may
                // not succeed. The driver should attempt to cancel the
                // transfer and reset the adapter.
            }
                        
            RtlCopyMemory(m_pSmallCpuPointer, pCpuPointer + MappedOffset, SMALL_SIZE);
            
            GpuCopyToFrameBuffer(m_pSmallMdl, SMALL_SIZE);

            DxgkCbUnmapFrameBufferPointer(pCpuPointer);
            Offset += SMALL_SIZE;
        }
    }
}
```

## Hardware reserved memory

Hardware reserved memory will be mapped by VidMm before the device is attached to the IOMMU.

Any memory reported to VidMm as a segment with the [**PopulatedFromSystemMemory**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_segmentflags) flag will automatically be handled by VidMm, and will be mapped based on the provided physical address.

For private hardware reserved regions not exposed by segments, VidMm will make a [**DXGKDDI_QUERYADAPTERINFO**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryadapterinfo) call to query the ranges by the driver. The provided ranges must not overlap any regions of memory used by the NTOS memory manager, and VidMm will validate that not such intersections occur. This ensures that the driver cannot accidentally report a region of physical memory that is outside the reserved range, as this would violate the security guarantees of the feature.

The query call will be made once to query the number of ranges that are needed, followed by a second call to populate the array of reserved ranges.

## Testing

If the driver opts in to this feature, a HLK test will scan the driver’s import table to ensure that none of the following *Mm* functions are called:

* MmAllocateContiguousMemory
* MmAllocateContiguousMemorySpecifyCache
* MmFreeContiguousMemory
* MmAllocatePagesForMdl
* MmAllocatePagesForMdlEx
* MmFreePagesFromMdl
* MmProbeAndLockPages

All memory allocation for contiguous memory and MDLs should instead go through *Dxgkrnl*’s callback interface using the functions listed above. The driver should also not lock any memory. *Dxgkrnl* will manage locked pages for the driver. Once the memory is remapped, the logical address of the pages provided to the driver might no longer match the physical addresses.
