---
title: IOMMU-based GPU isolation
description: IOMMU-based GPU isolation allows Dxgkrnl to restrict access to system memory from the GPU by making use of IOMMU hardware.
ms.date: 03/20/2023
---

# IOMMU-based GPU isolation

This page describes the IOMMU-based GPU isolation feature for IOMMU-capable devices, introduced in Windows 10 version 1803 (WDDM 2.4). See [IOMMU DMA remapping](iommu-dma-remapping.md) for more recent IOMMU updates.

## Overview

IOMMU-based GPU isolation allows *Dxgkrnl* to restrict access to system memory from the GPU by making use of IOMMU hardware. The OS can provide logical addresses instead of physical addresses. These logical addresses can be used to restrict the device’s access to system memory to only the memory it should be able to access. It does so by ensuring that the IOMMU translates memory accesses over PCIe to valid and accessible physical pages.

If the logical address accessed by the device isn't valid, the device can't get access to the physical memory. This restriction prevents a range of exploits that allow an attacker to gain access to physical memory via a compromised hardware device and to read the contents of system memory that aren't needed for the device’s operation.

Starting in Windows 10 version 1803, by default this feature is only enabled for PCs where Windows Defender Application Guard is enabled for Microsoft Edge (that is, container virtualization).

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

If this feature is enabled, the IOMMU is enabled shortly after the adapter starts. All driver allocations made prior to this time are mapped when it does get enabled.

Additionally, if the velocity staging key 14688597 is set as *enabled*, the IOMMU is activated when a secure virtual machine is created. For now, this staging key is disabled by default to allow self-hosting without proper IOMMU support.

While enabled, starting a secure virtual machine fails if the driver doesn't provide IOMMU support.

There's currently no way to disable the IOMMU after it has been enabled.

## Memory access

*Dxgkrnl* ensures that all memory accessible by the GPU is remapped through the IOMMU to ensure that this memory is accessible. The physical memory that the GPU needs to access can currently be broken down into four categories:

* Driver-specific allocations made through MmAllocateContiguousMemory- or MmAllocatePagesForMdl-style functions (including the SpecifyCache and extended variations) must be mapped to the IOMMU prior to GPU accessing them. Instead of calling the *Mm* APIs, *Dxgkrnl* provides callbacks to the kernel-mode driver to allow the allocation and remapping in one step. Any memory intended to be GPU-accessible must go through these callbacks, or the GPU isn't able to access this memory.

* All memory accessed by the GPU during paging operations, or mapped via the GpuMmu must be mapped to the IOMMU. This process is entirely internal to the Video Memory Manager (VidMm), which is a subcomponent of *Dxgkrnl*. VidMm handles mapping and unmapping the logical address space anytime the GPU is expected to access this memory, including:

* Mapping the backing store of an allocation for the entire duration during a transfer to or from VRAM or the entire time that it's mapped to system memory or aperture segments.
* Mapping and unmapping monitored fences.

* During power transitions, the driver might need to save portions of hardware-reserved memory. To handle this situation, *Dxgkrnl* provides a mechanism for the driver to specify how much memory is up front to store this data. The exact amount of memory required by the driver can change dynamically, but *Dxgkrnl* takes a commit charge on the upper bound at the time when the adapter is initialized to ensure that physical pages can be obtained when required. *Dxgkrnl* is responsible for ensuring this memory is locked and mapped to the IOMMU for the transfer during power transitions.

* For any hardware reserved resources, VidMm ensures that it correctly maps the IOMMU resources by the time the device is attached to the IOMMU. This includes memory reported by memory segments reported with [**PopulatedFromSystemMemory**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_segmentflags). For reserved memory (for example, firmware/BIOD reserved) that isn't exposed via VidMm segments, *Dxgkrnl* makes a [**DXGKDDI_QUERYADAPTERINFO**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryadapterinfo) call to query all reserved memory ranges that the driver needs mapped ahead of time. See [Hardware reserved memory](#hardware-reserved-memory) for details.

## Domain assignment

