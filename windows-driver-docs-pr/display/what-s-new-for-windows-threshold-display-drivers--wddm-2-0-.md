---
title: What's new for Windows 10 display drivers (WDDM 2.x)
description: Describes new features in Windows 10 for display drivers
ms.assetid: 619175D4-98DA-4B17-8F6F-71B13A31374D
ms.date: 12/06/2018
ms.localizationpriority: medium
ms.custom: seodec18
---

# What's new for Windows 10 display drivers (WDDM 2.0 and later)

## WDDM 2.5

### Content changes

| Topic | Date | Description |
| --- | --- | --- |
| [EDID Extension (VSDB) for HMDs and Specialized Displays](specialized-monitors-edid-extension.md) | 12/03/2018 | Specification for Display Manufacturers |
| [DirectX Graphics Kernel Subsystem (Dxgkrnl.sys)](directx-graphics-kernel-subsystem.md) | 12/04/2018 | Kernel-mode interfaces that the Windows operating system implements through the Microsoft DirectX graphics kernel subsystem (Dxgkrnl.sys). |
| [WDDM 2.1 Features](wddm-2-1-features.md) | 01/10/2019|Describes new and updated features for WDDM 2.1 |

### Raytracing

New Direct3D DDI's were created in parallel of Direct3D API's, in order to support hardware-accelerated raytracing. Example DDIs include: 

* [PFND3D12DDI_BUILD_RAYTRACING_ACCELERATION_STRUCTURE_0054](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_build_raytracing_acceleration_structure_0054) 
* [PFND3D12DDI_COPY_RAYTRACING_ACCELERATION_STRUCTURE_0054](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_copy_raytracing_acceleration_structure_0054)
* [PFND3D12DDI_EMIT_RAYTRACING_ACCELERATION_STRUCTURE_POSTBUILD_INFO_0054](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_emit_raytracing_acceleration_structure_postbuild_info_0054)
* [PFND3D12DDI_GET_RAYTRACING_ACCELERATION_STRUCTURE_PREBUILD_INFO_0054](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_get_raytracing_acceleration_structure_prebuild_info_0054)

For more info about raytracing, see:

* [Announcing Microsoft DirectX Raytracing](https://blogs.msdn.microsoft.com/directx/2018/03/19/announcing-microsoft-directx-raytracing/)
* [DirectX Raytracing and the Windows 10 October 2018 Update](https://blogs.msdn.microsoft.com/directx/2018/10/02/directx-raytracing-and-the-windows-10-october-2018-update/)
* [DirectX Forums](https://forums.directxtech.com/index.php?topic=5985.0)

## WDDM 2.1

WDDM 2.1 enables new scenarios and provides significant improvements in the areas of performance, reliability, upgrade resiliency, diagnostic improvements and future system advancements for the Windows graphics sub-system.
The WDDM 2.0 driver model is a pre-requisite for D3D12. WDDM 2.0 and DirectX12 are available only on Windows 10 and higher.

The following is a list of feature additions and updates for WDDM 2.1.

* Improved graphics performance by reducing overhead time spent in memory management and more efficient usage of scarce graphics memory. The graphics performance improvements are:

    * Offer and reclaim resources - offer and reclaim improvements to reduce memory footprint of applications running in background mode.
    * Support for 2MB Page Table Entry encoding - In WDDM 2.1, large Page Table Entry (PTE) encoding in VRAM is enabled. This change boosts performance on systems that support it.
    * Support for 64KB memory pages - Virtual memory allocations using a 64KB granularity is also supported in WDDM 2.1. This change especially benefits APUs and SoCs by reducing overhead for accessing virtual memory pages.

* Hardware-based protected content improvements with *present batching* ([PlayReady 3.0](https://docs.microsoft.com/playready/))

* Driver Store installation for graphics drivers to improve driver upgrade resiliency.

* DXIL, a new shader complier language

* D3D12 performance and optimization improvements

* Improved diagnostic options for developers

For more information, see [WDDM 2.1 Features](wddm-2-1-features.md).

## WDDM 2.0

WDDM 2.0 includes memory management updates.

### GPU virtual memory

-   All physical memory is abstracted into virtual segments that can be managed by the graphics processing unit (GPU) memory manager.
-   Each process gets its own GPU virtual address space.
-   Support for swizzling ranges has been removed.

For more details, see [GPU virtual memory in WDDM 2.0](gpu-virtual-memory-in-wddm-2-0.md).

### Driver residency

-   The video memory manager makes sure that allocations are resident in memory before submitting command buffers to the driver. To facilitate this functionality, new user mode driver device driver interfaces (DDIs) have been added ([*MakeResident*](https://msdn.microsoft.com/library/windows/hardware/dn906357), [*TrimResidency*](https://msdn.microsoft.com/library/windows/hardware/dn906364), [*Evict*](https://msdn.microsoft.com/library/windows/hardware/dn906355)).
-   The allocation and patch location list is being phased out because it is not necessary in the new model.
-   User mode drivers are now responsible for handling allocation tracking and several new DDIs have been added to enable this.
-   Drivers are given memory budgets and expected to adapt under memory pressure. This allows Universal Windows drivers to function across application platforms.
-   New DDIs have been added for process synchronization and context monitoring.

For more details, see [Driver residency in WDDM 2.0](driver-residency-in-wddm-2-0.md).