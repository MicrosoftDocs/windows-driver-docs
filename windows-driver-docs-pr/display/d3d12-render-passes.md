---
title: Direct3D 12 Render Passes
description: The Direct3D render pass feature
ms.date: 03/28/2025
ms.topic: concept-article
---

# Direct3D 12 render passes

The Direct3D 12 render pass feature is introduced in Windows 10, version 1809 (WDDM 2.5). It extends the generic concept of render passes by introducing a more structured way for applications to declare data dependencies and output targets for a set of rendering operations, thus enabling more efficient GPU processing.

This article describes the goals of the render pass feature and lists the key DDI additions/changes that support it. For more information, the [D3D12 Render Passes specification](https://microsoft.github.io/DirectX-Specs/d3d/RenderPasses.html). For application-level information, see [Direct3D 12 Render Passes](/windows/win32/direct3d12/direct3d-12-render-passes).

## Goals

D3D12 Render Passes are designed to achieve the following goals:

* Allow applications to avoid unnecessary loads and stores of resources between on-chip memory and main memory.

  D3D12 Render Passes provide a central location for applications to indicate their data dependencies for a set of rendering operations. These data dependencies allow drivers to inspect the data at bind/barrier time, and issue instructions that minimize resource loads and stores to and from main memory.

  The reduction in unnecessary resource loads/stores particularly optimizes rendering on TBDR (tile-based deferred rendering) architectures.

* Allow TBDR (tile-based deferred rendering) architectures to opportunistically persist resources in on-chip cache across Render Passes (even in separate command lists)
  
  * Case A: Reading/writing pixels "one-to-one"

    A common rendering pattern is for an application to render to Render Target View (RTV) A, and then texture from that resource as shader resource view (SRV) A at some time in future while rendering to RTV B. For cases in which writes to RTV B are reading from SRV A 'one-to-one' (pixels mapped to the identical location in SRV A), some architectures are able to continue the current binning pass during the writes to RTV A. These architectures thus avoid a flush to main memory since the SRV A reads only have a dependency on the current tile.

    A design goal is to enable these two passes to be coalesced without an intervening flush to main memory.

  * Case B: Writes to the same render targets across multiple command lists

    Another common rendering pattern is for the application to render to the same render target(s) across multiple command lists serially, even though the rendering commands are generated in parallel. D3D12 render passes allows drivers to avoid a flush to main memory on command list boundaries when the application knows it will resume rendering to the same render target(s) on the immediate succeeding command list.

    A design goal is to allow these two passes to be combined in a way that avoids an intervening flush to main memory.

* Allow the render pass APIs to be used on drivers that don't take advantage of them

  The design allows the APIs to be called on drivers that don't take advantage of the feature. As long as the application is running on a sufficiently new runtime, Render Passes can be used on all devices. Apps can write one path.

  Devices that don't care get a runtime translation of the feature to nonrender passes. Devices that do want to take advantage can do so.

* Allow UMD to choose an optimal rendering path without heavy CPU penalty

  This feature should be aligned with the low CPU-overhead goals of D3D12, and should be designed in such a way to not significantly impact CPU usage for common rendering workloads (no more than ~20%).

* Allow ISVs to verify proper use of the feature even on drivers that aren't necessarily making behavior changes based on feature use

  The debug layer should be able to help identify incorrect use of the feature even when running on a nonsupporting driver. (for example, how the DX11 debug layer clears a resource to a random color in response to a Discard call).

## Render passes driver interface updates

This section describes the key D3D12 interface updates made to support the extended Render Passes feature.

* The [**D3D12DDI_RENDER_PASS_FUNCS_0053**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_render_pass_funcs_0053) structure is added. The runtime queries this version of the interface by calling [**pfnFillDditTable**](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_fillddittable) with the [**D3D12DDI_TABLE_TYPE_0043_RENDER_PASS**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_table_type) table type. The structure contains pointers to the following driver-implemented DDIs.

  * [**pfnBeginRenderPass**](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_begin_render_pass_0053)

  * [**pfnEndRenderPass**](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_end_render_pass_0053)

* The [**D3D12DDI_RENDER_PASS_BEGINNING_ACCESS_TYPE_0053**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_render_pass_beginning_access_type_0053) and [**D3D12DDI_RENDER_PASS_ENDING_ACCESS_TYPE_0053**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_render_pass_ending_access_type_0053) enumerations are added. These enumerations allow the driver to specify how resources are accessed during a render pass. For more information, see [Resource access declaration](#resource-access-declaration).

* The following structures are used for clear and preserve local parameters access types. They allow for precise control over the initialization and retention of resource data.

  * [**D3D12DDI_RENDER_PASS_BEGINNING_ACCESS_CLEAR_PARAMETERS_0053**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_render_pass_beginning_access_clear_parameters_0053) provides parameters for clear operations.
  * [**D3D12DDI_RENDER_PASS_BEGINNING_ACCESS_PRESERVE_LOCAL_PARAMETERS_0101**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_render_pass_beginning_access_preserve_local_parameters_0101) provides parameters for local preservation of resources.

* The [**D3D12DDIARG_RENDER_PASS_RENDER_TARGET_DESC_0053**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddiarg_render_pass_render_target_desc_0053) and [**D3D12DDIARG_RENDER_PASS_DEPTH_STENCIL_DESC_0053**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddiarg_render_pass_depth_stencil_desc_0053) structures describe the render targets and depth-stencil buffers used in an extended render pass, including their beginning and ending access configurations, allowing for comprehensive setup of the render pass frame buffer.  

* The [**D3D12DDIARG_RENDER_PASS_FLAGS_0053**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddiarg_render_pass_flags_0053) enumeration introduces flags to modify the behavior of the render pass. These flags provide more flexibility in optimizing render pass execution.

### Resource access declaration

The [**D3D12DDI_RENDER_PASS_BEGINNING_ACCESS_TYPE_0053**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_render_pass_beginning_access_type_0053) enumeration is added. It specifies the beginning access type of a resource in a render pass. The following *extended* render pass values are added:

* D3D12DDI_RENDER_PASS_BEGINNING_ACCESS_TYPE_0101_PRESERVE_LOCAL_RENDER
* D3D12DDI_RENDER_PASS_BEGINNING_ACCESS_TYPE_0101_PRESERVE_LOCAL_SRV
* D3D12DDI_RENDER_PASS_BEGINNING_ACCESS_TYPE_0101_PRESERVE_LOCAL_UAV

Likewise, the [**D3D12DDI_RENDER_PASS_ENDING_ACCESS_TYPE_0053**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_render_pass_ending_access_type_0053) enumeration is added. It specifies the ending access type of a resource in a render pass. The following *extended* render pass values are added:

* D3D12DDI_RENDER_PASS_ENDING_ACCESS_TYPE_0101_PRESERVE_LOCAL_RENDER
* D3D12DDI_RENDER_PASS_ENDING_ACCESS_TYPE_0101_PRESERVE_LOCAL_SRV
* D3D12DDI_RENDER_PASS_ENDING_ACCESS_TYPE_0101_PRESERVE_LOCAL_UAV

At [**pfnBeginRenderPass**](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_begin_render_pass_0053) time, the driver receives all Resources that are serving as RTVs/DSVs (data source view) within that Render Pass. The user declares these Resources and specifies their beginning/ending access type characteristics. The beginning and ending values must both be provided for all resources.

| Beginning Access Type | Matching Ending Access Type |
| --------------------- | --------------------------- |
| D3D12DDI_RENDER_PASS_BEGINNING_ACCESS_TYPE_0053_DISCARD | D3D12DDI_RENDER_PASS_ENDING_ACCESS_TYPE_0053_DISCARD |
| D3D12DDI_RENDER_PASS_BEGINNING_ACCESS_TYPE_0053_PRESERVE | D3D12DDI_RENDER_PASS_ENDING_ACCESS_TYPE_0053_PRESERVE |
| D3D12DDI_RENDER_PASS_BEGINNING_ACCESS_TYPE_0053_CLEAR | D3D12DDI_RENDER_PASS_ENDING_ACCESS_TYPE_0053_RESOLVE |
| D3D12DDI_RENDER_PASS_BEGINNING_ACCESS_TYPE_0053_NO_ACCESS | D3D12DDI_RENDER_PASS_ENDING_ACCESS_TYPE_0053_NO_ACCESS |
| D3D12DDI_RENDER_PASS_BEGINNING_ACCESS_TYPE_0101_PRESERVE_LOCAL_RENDER | D3D12DDI_RENDER_PASS_ENDING_ACCESS_TYPE_0101_PRESERVE_LOCAL_RENDER |
| D3D12DDI_RENDER_PASS_BEGINNING_ACCESS_TYPE_0101_PRESERVE_LOCAL_SRV | D3D12DDI_RENDER_PASS_ENDING_ACCESS_TYPE_0101_PRESERVE_LOCAL_SRV |
| D3D12DDI_RENDER_PASS_BEGINNING_ACCESS_TYPE_0101_PRESERVE_LOCAL_UAV | D3D12DDI_RENDER_PASS_ENDING_ACCESS_TYPE_0101_PRESERVE_LOCAL_UAV |

## WHLK Testing

Direct3D 11on12 replaces OMSetRenderTargets calls with BeginRenderPass/EndRenderPass as appropriate to test general rendering functionality with Render Passes.

The HLK tests other specific functionality, including:

* A BEGINNING clear, with no rendering in Render Pass, and an ending PRESERVE results in a clear, for various resource formats and types (and RT counts).

* A BEGINNING clear, with rendering in the Render Pass, and an ending PRESERVE results in a clear (with drawing properly ordered after the clear), for various resource formats and types (and RT counts).

* A BEGINNING discard, that uses a blending or depth operations that have dependencies on existing contents doesn't result in a GPU hang (undefined rendering values is fine).

* An ENDING resolve correctly resolves resources in various configurations (including using the new MIN/MAX capabilities for depth/stencil that were added in ResolveSubresourceRegion).

* Using SUSPEND/RESUME results in no rendering difference (versus ENDING_PRESERVE/BEGINNING_PRESERVE), for various resource formats and types.

* For a BEGINNING/ENDING preserve/preserve_local, when no work occurs in the Render Pass, the values are still present in the Render Target outside of the Render Pass.
