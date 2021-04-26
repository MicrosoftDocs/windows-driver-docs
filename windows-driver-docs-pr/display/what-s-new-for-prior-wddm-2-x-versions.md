---
title: Features added in prior WDDM 2.X versions
description: Describes features in prior Windows 10 releases for display and graphics drivers
ms.date: 03/24/2020
ms.localizationpriority: medium
ms.custom: seodec18, 19H1
---

# Features added in prior WDDM 2.X versions

This page describes display and graphics drivers' features that were added in previous versions of WDDM 2.X for Windows 10. To see features added for the most recent WDDM 2.X version, see [What's new for Windows 10 display and graphics drivers](what-s-new-for-windows-10-display-and-graphics-drivers.md).

## WDDM 2.6

### Super Wet Ink

*Super-Wet Ink* is a feature that revolves around *front-buffer rendering*. IHV drivers can support the creation of “displayable” textures of formats or modes that are not supported by the hardware. They can do this by allocating the texture that the app requested, along with a “shadow” texture with a format/layout that can be displayed, and then copying between the two at present-time. This “shadow” may not necessarily be a texture in the normal way we think of it, but may just be compression data. Additionally, it may not be required to exist, but may be an optimization instead.

The runtime will evolve to understand these aspects of displayable surfaces:

* Whether or not a shadow must exist for display on a particular VidPnSource/plane.

* Whether it is more optimal for a shadow to exist.

* When to transfer contents from the application surface to the shadow surface. The runtime will be explicit about this operation, as opposed to it being implicit within Present.

* How to request setting a mode or dynamically flipping between the original and shadow surfaces.

Scanout may begin shortly after a VBlank, scans vertically from top to bottom of the image, and completes shortly before the next VBlank. This is not always the case, depending on the timing of the pixel clock, and the layout of the data in the texture; especially if there is actually compression available.

New DDIs were added to separate and understand transformations which occur prior to scanout, in order to (when possible) enable front-buffer rendering. See [D3DWDDM2_6DDI_SCANOUT_FLAGS](/windows-hardware/drivers/ddi/d3d10umddi/ne-d3d10umddi-d3dwddm2_6ddi_scanout_flags) and [PFND3DWDDM2_6DDI_PREPARE_SCANOUT_TRANSFORMATION](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3dwddm2_6ddi_prepare_scanout_transformation).

### Variable Rate Shading

Variable rate shading, or coarse pixel shading, is a mechanism to enable allocation of rendering performance/power at varying rates across rendered images.

In the previous model, in order to use MSAA (multi-sample anti-aliasing) to reduce geometric aliasing:

* The amount by which to reduce geometric aliasing needs to be known up-front when the target is allocated.
* The amount by which to reduce geometric aliasing can’t be changed once the target is allocated.

In WDDM 2.6, the new model extends MSAA into the opposite, *coarse pixel* direction, by adding a new concept of *coarse shading*. This is where shading can be performed at a frequency coarser than a pixel. A group of pixels can be shaded as a single unit and the result is then broadcast to all samples in the group.

A coarse shading API allows apps to specify the number of pixels that belong to a shaded group. The coarse pixel size can be varied after the render target is allocated. So, different portions of the screen or different draw passes can have different course shading rates.

A multiple-tier implementation is available with two user-queryable caps. For Tiers 1 and 2, coarse shading is available for both single-sampled and MSAA resources. For MSAA resources, shading can be performed per-coarse-pixel or per-sample as usual. However, on Tiers 1 and 2, for MSAA resources, coarse sampling cannot be used to shade at a frequency between per-pixel and per-sample.

Tier 1:

* Shading rate can only be specified on a per-draw-basis; nothing more granular than that

* Shading rate applies uniformly to what is drawn independently of where it lies within the render target  

Tier 2:

* Shading rate can be specified on a per-draw-basis, as in Tier 1. It can also be specified by a combination of per-draw-basis, and of:

  * Semantic from the per-provoking-vertex, and
  * A screenspace image

* Shading rates from the three sources are combined using a set of combiners
* Screen space image tile size is 16x16 or smaller. Shading rate requested by the app is guaranteed to be delivered exactly  (for precision of temporal and other reconstruction filters)

