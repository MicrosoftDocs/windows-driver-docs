---
title: IOMMU DMA remapping
description: In the IOMMU model, each process has a single virtual address space that is shared between the CPU and graphics processing unit (GPU) and is managed by the OS memory manager.
ms.date: 08/08/2023
---

# IOMMU DMA remapping

This page describes the IOMMU DMA remapping feature that was introduced in Windows 11 22H2 (WDDM 3.0). See [IOMMU-based GPU isolation](iommu-based-gpu-isolation.md) for information about IOMMU GPU isolation prior to WDDM 3.0.

## Overview

Up until WDDM 3.0, *dxgkrnl* only supported IOMMU isolation through 1:1 physical remapping, meaning the logical pages accessed by the GPU were translated to the same physical page number. IOMMU DMA remapping allows the GPU to access memory through logical addresses that are no longer mapped 1:1. Instead, *dxgkrnl* is able to provide logically contiguous address ranges.

*Dxgkrnl* imposes a restriction on GPUs: GPUs must be able to access all of physical memory in order for the device to start. If the highest visible address of the GPU doesn't exceed the highest physical address that is installed on the system, *dxgkrnl* fails the initialization of the adapter. Upcoming servers and high end workstations can be configured with over 1 TB of memory that crosses the common 40-bit address space limitation of many GPUs. DMA remapping is used as a mechanism to allow GPUs to work in this environment.

At startup time, *dxgkrnl* determines whether logical remapping is necessary by comparing the device's highest accessible physical address to the memory installed on the system. If it's necessary, DMA remapping is used to map a logical address range that is within the GPU's visible bounds to any physical memory on the system. For example, if the GPU has a limit of 1 TB, then *dxgkrnl* allocates logical addresses from [0, 1TB) which can then map to any physical memory on the system through the IOMMU.

## Logical versus physical adapters

*Dxgkrnl* distinguishes between the concept of a logical and physical adapter. A physical adapter represents an individual hardware device that may or may not be linked with other devices in an [LDA chain](linked-display-adapter.md). A logical adapter represents one or more linked physical adapters.

A single IOMMU DMA domain is created per logical adapter and attached to all physical adapters that are linked. Thus, all physical adapters share the same domain and the same view of physical memory.

## Integrated versus discrete GPU support

Because IOMMU DMA remapping offers little value to integrated GPUs that should, by definition, already be designed to access all physical memory in the system, implementing support on integrated parts is optional but recommended.

Discrete GPUs must support IOMMU DMA remapping, which is a requirement for WDDM 3.0 certification.

## DDI changes

The following DDI changes were made to support IOMMU DMA remapping.

### Driver capabilities

Two sets of driver caps are required to support linear remapping:

* The driver must inform *Dxgkrnl* about its physical memory restrictions; that is, about its highest visible physical address via [**DXGKQAITYPE_PHYSICAL_MEMORY_CAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_queryadapterinfotype) and its associated [**DXGK_PHYSICAL_MEMORY_CAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgk_physical_memory_caps) structure.
* The driver must indicate its support for IOMMU linear remapping via [**DXGKQAITYPE_IOMMU_CAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_queryadapterinfotype) and its associated [**DXGK_IOMMU_CAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgk_iommu_caps) structure. By indicating support, the driver is indicating that all of the DDIs described later are supported and used.

Both of these caps must be provided before *Dxgkrnl* starts the device via [**DXGKDDI_START_DEVICE**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_start_device) so that the device can be created and attached to an IOMMU domain before any memory can be accessed. Linear remapping can only be done if the device doesn't reference any existing physical memory.

### Address descriptor lists

To support both physical and logical access modes and switch between the two modes seamlessly at runtime, *Dxgkrnl* provides a [**DXGK_ADL**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgk_adl) structure that describes an address descriptor list (ADL). This data structure is similar to an [**MDL**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_mdl), but describes an array of pages that can be either physical or logical. Because these pages can be logical pages, the addresses described by an ADL can't be mapped to a virtual address for direct CPU access.

