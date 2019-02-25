---
title: Offer and reclaim changes
description: For Windows Display Driver Model (WDDM) v2, requirements around Offer and Reclaim are being relaxed.
ms.assetid: 1A987708-DE73-4998-B5F9-03A9D502205A
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Offer and reclaim changes


For Windows Display Driver Model (WDDM) v2, requirements around *Offer* and *Reclaim* are being relaxed. User mode drivers are no longer required to use offer and reclaim on internal allocations. Idle/suspended applications will get rid of driver internal resources by using the **Trim**API that was introduced in Microsoft DirectX 11.1.

Offer and reclaim will continue to be supported at the API level and the user mode driver is required to forward application requests to offer or reclaim resources to the kernel. Under WDDM v2, offering allocation is no longer supported through the allocation list and as a result the user mode driver needs to change the way it implements offer and reclaim.

Resources being offered by an application should be offered immediately by the user mode driver, by calling **OfferCb**, if the resources have no reference in the direct memory access (DMA) buffers currently being built across all contexts. If the resources have pending references in the DMA buffer being built, the user mode driver should defer the call to **OfferCb** until after the dependent DMA buffer has been submitted through [*RenderCb*](https://msdn.microsoft.com/library/windows/hardware/ff568923). The graphics kernel will take care of deferring the operation, in a non-blocking way, until it is safe to offer the resource and as such the user mode driver doesn't need to worry about having to defer the call to **OfferCb** until the dependent operation completes on the graphics processing unit (GPU).

Calling reclaim will automatically page in an allocation if it is in the residency requirement list (i.e. the user or driver has requested the allocation to be resident via a [*MakeResidentCb*](https://msdn.microsoft.com/library/windows/hardware/dn906357) call). For [**ReclaimAllocations2Cb**](https://msdn.microsoft.com/library/windows/hardware/dn903528), this operation is asynchronous, and a paging fence is returned and should be handled the same way as fences returned from *MakeResidentCb*. The allocation is guaranteed to be resident and usable on the GPU when the fence is signaled.

Immediately after returning from [**ReclaimAllocationsCb**](https://msdn.microsoft.com/library/windows/hardware/hh451695)/[**ReclaimAllocations2Cb**](https://msdn.microsoft.com/library/windows/hardware/dn903528), the backing store of the allocation is guaranteed to be valid and the allocation may be placed under CPU access via [*Lock2Cb*](https://msdn.microsoft.com/library/windows/hardware/dn914483). The driver does not need to wait on the paging fence to do so.

 

 





