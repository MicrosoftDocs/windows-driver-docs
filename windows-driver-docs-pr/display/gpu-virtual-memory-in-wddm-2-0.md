---
title: GPU virtual memory in WDDM 2.0
description: This section provides details about GPU virtual memory, including why the changes were made and how drivers will use it.
ms.assetid: 88A99A31-9B84-4594-8A93-1C2783F7390D
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GPU virtual memory in WDDM 2.0


This section provides details about GPU virtual memory, including why the changes were made and how drivers will use it. This functionality is available starting with Windows 10.

## <span id="Introduction"></span><span id="introduction"></span><span id="INTRODUCTION"></span>Introduction


Under Windows Display Driver Model (WDDM) v1.x, the device driver interface (DDI) is built such that graphics processing unit (GPU) engines are expected to reference memory through segment physical addresses. As segments are shared across applications and over committed, resources gets relocated through their lifetime and their assigned physical addresses change. This leads to the need to track memory references inside command buffers through allocation and patch location lists, and to patch those buffers with the correct physical memory reference before submission to a GPU engine. This tracking and patching is expensive and essentially imposes a scheduling model where the video memory manager has to inspect every packet before it can be submitted to an engine.

As more hardware vendors move toward a hardware based scheduling model, where work is submitted to the GPU directly from user mode and where the GPU manages the various queue of work itself, it is necessary to eliminate the need for the video memory manager to inspect and patch every command buffer before submission to a GPU engine.

To achieve this we are introducing support for GPU virtual addressing in WDDM v2. In this model, each process gets assigned a unique GPU virtual address space in which every GPU context to execute in. An allocation, created or opened by a process, gets assigned a unique GPU virtual address within that process GPU virtual address space that remains constant and unique for the lifetime of the allocation. This allows the user mode driver to reference allocations through their GPU virtual address without having to worry about the underlying physical memory changing through its lifetime.

Individual engines of a GPU can operate in either physical or virtual mode. In the physical mode, the scheduling model remains the same as it is with WDDM v1.x. In the physical mode the user mode driver continues to generate the allocation and patch location lists. They are submitted along a command buffer and are used to patch command buffers to actual physical addresses before submission to an engine.

In the virtual mode, an engine references memory through GPU virtual addresses. In this mode the user mode driver generates command buffers directly from user mode and uses new services to submit those commands to the kernel. In this mode the user mode driver doesnâ€™t generate allocation or patch location lists, although it is still responsible for managing the residency of allocations. For more information on driver residency, see [Driver residency in WDDM 2.0](driver-residency-in-wddm-2-0.md).

## <span id="GPU_memory_models"></span><span id="gpu_memory_models"></span><span id="GPU_MEMORY_MODELS"></span>GPU memory models


WDDM v2 supports two distinct models for GPU virtual addressing, *GpuMmu* and *IoMmu*. A driver must opt-in to support either or both of the models. A single GPU node can support both modes simultaneously.

<span id="GpuMmu_model"></span><span id="gpummu_model"></span><span id="GPUMMU_MODEL"></span>GpuMmu model  
In the *GpuMmu* model, the video memory manager manages the GPU memory management unit and underlying page tables, and exposes services to the user mode driver that allow it to manage GPU virtual address mapping to allocations.

For more information, see [GpuMmu model](gpummu-model.md).

<span id="IoMmu_model"></span><span id="iommu_model"></span><span id="IOMMU_MODEL"></span>IoMmu model  
In the *IoMmu* model, the CPU and GPU share a common address space and page tables.

For more information, see [IoMmu model](iommu-model.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20GPU%20virtual%20memory%20in%20WDDM%202.0%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