### DXGK_OPERATION_MAP_APERTURE_SEGMENT2 operation for DxgkddiBuildpagingbuffer

*VidMm* provides the [**DXGK_OPERATION_MAP_APERTURE_SEGMENT2**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_buildpagingbuffer_operation) paging buffer mode for mapping memory to the aperture segment since the prior version uses an MDL that is incompatible with logical addresses. The [**DxgkddiBuildpagingbuffer**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_buildpagingbuffer) callback of WDDM 3.0 drivers that support logical address remapping receive calls to the **DXGK_OPERATION_MAP_APERTURE_SEGMENT2** mode, and no longer receive calls to the original **DXGK_OPERATION_MAP_APERTURE_SEGMENT** mode.

This operation is required to support logical DMA remapping. It behaves similarly to the original operation, but provides a [**DXGK_ADL**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgk_adl) instead of an [**MDL**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_mdl).

``` syntax
typedef enum _DXGK_BUILDPAGINGBUFFER_OPERATION
{
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_9)
    DXGK_OPERATION_MAP_APERTURE_SEGMENT2 = 17,
#endif //  DXGKDDI_INTERFACE_VERSION
};

// struct _DXGKARG_BUILDPAGINGBUFFER:
struct
{
    HANDLE  hDevice;
    HANDLE  hAllocation;
    UINT    SegmentId;
    SIZE_T  OffsetInPages;
    SIZE_T  NumberOfPages;
    DXGK_ADL Adl;
    DXGK_MAPAPERTUREFLAGS Flags;
    ULONG   AdlOffset;
    PVOID   CpuVisibleAddress;
} MapApertureSegment2;
```

To opt in to the **DXGK_OPERATION_MAP_APERTURE_SEGMENT2** operation, the driver must indicate support for [**MapApertureSegment2**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_buildpagingbuffer) calls in the [memory management caps](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidmmcaps):

``` syntax
typedef struct _DXGK_VIDMMCAPS {
  union {
    struct {
        ...
        UINT MapAperture2Supported : 1;
        ...
    }
    ...
} DXGK_VIDMMCAPS;
```

The [**DXGK_VIDMMCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidmmcaps) memory management caps are part of the [**DXGK_DRIVERCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_drivercaps) data structure. The driver is unable to use DMA remapping (that is, logical address remapping) functionality without this support enabled.

Some drivers might require CPU access to the memory during a [**MapApertureSegment2**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_buildpagingbuffer) call. This functionality is optionally provided via another [**MapApertureSegment2.CpuVisibleAddress**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_buildpagingbuffer) parameter. This address is a kernel-mode virtual address that is valid as long as the allocation is mapped into the aperture segment. That is, this address will be freed immediately after the corresponding **DXGK_OPERATION_UNMAP_APERTURE_SEGMENT** call for the same allocation.

This address might not be required for all allocations, and so a [**MapApertureCpuVisible** flag was added to the allocation flags](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_allocationinfoflags_wddm2_0) to indicate when it's needed.

If **MapApertureCpuVisible** isn't specified, **MapApertureSegment2.CpuVisibleAddress** is NULL for **DXGK_OPERATION_MAP_APERTURE_SEGMENT2** operations.

**MapApertureCpuVisible** is a part of **DxgkDdiBuildPagingBuffer**'s **MapAperatureSegment2** functionality, so the driver must set [**DXGK_VIDMMCAPS MapAperature2Supported**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidmmcaps) to use this field. If **MapAperature2Supported** isn't set but the driver specifies **MapApertureCpuVisible**, the call to [**DxgkDdiCreateAllocation**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createallocation) fails.