During initialization of the hardware, *Dxgkrnl* creates a domain for each logical adapter on the system. The domain manages the logical address space and tracks page tables and other necessary data for the mappings. All physical adapters in a single logical adapter belong to the same domain. *Dxgkrnl* tracks all mapped physical memory through the new allocation callback routines, and any memory allocated by VidMm itself.

The domain will be attached to the device the first time a secure virtual machine is created, or shortly after the device is started if the above registry key is used.

## Exclusive access

Some chip sets don't support atomically swapping the logical address domain when there are pending PCI transactions on the bus. To accommodate this limitation, *Dxgkrnl* has two DDIs for exclusive hardware access. These DDIs form a begin/end pairing, where *Dxgkrnl* requests that the hardware is silent over the bus. *Dxgkrnl* ensures that any pending work scheduled on the hardware completes, and then enter this exclusive access region. During this time, *Dxgkrnl* assigns the domain to the device. *Dxgkrnl* doesn't make any requests of the driver or hardware between these calls. Both DDIs are documented in the following section.

## DDI Changes

The following DDI changes were made to support IOMMU-based GPU isolation:

* The **IoMmuSecureModeSupported** cap was added to [**DXGK_VIDMMCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidmmcaps)
* The [**DXGKQAITYPE_FRAMEBUFFERSAVESIZE**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_queryadapterinfotype) enum value and [**DXGK_FRAMEBUFFERSAVEAREA**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_framebuffersavearea) structure were added
* The [**DXGKQAITYPE_HARDWARERESERVEDRANGES**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_queryadapterinfotype) enum value and [**DXGK_HARDWARERESERVEDRANGE**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_hardwarereservedranges) structure were added
* The [**DXGK_MEMORY_CACHING_TYPE**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_memory_caching_type) was added
* The following [*Dxgkrnl* callbacks](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_dxgkrnl_interface) and callback parameter structures were added. Callback functions must be called at IRQL <= APC_LEVEL. Starting in WDDM 3.2, drivers that call any of these functions are validated against this requirement and bugcheck if the IRQL is DISPATCH_LEVEL or higher.

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

*Dxgkrnl* provides the first six callbacks in the above table to the kernel-mode driver to allow it to allocate memory and remap it to the IOMMU’s logical address space. These callback functions mimic the routines provided by the *Mm* API interface. They provide the driver with MDLs, or pointers that describe memory that is also mapped through to the IOMMU. These MDLs continue to describe physical pages, but the IOMMU’s logical address space is mapped in at the same address.

*Dxgkrnl* tracks requests to these callbacks to help ensure there are no leaks by the driver. The allocation callbacks provide an additional handle as part of the output that must be provided back to the respective free callback.

For memory that can't be allocated through one of the provided allocation callbacks, the [**DXGKCB_MAPMDLTOIOMMU**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_mapmdltoiommu) callback is provided to allow driver-managed MDLs to be tracked and used with the IOMMU. A driver that uses this callback is responsible for ensuring that the lifetime of the MDL exceeds the corresponding unmap call. Otherwise the unmap call has undefined behavior that might lead to compromised security of the pages from the MDL that get repurposed by Mm by the time they're unmapped.

VidMm automatically manages any allocations it creates (for example, DdiCreateAllocationCb, monitored fences, etc.) in system memory. The driver doesn't need to do anything to make these allocations work.

## Frame buffer reservation

For drivers that must save reserved portions of the frame buffer to system memory during power transitions, *Dxgkrnl* takes a commit charge on required memory when the adapter is initialized. If the driver reports [IOMMU isolation support](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidmmcaps), *Dxgkrnl* will issue a call to [**DXGKDDI_QUERYADAPTERINFO**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryadapterinfo) with the following immediately after querying the physical adapter caps:

* **Type** is [**DXGKQAITYPE_FRAMEBUFFERSAVESIZE**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_queryadapterinfotype)
* The input is of the type UINT, which is the physical adapter index.
* The output is of the type [**DXGK_FRAMEBUFFERSAVEAREA**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_framebuffersavearea), and should be the maximum size required by the driver to save the frame buffer reserve area during power transitions.

