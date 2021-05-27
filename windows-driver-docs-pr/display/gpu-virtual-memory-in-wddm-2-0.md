---
title: GPU virtual memory in WDDM 2.0
description: This section provides details about GPU virtual memory, including why the changes were made and how drivers will use it.
ms.date: 06/20/2019
ms.localizationpriority: medium
---

# GPU virtual memory in WDDM 2.0

This section provides details about GPU virtual memory, including why the changes were made and how drivers will use it. This functionality is available starting with Windows 10.

## Introduction

Under Windows Display Driver Model (WDDM) v1.x, the device driver interface (DDI) is built such that graphics processing unit (GPU) engines are expected to reference memory through segment physical addresses. As segments are shared across applications and over committed, resources get relocated through their lifetime and their assigned physical addresses change. This leads to the need to track memory references inside command buffers through allocation and patch location lists, and to patch those buffers with the correct physical memory reference before submission to a GPU engine. This tracking and patching is expensive and essentially imposes a scheduling model where the video memory manager has to inspect every packet before it can be submitted to an engine.

As more hardware vendors move toward a hardware based scheduling model, where work is submitted to the GPU directly from user mode and where the GPU manages the various queue of work itself, it is necessary to eliminate the need for the video memory manager to inspect and patch every command buffer before submission to a GPU engine.

To achieve this, WDDM v2 supports GPU virtual addressing. In this model, each process gets assigned a unique GPU virtual address space in which every GPU context to execute in. An allocation, created or opened by a process, gets assigned a unique GPU virtual address within that process GPU virtual address space that remains constant and unique for the lifetime of the allocation. This allows the user mode driver to reference allocations through their GPU virtual address without having to worry about the underlying physical memory changing through its lifetime.

Individual engines of a GPU can operate in either physical or virtual mode. In the physical mode, the scheduling model remains the same as it is with WDDM v1.x. In the physical mode the user mode driver continues to generate the allocation and patch location lists. They are submitted along a command buffer and are used to patch command buffers to actual physical addresses before submission to an engine.

In the virtual mode, an engine references memory through GPU virtual addresses. In this mode the user mode driver generates command buffers directly from user mode and uses new services to submit those commands to the kernel. In this mode the user mode driver doesn’t generate allocation or patch location lists, although it is still responsible for managing the residency of allocations. For more information on driver residency, see [Driver residency in WDDM 2.0](driver-residency-in-wddm-2-0.md).

## GPU memory models

WDDM v2 supports two distinct models for GPU virtual addressing, *GpuMmu* and *IoMmu*. A driver must opt-in to support either or both of the models. A single GPU node can support both modes simultaneously.

### GpuMmu model

In the *GpuMmu* model, the video memory manager manages the GPU memory management unit and underlying page tables, and exposes services to the user mode driver that allow it to manage GPU virtual address mapping to allocations. GpuMmu implies that GPU page tables are used by the GPU to access data. The page tables could point to system memory or local device memory.

For more information, see [GpuMmu model](gpummu-model.md).

### IoMmu model

In the *IoMmu* model, the CPU and GPU share a common address space and CPU page tables. Only system memory can be accessed in this case, so IoMmu is suitable for integrated GPUs. IoMmu provides a simpler programming model, where the same pointer can be used by the GPU and CPU to access memory. There is no need to manage a separate set of page tables in GPU-accessible memory. That said, the IoMmu model can result in degraded performance due to the overhead of address translation and management.

For more information, see [IoMmu model](iommu-model.md).
