---
title: Allocation Notification
description: Describes the design of the allocation notification DDI.
keywords:
- allocation notification DDI
- allocation notification, WDDM
ms.date: 08/19/2024
---

# Allocation notification

> [!IMPORTANT]
> Some information relates to a prerelease product that might be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

There are times when certain operations need to be performed on an allocation that's about to undergo a paging eviction or promotion operation. For example, an allocation might be compressed when it's under device access. When that allocation is being evicted (that is, no longer under device access), the driver must first decompress it before the actual eviction. The **DXGK_OPERATION_NOTIFY_ALLOC** paging operation is designed for this purpose. This operation is available starting in Windows 11, version 24H2 (WDDM 3.2).

## How to request allocation notifications

When the system calls [**DxgkDdiCreateAllocation**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createallocation) to create an allocation, the kernel-mode driver (KMD) can set flags in[**DXGK_ALLOCATIONINFOFLAGS2**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgk_allocationinfoflags2) to instruct *Dxgkrnl* to perform the **DXGK_OPERATION_NOTIFY_ALLOC** paging operation. The current notification flags are:

* **NotifyEviction**
* **NotifyIoMmuUnmap**

## DDI changes

### DXGK_OPERATION_NOTIFY_ALLOC paging operation added

* The **DXGK_OPERATION_NOTIFY_ALLOC** paging operation is added to [**DXGK_BUILDPAGINGBUFFER_OPERATION**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_buildpagingbuffer_operation).

* The [**DXGK_BUILDPAGINGBUFFER_NOTIFYALLOC**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgk_buildpagingbuffer_notifyalloc) structure is added for use with the **DXGK_OPERATION_NOTIFY_ALLOC** operation.

### Flags added to DXGK_ALLOCATIONINFOFLAGS2

The following flags are added to [**DXGK_ALLOCATIONINFOFLAGS2**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgk_allocationinfoflags2).

* **NotifyEviction**

  The driver sets the **NotifyEviction** flag in its [**DxgkDdiCreateAllocation**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createallocation) implementation. This flag indicates that *Dxgkrnl* should issue a [**DXGK_OPERATION_NOTIFY_ALLOC NotifyEviction**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_buildpagingbuffer_operation) operation to the driver before evicting an allocation.

  When the flag is specified and the allocation is about to be evicted:

  * *Dxgkrnl* maps the allocation to the paging process's GPU virtual address (VA) space.
  * *Dxgkrnl* calls [**DxgkDdiBuildPagingBuffer**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_buildpagingbuffer) with the **DXGK_OPERATION_NOTIFY_ALLOC** operation and the **NotifyEviction** flag.
  * The driver builds commands in the paging DMA buffer.
  * The paging DMA buffer is submitted for execution in the system context.
  * *Dxgkrnl* unmaps the allocation from the paging process GPU VA space.

  These steps can be executed multiple times if the allocation size is larger than the size of the paging process GPU VA space.

  *Dxgkrnl* sends the notification to the driver only when an allocation is evicted from an aperture segment or from the implicit system memory segment.

* **NotifyIoMmuUnmap**

  The driver sets the **NotifyIoMmuUnmap** flag in its [**DxgkDdiCreateAllocation**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createallocation) function. This flag indicates that *Dxgkrnl* should issue a[**DXGK_OPERATION_NOTIFY_ALLOC NotifyIoMmuUnmap**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_buildpagingbuffer_operation) operation before unmapping the allocation from IOMMU. The driver has the chance to clear internal caches. The driver should ensure that the allocation GPU VA isn't accessed after return from the paging operation.

  When the flag is specified and the allocation is about to be evicted:

  * *Dxgkrnl* maps the allocation to the paging process's GPU VA space.
  * *Dxgkrnl* calls [**DxgkDdiBuildPagingBuffer**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_buildpagingbuffer) with the **DXGK_OPERATION_NOTIFY_ALLOC** operation and the **NotifyIoMmuUnmap** flag.
  * The driver build commands in the paging DMA buffer.
  * The paging DMA buffer is submitted for execution in the system context.
  * *Dxgkrnl* unmaps the allocation from the paging process GPU VA space.

  These steps can be executed multiple times if the allocation size is larger than the size of the paging process GPU VA space.

  *Dxgkrnl* send the notification to the driver only when an allocation is evicted from an aperture segment or from the implicit system memory segment.

### Paging process GPU VA space size

To get the size of the paging process GPU VA space, **DXGKQAITYPE_PAGINGPROCESSGPUVASIZE** is added to the [**DXGK_QUERYADAPTERINFOTYPE**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_queryadapterinfotype) enumeration.

The [**DXGK_OPERATION_NOTIFY_ALLOC NotifyEviction**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_buildpagingbuffer_operation) operation requires the corresponding allocation to be mapped to the paging process GPU VA space. *Dxgkrnl* allocates the GPU VA space for the paging (system) process only when there's a local memory segment or when hardware scheduling is enabled. The size of the GPU VA space is a quarter of the largest local memory segment or the size of the hardware scheduling log buffers, whichever is greater. The resulting GPU VA size could be small to map a full allocation. In this case, the driver needs to specify the size of the paging process GPU VA space.

*Dxgkrnl* calls [**DxgkDdiQueryAdapterInfo**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryadapterinfo) with a [**DXGKARG_QUERYADAPTERINFO**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_queryadapterinfo) structure as follows to get the size of the paging process GPU VA space:

* **Type** is set [**DXGKQAITYPE_PAGINGPROCESSGPUVASIZE**](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_queryadapterinfotype).
* **pInputData** points to a UINT value that specifies the physical adapter index in an LDA configuration. *Dxgkrnl* sets it to zero for non-LDA configurations.
* **InputDataDataSize** is ```sizeof(UINT)```.
* **pOutputData** points to a UINT value in which the driver returns the size of the paging process GPU VA space in megabytes.
* **OutputDataSize** is ```sizeof(UINT)```.

If the driver fails the call or returns a **pOutputData** value of zero, the OS determines the paging process GPU VA size.

If an adapter has a large local memory segment, the driver should return zero to let the OS choose the size of the paging process GPU VA space. The larger the VA space, the more memory is needed for paging process GPU page tables. The page tables are always resident, so the driver shouldn't specify an unnecessary large size for the VA space.

Paging operations (fill, transfer, notify allocation) are done in chunks when an allocation size exceeds the paging process GPU VA space size.