* SV_ShadingRate PS input is supported. The per-provoking vertex rate, also referred to here as a per-primitive rate, is only valid when one viewport is used and SV_ViewportIndex is not written to.

* The per-provoking vertex rate, also referred to as a per-primitive rate, can be used with more than one viewport if the SupportsPerVertexShadingRateWithMultipleViewports cap is marked true. Additionally, in that case, it can be used when SV_ViewportIndex is written to.

See [PFND3D12DDI_RS_SET_SHADING_RATE_0062](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_rs_set_shading_rate_0062) and [D3D12DDI_SHADING_RATE_0062](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_shading_rate_0062).

### Collect Diagnostic Info

*Collect diagnostic info* allows the OS to collect a private data from drivers for graphics adapters which consist of both rendering and display functions. This new feature is a requirement in WDDM 2.6.

The new DDI should allow the OS to collect information at any time a driver is loaded. Currently the OS uses DxgkDdiCollectDebugInfo function implemented by the miniport to query driver private data for TDR (timeout detection and recovery) related cases. The new DDI will be used to collect data for variety of reasons. The OS will call this DDI when diagnostic is needed providing a type of information being requested. The driver should collect all private information important to investigate the issue and submit it to the OS. DxgkDdiCollectDebugInfo will be eventually deprecated and replaced with DxgkDdiCollectDiagnosticInfo.

See [DXGKDDI_COLLECTDIAGNOSTICINFO](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_collectdiagnosticinfo).

### Background Processing

Background processing allows user mode drivers to express desired threading behavior, and the runtime to control/monitor it. User mode drivers would spin up background threads and assign the threads as low a priority as possible, and rely on the NT scheduler to ensure these threads don’t disrupt the critical-path threads, generally with success.

APIs allow apps to adjust what amount of background processing is appropriate for their workloads and when to perform that work.

See [PFND3D12DDI_QUEUEPROCESSINGWORK_CB_0062](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_queueprocessingwork_cb_0062).

### Driver Hot Update

Driver hot update reduces server downtime as much as possible when an OS component needs to be updated.

Driver hot patch is used to apply a security patch to the kernel mode driver. In this case the driver is asked to save adapter memory, the adapter is stopped, the driver is unloaded, new driver is loaded and the adapter is started again.

See[DXGKDDI_SAVEMEMORYFORHOTUPDATE](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_savememoryforhotupdate) and [DXGKDDI_RESTOREMEMORYFORHOTUPDATE](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_restorememoryforhotupdate).

## WDDM 2.5

### Tracked Workloads

Tracked Workloads is an experimental feature that provides more control over the trade-off between quicker processor execution vs. lower power consumption, and is not available until further notice. The implementation was removed from Windows 10, version 2003; and deprecated from earlier OS versions as part of a security fix.

### Content changes

| Topic | Date | Description |
| --- | --- | --- |
| [EDID Extension (VSDB) for HMDs and Specialized Displays](specialized-monitors-edid-extension.md) | 12/03/2018 | Specification for Display Manufacturers |
| [DirectX Graphics Kernel Subsystem (Dxgkrnl.sys)](directx-graphics-kernel-subsystem.md) | 12/04/2018 | Kernel-mode interfaces that the Windows operating system implements through the Microsoft DirectX graphics kernel subsystem (Dxgkrnl.sys). |
| [WDDM 2.1 Features](wddm-2-1-features.md) | 01/10/2019|Describes new and updated features for WDDM 2.1 |

### Raytracing

New Direct3D DDI's were created in parallel of Direct3D API's, in order to support hardware-accelerated raytracing. Example DDIs include:

* [PFND3D12DDI_BUILD_RAYTRACING_ACCELERATION_STRUCTURE_0054](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_build_raytracing_acceleration_structure_0054)
* [PFND3D12DDI_COPY_RAYTRACING_ACCELERATION_STRUCTURE_0054](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_copy_raytracing_acceleration_structure_0054)
* [PFND3D12DDI_EMIT_RAYTRACING_ACCELERATION_STRUCTURE_POSTBUILD_INFO_0054](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_emit_raytracing_acceleration_structure_postbuild_info_0054)
* [PFND3D12DDI_GET_RAYTRACING_ACCELERATION_STRUCTURE_PREBUILD_INFO_0054](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_get_raytracing_acceleration_structure_prebuild_info_0054)

