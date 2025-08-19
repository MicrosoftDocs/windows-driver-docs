---
title: GpuMmu Model
description: In the GpuMmu model, the graphics processing unit (GPU) has its own memory management unit (MMU) which translates per-process GPU virtual addresses to physical addresses.
keywords:
- WDDM 2.0 , GpuMmu model , GPU , memory management unit , GPU memory management
ms.date: 12/18/2024
ms.topic: concept-article
---

# GpuMmu model

This article describes the *GpuMmu* model, which was introduced in Windows 10 (WDDM 2.0).

In the GpuMmu model, the GPU has its own memory management unit (MMU) that translates per-process GPU virtual addresses to physical addresses.

Each process has separate CPU and GPU virtual address spaces that use distinct page tables. The video memory manager (*VidMm*) manages the GPU virtual address space of all processes. *VidMm* is also responsible for allocating, growing, updating, ensuring residency, and freeing page tables. The hardware format of the page tables used by the GPU MMU is unknown to *VidMm* and is abstracted through device driver interfaces (DDIs). The abstraction supports a multilevel level translation, including a fixed size page table and a resizable root page table.

Although *VidMm* is responsible for managing the GPU virtual address space and its underlying page tables, *VidMm* doesn't automatically assign GPU virtual addresses to allocations. This responsibility falls on the user-mode driver (UMD).

*VidMm* offers two main services to the UMD:

* Memory allocation and deallocation. The UMD can allocate video memory through the existing [*Allocate*](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_allocatecb) callback and free that memory through the existing [*Deallocate*](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_deallocatecb) callback. *Allocate* returns a handle to a *VidMm* allocation to the UMD. A GPU engine can operate on this handle. Such an allocation refers specifically to physical video memory, which a GPU engine can access and process via an allocation list.

* GPU virtual address space management. For engines running in the virtual mode, a GPU virtual address needs to be explicitly assigned to an allocation before it can be accessed virtually. For this purpose, *VidMm* offers the UMD services to reserve or free GPU virtual addresses and to map specific allocation ranges into the GPU virtual address space of a process. These services are flexible and allow the UMD fine grain control over a process GPU virtual address space. The UMD can decide to either assign a specific GPU virtual address to an allocation, or let *VidMm* automatically pick an available one, possibly specifying some min and max GPU virtual address constraints. A single allocation can have multiple GPU virtual address mappings associated with it and services are provided to the UMD to implement the *Tile Resource contract*.

Similarly, in a linked display adapter configuration, the UMD can explicitly map GPU virtual addresses to specific allocation instances. For each mapping, UMD can choose whether the mapping should be to self or to a specific peer GPU. In this model, the CPU and GPU virtual addresses assigned to an allocation are independent. A UMD can decide to keep them the same in both address spaces or keep them independent.

GPU virtual addresses are managed logically at a fixed 4-KB page granularity through the DDI interface. GPU virtual addresses can reference allocations that are resident in either a memory segment or system memory. System memory is managed at 4-KB physical granularity while memory segments are managed at either 4 KB or 64 KB at the driver's choice. All *VidMm* allocations are aligned and sized to be a multiple of the page size chosen by the driver.

Access to an invalid range of GPU virtual addresses results in an access violation and termination of the context and/or device that caused the access fault. To recover from such a fault, *VidMm* initiates an engine reset which gets promoted to an adapter wide timeout detection recovery (TDR) if unsuccessful.

The *GpuMmu* model is illustrated in the following diagram:

:::image type="content" source="images/gpummu-model.1.png" alt-text="Diagram that shows the GpuMmu model with its components and interactions.":::
