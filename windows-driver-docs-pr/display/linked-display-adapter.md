---
title: Linked display adapter
description: Each physical adapter in a linked display adapter (LDA) link can support GpuMmu or IoMmu or both addressing modes independently.
ms.assetid: 28B13BD7-6CC7-47C7-9FA3-BC55C73441DF
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Linked display adapter


Each physical adapter in a linked display adapter (LDA) link can support *GpuMmu* or *IoMmu* or both addressing modes independently.

## <span id="IoMmu_support"></span><span id="iommu_support"></span><span id="IOMMU_SUPPORT"></span>IoMmu support


Each physical adapter in a link can support the *IoMmu* model and/or the *GpuMmu* model.

[*DxgkDdiCreateDevice*](https://msdn.microsoft.com/library/windows/hardware/ff559615) will be called for logical adapters, which support the *IoMmu* model.

## <span id="GpuMmu_support"></span><span id="gpummu_support"></span><span id="GPUMMU_SUPPORT"></span>GpuMmu support


All physical adapters in a link share the same process virtual address space, but each graphics processing unit (GPU) has its own page tables. Generally, content of page tables is different on each GPU.

![linked display adapter memory address segments](images/linked-display-adapter.1.png)

Each physical adapter is allowed to have its own *GpuMmu* capabilities (page table segment, page table update node, virtual address layout, the underlying page table format, size, etc.). The only restriction is that all physical adapters must have the same virtual address size. **GpuMmuCaps.VirtualAddressBitCount** must be the same for all adapters. The driver should clamp the address space size to the smallest of the physical GPUs.

The Microsoft DirectX graphics kernel will now query *GpuMmu* caps for every physical adapter in a link. [*DxgkDdiQueryAdapterInfo*](https://msdn.microsoft.com/library/windows/hardware/ff559746) (**DXGKQAITYPE\_PAGETABLELEVELDESC**) will also be called for each physical adapter.

**InputDataSize** and **pInputData** for [*DxgkDdiQueryAdapterInfo*](https://msdn.microsoft.com/library/windows/hardware/ff559746)(**DXGKQAITYPE\_GPUMMUCAPS**) will point to **DXGK\_GPUMMUCAPSIN**.

**InputDataSize** and **pInputData** for [*DxgkDdiQueryAdapterInfo*](https://msdn.microsoft.com/library/windows/hardware/ff559746)(**DXGKQAITYPE\_PAGETABLELEVELDESC**) will point to **DXGK\_PAGETABLELEVELDESCIN**.

## <span id="related_topics"></span>Related topics


[*DxgkDdiCreateDevice*](https://msdn.microsoft.com/library/windows/hardware/ff559615)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Linked%20display%20adapter%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





