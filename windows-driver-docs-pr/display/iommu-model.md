---
title: IoMmu model
description: In the IoMmu model each process has a single virtual address space that is shared between the CPU and graphics processing unit (GPU) and is managed by the OS memory manager.
ms.date: 06/24/2022
---

# IoMmu model

This page describes the *IoMmu* model introduced in WDDM 2.0. See [IOMMU-based GPU isolation](iommu-based-gpu-isolation.md) and [IOMMU DMA remapping](iommu-dma-remapping.md) for more recent IOMMU updates.

## Overview

An Input-Output Memory Management Unit (IOMMU) is an MMU component that connects a DMA-capable I/O bus to system memory. It maps device-visible virtual addresses to physical addresses, making it useful in virtualization.

In the WDDM 2.0 IoMmu model, each process has a single virtual address space that is shared between the CPU and GPU and is managed by the OS memory manager.

To access memory, the GPU sends a data request to a compliant IOMMU. The request includes a shared virtual address and a *process address space identifier* (PASID). The IOMMU performs the address translation using the shared page table. This is illustrated in the following diagram.

![iommu process address space translation.](images/iommu-model.1.png)

The kernel-mode driver expresses support for the *IoMmu* model by setting the [**DXGK_VIDMMCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidmmcaps)::**IoMmuSupported** caps. When this flags is set, the video memory manager will automatically register any process using the GPU with the IOMMU and obtain a *PASID* for that process address space. The *PASID* is passed to the driver during device creation.

Primary allocations are mapped by the video memory manager into the aperture segment before being displayed, ensuring that the display controller has physical access to these allocations.

In the IoMmu model, the user-mode driver continues to allocate video memory for the GPU using the video memory manager's [*Allocate*](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_allocatecb) service. This allow the user-mode driver to:

* Follow the residency model.
* Support the Microsoft DirectX resource sharing model.
* Ensure that primary surfaces are visible to the kernel and are mapped into aperture before being displayed.

The first level of translation (*tile resource address* to *shared CPU/GPU address*) is entirely managed in user mode by the user-mode driver.