*Dxgkrnl* takes a commit charge on the amount specified by the driver to ensure that it can always get physical pages upon request. This action is done by creating a unique section object for each physical adapter that specifies a nonzero value for the maximum size.

The maximum size reported by the driver must be a multiple of PAGE_SIZE.

Performing the transfer to and from the frame buffer can be done at a time of the driver’s choice. To aid in the transfer, *Dxgkrnl* provides the last four callbacks in the above table to the kernel-mode driver. These callbacks can be used to map the appropriate portions of the section object that was created when the adapter was initialized.

The driver must always provide the *hAdapter* for the master/lead device in an LDA chain when it calls these four callback functions.

The driver has two options to implement the frame buffer reservation:

1. (Preferred method) The driver should allocate space per physical adapter using the above [**DXGKDDI_QUERYADAPTERINFO**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryadapterinfo) call to specify the amount of storage that is needed per adapter. At the time of the power transition, the driver should save or restore the memory one physical adapter at a time. This memory is split across multiple section objects, one per physical adapter.

2. Optionally, the driver can save or restore all data into a single shared section object. This action can be done by specifying a single large maximum size in the [**DXGKDDI_QUERYADAPTERINFO**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryadapterinfo) call for physical adapter 0, and then a zero value for all other physical adapters. The driver can then pin down the entire section object once for use across all save/restore operations, for all of the physical adapters. This method has the primary drawback that it requires locking a larger amount of memory at once, since it doesn't support pinning only a subrange of the memory into an MDL. As a result, this operation is more likely to fail under memory pressure. The driver would also be expected to map the pages in the MDL to the GPU using the correct page offsets.

The driver should perform the following tasks to complete a transfer to or from the frame buffer:

* During initialization, the driver should preallocate a small chunk of GPU accessible memory using one of the allocation callback routines. This memory is used to help ensure forward progress if the entire section object can't be mapped/locked down at once.

* At the time of the power transition, the driver should first call *Dxgkrnl* to pin down the frame buffer. On success, *Dxgkrnl* provides the driver with an MDL to locked pages that are mapped to the IOMMU. The driver can then perform a transfer directly to these pages in whatever means is most efficient for the hardware. The driver should then call *Dxgkrnl* to unlock/unmap the memory.

* If *Dxgkrnl* can't pin down the entire frame buffer at once, the driver must attempt to make forward progress by using the preallocated buffer allocated during initialization. In this case, the driver performs the transfer in small chunks. During each iteration of the transfer (for each chunk), the driver must ask *Dxgkrnl* to provide a mapped range of the section object that they can copy the results into. The driver must then unmap the portion of the section object before the next iteration.

The following pseudocode is an example implementation of this algorithm.

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

VidMm maps hardware reserved memory before the device is attached to the IOMMU.

VidMm automatically handles any memory reported as a segment with the [**PopulatedFromSystemMemory**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_segmentflags) flag. VidMm maps this memory based on the provided physical address.

For private hardware reserved regions not exposed by segments, VidMm makes a [**DXGKDDI_QUERYADAPTERINFO**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryadapterinfo) call to query the ranges by the driver. The provided ranges must not overlap any regions of memory used by the NTOS memory manager; VidMm validates that no such intersections occur. This validation ensures that the driver can't accidentally report a region of physical memory that is outside the reserved range, which would violate the security guarantees of the feature.

The query call is made one time to query the number of needed ranges, and is followed by a second call to populate the array of reserved ranges.

## Testing

If the driver opts in to this feature, an HLK test scans the driver’s import table to ensure that none of the following *Mm* functions are called:

* MmAllocateContiguousMemory
* MmAllocateContiguousMemorySpecifyCache
* MmFreeContiguousMemory
* MmAllocatePagesForMdl
* MmAllocatePagesForMdlEx
* MmFreePagesFromMdl
* MmProbeAndLockPages

All memory allocation for contiguous memory and MDLs should instead go through *Dxgkrnl*’s callback interface using the listed functions. The driver should also not lock any memory. *Dxgkrnl* manages locked pages for the driver. Once the memory is remapped, the logical address of the pages provided to the driver might no longer match the physical addresses.
