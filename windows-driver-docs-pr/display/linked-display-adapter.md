---
title: Linked display adapter
description: Each physical adapter in a linked display adapter (LDA) link can support GpuMmu or IoMmu or both addressing modes independently.
ms.assetid: 28B13BD7-6CC7-47C7-9FA3-BC55C73441DF
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 






