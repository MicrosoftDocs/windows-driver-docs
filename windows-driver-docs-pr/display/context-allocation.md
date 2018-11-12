---
title: Context allocation
description: To allocate memory for the context save area of a context, the kernel mode driver can use context allocations via DxgkCbCreateContextAllocation.
ms.assetid: DAD08E7F-13F9-4648-A24C-DD9FBA6D490F
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Context allocation


To allocate memory for the context save area of a context, the kernel mode driver can use context allocations via [*DxgkCbCreateContextAllocation*](https://msdn.microsoft.com/library/windows/hardware/hh451312). Some new functionality is added to context allocations to make them fit into the new graphics processing unit (GPU) virtual address model.

## <span id="AccessedPhysically"></span><span id="accessedphysically"></span><span id="ACCESSEDPHYSICALLY"></span>AccessedPhysically


A context allocation can specify the **AccessedPhysically** flags to indicate that the allocation should be allocated contiguously in a memory segment or mapped into the aperture if accessed from system memory.

## <span id="Assigning_a_GPU_virtual_address_to_a_context_allocation"></span><span id="assigning_a_gpu_virtual_address_to_a_context_allocation"></span><span id="ASSIGNING_A_GPU_VIRTUAL_ADDRESS_TO_A_CONTEXT_ALLOCATION"></span>Assigning a GPU virtual address to a context allocation


The video memory manager exposes a new [*DxgkCbMapContextAllocation*](https://msdn.microsoft.com/library/windows/hardware/dn906334) service to the kernel mode driver to allocate a GPU virtual address to a context allocation.

Context allocations are mapped into the application GPU virtual address space associated with the specified context.

**Note**  The driver should be careful not to expose privileged information when a context allocation is to be mapped directly to an application GPU virtual address space.

 

These services behave like their user mode counterpart.

## <span id="Updating_the_content_of_a_context_allocation"></span><span id="updating_the_content_of_a_context_allocation"></span><span id="UPDATING_THE_CONTENT_OF_A_CONTEXT_ALLOCATION"></span>Updating the content of a context allocation


It may sometime be necessary for the kernel mode driver to update the content of a context allocation. For example, a privileged (**AccessedPhysically**, no GPU virtual mapping) context allocation may contain a reference to the page directory associated with a particular context. When the kernel mode driver is notified of the page directory relocation by [*DxgkDdiSetRootPageTable*](https://msdn.microsoft.com/library/windows/hardware/dn906342), the kernel mode driver may need to update the content of that context allocation.

For this purpose a new [*DxgkCbUpdateContextAllocation*](https://msdn.microsoft.com/library/windows/hardware/dn906336)device driver interface (DDI) is added. This DDI queues a request to the video memory manager to initiate an update of the context allocation. The context allocation being updated is mapped into the scratch area of the video memory manager paging process, then the driver is called with a new *UpdateContextAllocation* paging operation to do the actual update of the context allocation. The video memory manager returns from *DxgkCbUpdateContextAllocation* after the update is completed.

The kernel mode driver can pass some private driver data between its calls to [*DxgkCbUpdateContextAllocation*](https://msdn.microsoft.com/library/windows/hardware/dn906336) and the resulting *UpdateContextAllocation* paging operation.

 

 