Additionally, in order to receive the **DXGK_OPERATION_MAP_APERTURE_SEGMENT2** operation, the driver must set the [**DXGK_ALLOCATIONINFOFLAGS_WDDM2_0 AccessedPhysically**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_allocationinfoflags_wddm2_0) flag. If **AccessedPhysically** isn't set, any allocation that specifies an aperture segment in their supported segment set gets upgraded to the implicit system memory segment, which doesn't receive MAP_APERTURE calls (since there's no aperture ranges to map).

In summary, to properly receive the CPU address of a system memory allocation, the driver must set the following flags/caps:

* **DXGK_DRIVERCAPS::MemoryManagementCaps.MapAperture2Supported** = 1
* **DXGK_ALLOCATIONINFOFLAGS_WDDM2_0::MapApertureCpuVisible** = 1
* **DXGK_ALLOCATIONINFOFLAGS_WDDM2_0::AccessedPhysically** = 1

For **MapApertureSegment2** calls, the ADL is always initialized and passed as contiguous when logical mapping is enabled. The driver must check the ADL flags to determine whether the allocation is contiguous, and behave accordingly.

### Memory Management Services

There are three fundamental requirements for the memory management functions:

1. The ability to manage physical memory. This might include allocation of memory via nonpaged memory functions such as [**MmAllocatePagesforMdl**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmallocatepagesformdl) or [**MmAllocateContiguousMemory**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmallocatecontiguousmemory), and paged memory functions such as [**ZwCreateSection**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatesection) or [**ZwAllocateVirtualMemory**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwallocatevirtualmemory). The ability to express IO space ranges is also required.

2. The ability to map a GPU-visible logical address from the physical memory. This would provide the caller with a list of logical pages (much like the PFN array of an MDL) that the GPU can be programmed to access. Calling these functions would guarantee that the underlying physical pages are locked and not pageable.

3. The ability to map CPU virtual addresses from the physical memory in both user mode and kernel mode, with a specified cache type (Cached vs WriteCombined).

The following table lists the DDIs and associated input structures introduced to describe physical memory allocation and mapping of logical/virtual views. These DDIs are an updated set to replace the prior callbacks provided to drivers for managing IOMMU mappings (*DxgkCbAllocatePagesforMdl*, *DxgkCbAllocateContiguousMemory*, *DxgkCbMapMdlToIoMmu*). For WDDM 3.0 drivers that support logical remapping, these older callback functions are deprecated and can't be used. The driver should instead use the following memory management callback functions.

Callback functions must be called at IRQL <= APC_LEVEL. Starting in WDDM 3.2, drivers that call any of these functions are validated against this requirement and bugcheck if the IRQL is DISPATCH_LEVEL or higher.

| Callback | Associated callback structure |
| -------- | ----------------------------- |
| [**DXGKCB_CREATEPHYSICALMEMORYOBJECT**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_createphysicalmemoryobject) | [**DXGKARGCB_CREATE_PHYSICAL_MEMORY_OBJECT**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgkargcb_create_physical_memory_object) |
| [**DXGKCB_DESTROYPHYSICALMEMORYOBJECT**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_destroyphysicalmemoryobject) | [**DXGKARGCB_DESTROY_PHYSICAL_MEMORY_OBJECT**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgkargcb_destroy_physical_memory_object) |
| [**DXGKCB_MAPPHYSICALMEMORY**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_mapphysicalmemory) | [**DXGKARGCB_MAP_PHYSICAL_MEMORY**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgkargcb_map_physical_memory) |
| [**DXGKCB_UNMAPPHYSICALMEMORY**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_unmapphysicalmemory) | [**DXGKARGCB_UNMAP_PHYSICAL_MEMORY**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgkargcb_unmap_physical_memory) |
| [**DXGKCB_ALLOCATEADL**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_allocateadl) | [**DXGKARGCB_ALLOCATE_ADL**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgkargcb_allocate_adl) |
| [**DXGKCB_FREEADL**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_freeadl) |
| [**DXGKCB_OPENPHYSICALMEMORYOBJECT**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_openphysicalmemoryobject) | [**DXGKARGCB_OPEN_PHYSICAL_MEMORY_OBJECT**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgkargcb_open_physical_memory_object) |
| [**DXGKCB_CLOSEPHYSICALMEMORYOBJECT**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_closephysicalmemoryobject) | [**DXGKARGCB_CLOSE_PHYSICAL_MEMORY_OBJECT**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgkargcb_close_physical_memory_object) |
