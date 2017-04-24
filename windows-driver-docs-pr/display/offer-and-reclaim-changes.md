---
title: Offer and reclaim changes
description: For Windows Display Driver Model (WDDM) v2, requirements around Offer and Reclaim are being relaxed.
ms.assetid: 1A987708-DE73-4998-B5F9-03A9D502205A
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Offer and reclaim changes


For Windows Display Driver Model (WDDM) v2, requirements around *Offer* and *Reclaim* are being relaxed. User mode drivers are no longer required to use offer and reclaim on internal allocations. Idle/suspended applications will get rid of driver internal resources by using the **Trim**API that was introduced in Microsoft DirectX 11.1.

Offer and reclaim will continue to be supported at the API level and the user mode driver is required to forward application requests to offer or reclaim resources to the kernel. Under WDDM v2, offering allocation is no longer supported through the allocation list and as a result the user mode driver needs to change the way it implements offer and reclaim.

Resources being offered by an application should be offered immediately by the user mode driver, by calling **OfferCb**, if the resources have no reference in the direct memory access (DMA) buffers currently being built across all contexts. If the resources have pending references in the DMA buffer being built, the user mode driver should defer the call to **OfferCb** until after the dependent DMA buffer has been submitted through [*RenderCb*](https://msdn.microsoft.com/library/windows/hardware/ff568923). The graphics kernel will take care of deferring the operation, in a non-blocking way, until it is safe to offer the resource and as such the user mode driver doesnâ€™t need to worry about having to defer the call to **OfferCb** until the dependent operation completes on the graphics processing unit (GPU).

Calling reclaim will automatically page in an allocation if it is in the residency requirement list (i.e. the user or driver has requested the allocation to be resident via a [*MakeResidentCb*](https://msdn.microsoft.com/library/windows/hardware/dn906357) call). For [**ReclaimAllocations2Cb**](https://msdn.microsoft.com/library/windows/hardware/dn903528), this operation is asynchronous, and a paging fence is returned and should be handled the same way as fences returned from *MakeResidentCb*. The allocation is guaranteed to be resident and usable on the GPU when the fence is signaled.

Immediately after returning from [**ReclaimAllocationsCb**](https://msdn.microsoft.com/library/windows/hardware/hh451695)/[**ReclaimAllocations2Cb**](https://msdn.microsoft.com/library/windows/hardware/dn903528), the backing store of the allocation is guaranteed to be valid and the allocation may be placed under CPU access via [*Lock2Cb*](https://msdn.microsoft.com/library/windows/hardware/dn914483). The driver does not need to wait on the paging fence to do so.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Offer%20and%20reclaim%20changes%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




