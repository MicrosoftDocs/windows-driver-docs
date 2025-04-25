---
title: GPU Virtual Memory in WDDM 2.0
description: This section provides details about GPU virtual addressing starting in WDDM 2.0.
keywords:
- GPU virtual memory, WDDM
- GPU virtual addressing, WDDM
ms.date: 04/24/2025
---

# GPU virtual memory in WDDM 2.0

This article provides details about GPU virtual memory management starting in Windows 10 (WDDM 2.0). It describes why WDDM 2.0 was changed to support GPU virtual addressing and how drivers use it.

## Introduction

Before WDDM 2.0, the device driver interface (DDI) was built such that GPU engines were expected to reference memory through segment physical addresses. As segments were shared across applications and over-committed, resources got relocated through their lifetime and their assigned physical addresses changed. This process required memory references to be tracked inside command buffers through allocation and patch location lists. Those buffers then needed to be patched with the correct physical memory reference before submission to a GPU engine. This tracking and patching was expensive. It essentially imposed a scheduling model where the video memory manager (VidMm) had to inspect every packet before it could be submitted to an engine.

Over time, more hardware vendors moved toward a hardware-based scheduling model. In this model, work is submitted to the GPU directly from user mode and the GPU manages the various queues of work itself. This evolution made it necessary to eliminate the need for VidMm to inspect and patch every command buffer before submission to a GPU engine.

To do so, WDDM supports GPU virtual addressing starting in WDDM 2.0. In this model, each process gets assigned a unique GPU virtual address (GPUVA) space that every GPU context can execute in. An allocation created or opened by a process gets assigned a unique GPUVA within that process's GPU virtual address space. This assigned GPUVA remains constant and unique for the lifetime of the allocation. The user-mode display driver (UMD) is thus able to reference allocations through their GPU virtual address without having to worry about the underlying physical memory changing through its lifetime.

Individual engines of a GPU can operate in either physical or virtual mode:

* In physical mode, the scheduling model remains the same as it is with WDDM v1.x. The UMD continues to generate the allocation and patch location lists. These allocation lists are submitted with a command buffer and are used to patch command buffers to actual physical addresses before submission to an engine.

* In virtual mode, an engine references memory through GPU virtual addresses. The UMD generates command buffers directly from user mode and uses new services to submit those commands to the kernel. The UMD doesn't generate allocation or patch location lists, although it's still responsible for managing the residency of allocations. For more information on driver residency, see [Driver residency in WDDM 2.0](driver-residency-in-wddm-2-0.md).

## GPU memory models

WDDM v2 supports two distinct models for GPU virtual addressing, *GpuMmu* and *IoMmu*. A driver must [opt-in](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidmmcaps) to support either or both of the models. A single GPU node can support both modes simultaneously.

### GpuMmu model

In the *GpuMmu* model, VidMm manages the GPU memory management unit and underlying page tables. VidMm also exposes services to the UMD that allow it to manage GPU virtual address mapping to allocations. GpuMmu implies that the GPU uses GPU page tables to access data. The page tables could point to system memory or local device memory.

For more information, see [GpuMmu model](gpummu-model.md).

### IoMmu model

In the *IoMmu* model, both the CPU and GPU share a common address space and CPU page tables. Only system memory can be accessed in this case, so IoMmu is suitable for integrated GPUs. IoMmu provides a simpler programming model, where both the GPU and CPU can use the same pointer to access memory. There's no need to manage a separate set of page tables in GPU-accessible memory. That said, the IoMmu model can result in degraded performance due to the overhead of address translation and management.

For more information, see [IoMmu model](iommu-model.md).