For more info about raytracing, see:

* [Announcing Microsoft DirectX Raytracing](https://devblogs.microsoft.com/directx/announcing-microsoft-directx-raytracing/)
* [DirectX Raytracing and the Windows 10 October 2018 Update](https://devblogs.microsoft.com/directx/directx-raytracing-and-the-windows-10-october-2018-update/)

### Display Synchronization

The OS will check for capabilities for display synchronization when the display is exposed by the driver to the OS, so prior to enabling the display. For TypeIntegratedDisplay child devices, this is reported via a call to [DxgkDdiQueryAdapterInfo](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryadapterinfo) with *Type* [DXGKQAITYPE_INTEGRATED_DISPLAY_DESCRIPTOR2](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_queryadapterinfotype) during adapter initialization. For TypeVideoOutput child devices, which are supported starting with WDDM 2.5, the capabilities are reported as part of the hot plug processing via [DxgkDdiUpdateMonitorLinkInfo](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_updatemonitorlinkinfo) so that the capabilities may change based on the target or connected monitor.

The OS specifies the display synchronization in the [DxgkDdiSetTimingsFromVidPn](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_settimingsfromvidpn) call in the Input field in the per path [DXGK_SET_TIMING_PATH_INFO](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_set_timing_path_info#input) structure.

## WDDM 2.1

WDDM 2.1 enables new scenarios and provides significant improvements in the areas of performance, reliability, upgrade resiliency, diagnostic improvements and future system advancements for the Windows graphics sub-system.
The WDDM 2.0 driver model is a pre-requisite for D3D12. WDDM 2.0 and DirectX12 are available only on Windows 10 and higher.

The following is a list of feature additions and updates for WDDM 2.1.

* Improved graphics performance by reducing overhead time spent in memory management and more efficient usage of scarce graphics memory. The graphics performance improvements are:

  * Offer and reclaim resources - offer and reclaim improvements to reduce memory footprint of applications running in background mode.
  * Support for 2MB Page Table Entry encoding - In WDDM 2.1, large Page Table Entry (PTE) encoding in VRAM is enabled. This change boosts performance on systems that support it.
  * Support for 64KB memory pages - Virtual memory allocations using a 64KB granularity is also supported in WDDM 2.1. This change especially benefits APUs and SoCs by reducing overhead for accessing virtual memory pages.

* Hardware-based protected content improvements with *present batching* ([PlayReady 3.0](/playready/))

* Driver Store installation for graphics drivers to improve driver upgrade resiliency.

* DXIL, a new shader complier language

* D3D12 performance and optimization improvements

* Improved diagnostic options for developers

For more information, see [WDDM 2.1 Features](wddm-2-1-features.md).

## WDDM 2.0

WDDM 2.0 includes memory management updates.

### GPU virtual memory

* All physical memory is abstracted into virtual segments that can be managed by the graphics processing unit (GPU) memory manager.
* Each process gets its own GPU virtual address space.
* Support for swizzling ranges has been removed.

For more details, see [GPU virtual memory in WDDM 2.0](gpu-virtual-memory-in-wddm-2-0.md).

### Driver residency

* The video memory manager makes sure that allocations are resident in memory before submitting command buffers to the driver. To facilitate this functionality, new user mode driver device driver interfaces (DDIs) have been added ([*MakeResident*](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_makeresidentcb), [*TrimResidency*](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_trimresidencyset), [*Evict*](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_evictcb)).
* The allocation and patch location list is being phased out because it is not necessary in the new model.
* User mode drivers are now responsible for handling allocation tracking and several new DDIs have been added to enable this.
* Drivers are given memory budgets and expected to adapt under memory pressure. This allows Universal Windows drivers to function across application platforms.
* New DDIs have been added for process synchronization and context monitoring.

For more details, see [Driver residency in WDDM 2.0](driver-residency-in-wddm-2-0.md).
