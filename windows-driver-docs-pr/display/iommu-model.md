---
title: IoMmu Model
description: In the IoMmu model, each process has a single virtual address space that is shared between the CPU and graphics processing unit (GPU) and managed by the OS memory manager.
keywords:
- IoMmu model, WDDM 2.0
- IOMMU, WDDM 2.0
ms.date: 09/20/2024
---

# IoMmu model

This page describes the *IoMmu* model introduced in WDDM 2.0. See [IOMMU-based GPU isolation](iommu-based-gpu-isolation.md) and [IOMMU DMA remapping](iommu-dma-remapping.md) for more recent IOMMU updates.

## Overview

An Input-Output Memory Management Unit (IOMMU) is a hardware component that connects a DMA-capable I/O bus to system memory. It maps device-visible virtual addresses to physical addresses, making it useful in virtualization.

In the WDDM 2.0 IoMmu model, each process has a single virtual address space that is:

* Shared between the CPU and GPU.
* Managed by the OS memory manager.

To access memory, the GPU sends a data request to a compliant IOMMU. The request includes a shared virtual address and a *process address space identifier* (PASID). The IOMMU performs the address translation using the shared page table. This action is illustrated in the following diagram.

:::image type="content" source="images/iommu-model.1.png" alt-text="Diagram that shows IOMMU process address space translation in WDDM 2.0.":::

The kernel-mode display driver (KMD) expresses support for the *IoMmu* model by setting the [**DXGK_VIDMMCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidmmcaps)::**IoMmuSupported** caps. When this flag is set, the video memory manager (VidMm) automatically registers any process using the GPU with the IOMMU and obtains a *PASID* for that process address space. The *PASID* is passed to the driver during device creation.

VidMm maps primary allocations into the aperture segment before being displayed, ensuring that the display controller has physical access to these allocations.

In the IoMmu model, the user-mode display driver (UMD) continues to allocate video memory for the GPU using VidMm's [*Allocate*](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_allocatecb) service. This process allows the UMD to:

* Follow the residency model.
* Support the DirectX resource sharing model.
* Ensure that primary surfaces are visible to the kernel and are mapped into aperture before being displayed.

The UMD entirely manages the first level of translation (*tile resource address* to *shared CPU/GPU address*) in user mode.
