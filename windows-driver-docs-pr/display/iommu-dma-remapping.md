---
title: IOMMU DMA remapping
description: In the IOMMU model each process has a single virtual address space that is shared between the CPU and graphics processing unit (GPU) and is managed by the OS memory manager.
ms.date: 06/16/2022
---

# IOMMU DMA remapping

This page describes the IOMMU DMA remapping feature that was introduced in Windows 11 22H2 (WDDM 3.0). See [IOMMU DMA remapping](iommu-dma-remapping.md) for past reference.

## Overview

Up until WDDM 3.0, *dxgkrnl* only supported IOMMU isolation through 1:1 physical remapping, meaning the logical pages accessed by the GPU were translated to the same physical page number. IOMMU DMA remapping allows the GPU to access memory through logical addresses which are no longer mapped 1:1; that is, *dxgkrnl* is able to provide logically contiguous address ranges.

*Dxgkrnl* requires that GPUs are able to access all of physical memory in order for the device to start. If the highest visible address of the GPU does not exceed the highest physical address that is installed on the system, *dxgkrnl* will fail the initialization of the adapter. Upcoming servers and high end workstations can be configured with over 1TB of memory which crosses the common 40-bit address space limitation of many GPUs. DMA remapping will be used as a mechanism to allow GPUs to work in this environment.

At startup time, *dxgkrnl* will determine if logical remapping is necessary by comparing the device's highest accessible physical address to the memory installed on the system. If necessary, DMA remapping will be used to map a logical address range that is within the GPU's visible bounds to any physical memory on the system. For example, if the GPU has a limit of 1TB, then *dxgkrnl* will allocate logical addresses from [0, 1TB) which can then map to any physical memory on the system through the IOMMU.

## Logical versus physical adapters

*Dxgkrnl* distinguishes between the concept of a logical and physical adapter. A physical adapter represents an individual hardware device that may or may not be linked with other devices in an [LDA chain](linked-display-adapter.md). A logical adapter represents one or more linked physical adapters.

A single IOMMU DMA domain is created per logical adapter and attached to all physical adapters that are linked. This means all physical adapters share the same domain and the same view of physical memory.

## Integrated versus discrete GPU support

Because IOMMU DMA remapping offers little value to integrated GPUs which should, by definition, already be designed to access all physical memory in the system, implementing support on integrated parts is optional but recommended.

Discrete GPUs must support IOMMU DMA remapping, which is a requirement for WDDM 3.0 certification.

## DDI changes

The following DDI changes were made to support IOMMU DMA remapping.

### Driver caps

Two [**DXGK_QUERYADAPTERINFOTYPE**] driver caps are required to support linear remapping:

* The driver must inform *Dxgkrnl* about its physical memory restrictions; that is, about its highest visible physical address.
* The driver must indicate its support for IOMMU linear remapping. By indicating support, the driver is indicating that all of the DDIs described below are supported and used.

Both of these caps must be provided before *Dxgkrnl* starts the device via [**DXGKDDI_START_DEVICE**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_start_device) so that the device can be created and attached to an IOMMU domain before any memory can be accessed. Linear remapping can only be done if no existing physical memory is referenced by the device.

``` C++

typedef enum _DXGK_QUERYADAPTERINFOTYPE
{
    ...
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_9)
    DXGKQAITYPE_PHYSICAL_MEMORY_CAPS = 34,
    DXGKQAITYPE_IOMMU_CAPS           = 35,
#endif //  DXGKDDI_INTERFACE_VERSION
} DXGK_QUERYADAPTERINFOTYPE;

typedef struct _DXGK_PHYSICAL_ADAPTER_CAPS
{
    PHYSICAL_ADDRESS HighestVisibleAddress;
} DXGK_PHYSICAL_ADAPTER_CAPS;

typedef struct _DXGK_IOMMU_CAPS
{
    union
    {
        struct
        {
            UINT32 IommuIsolationSupported  :  1;
            UINT32 IommuIsolationRequired   :  1;
            UINT32 DmaRemappingSupported    :  1;
            UINT32 Reserved                 : 29;
        };
        UINT32 Value;
    };
} DXGK_IOMMU_CAPS;
```



To support logical remapping, DDIs were added to provide better control over physical memory that can be mapped to the GPU and/or CPU, and to ensure that any DDIs consuming memory addresses are updated to understand that these are logical.















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
