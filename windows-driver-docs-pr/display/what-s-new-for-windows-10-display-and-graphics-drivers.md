---
title: What's new for Windows 10 display and graphics drivers
description: Describes new features in Windows 10 for display drivers
ms.date: 05/12/2020
---

# What's new for Windows 10 display and graphics drivers

This page describes what's new in display and graphics drivers for Windows 10, version 2004 (WDDM 2.7). To see features added in previous versions of WDDM 2.X, see [What's new for prior WDDM 2.X versions](what-s-new-for-prior-wddm-2-x-versions.md).

## Mesh Shaders

Mesh shaders are a means of increasing the flexibility and performance of Direct3D 12's graphics pipeline when using rasterization. They act as a new replacement for the input assembler — in particular, vertex and geometry shader stages — replacing some of the input assembler's fixed-function behavior with flexible-function behavior. With mesh shaders, applications can apply culling earlier, and therefore more efficiently, than the input assembler. Primitives can be culled without having their index data processed by the GPU, which is highly beneficial as we see the primitive counts of 3D applications getting higher and higher over time.

In the case that there is a pixel shader attached, the primitives output from a mesh shader will feed directly into the pixel shader stage.

The mesh shader feature introduces the mesh shader stage along with a new stage: the amplification shader. Amplifications shaders replace the GPU tessellation stage. Applications set up their amplification shader to invoke a mesh shader some number of times as needed. Amplification shaders are an optional step which allow an application to dynamically control levels of geometric detail.

The mesh shader feature involves new shading language constructs as well as UMD changes. For reporting device capability of mesh shaders, there's a field called **MeshShaderTier** reported through [**D3D12DDI_D3D12_OPTIONS_DATA_0073**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_d3d12_options_data_0073). And, since this introduces two new shader stages, there are two new fields in [**D3D12DDIARG_CREATE_PIPELINE_STATE_0075**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddiarg_create_pipeline_state_0075), **hMeshShader** and **hAmplificationShader**. To kick things off, there's the command list DDI [**PFND3D12DDI_DISPATCH_MESH_0074**](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_dispatch_mesh_0074) and also [**D3D12DDI_INDIRECT_ARGUMENT_TYPE_DISPATCH_MESH**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_indirect_argument_type) for indirect dispatch.

## DirectX Raytracing (DXR) 1.1

WDDM 2.7 brings along some new features and improvements which build on the initial release of DXR in Direct3D 12.

- Inline raytracing is an alternative form of raytracing that doesn’t use any separate dynamic shaders or shader tables. It gives the developer flexibility and some convenience in all those cases where shaders using DXR 1.0-style raytracing, call them "dynamic-shader-based" raytracing, don't fit. Inline raytracing is available in any shader stage, including compute shaders, pixel shaders, and so forth. This is being mentioned here as something available with WDDM 2.7, although it doesn't correspond to a DDI change.

- Applications can call DispatchRays through ExecuteIndirect, allowing raytracing work to be configured on the GPU. This could be useful for applications that seek to cull, sort, or adjust raytracing work and they use shaders for doing that. Going along with this, there is now a D3D12DDI_INDIRECT_ARGUMENT_TYPE enumeration value. When using indirect raytracing dispatch, each element of the execute-indirect buffer is of type [**D3D12DDIARG_DISPATCH_RAYS_0054**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddiarg_dispatch_rays_0054).

- The overhead of creating pipeline state to account for different shader combinations is one of those difficult problems in 3D computer graphics. DXR 1.1 includes something that can help: add-to-state-object. AddToStateObject(), as it is exposed in the API, allows applications to add shaders to an existing state object with CPU overhead proportional only to what is being added. Going along with this, there are two device DDI functions: [**PFND3D12DDI_ADD_TO_STATE_OBJECT_0072**](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_add_to_state_object_0072) and [**PFND3D12DDI_CALC_PRIVATE_ADD_TO_STATE_OBJECT_SIZE_0072**](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_calc_private_add_to_state_object_size_0072).

For general capability-reporting, there's a new enumeration value [**D3D12DDI_RAYTRACING_TIER_1_1**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_raytracing_tier) used for reporting tier 1.1.

## Sampler Feedback

Sampler Feedback is a Direct3D 12 feature for capturing and recording texture sampling information and locations. Without sampler feedback, these details would be opaque to the developer. This feature gives applications the ability to not just know what mip was sampled, but to know where on those mips. Applications might be interested in sampling information, for example, to:

- accurately know what to load next in a texture streaming system, or
- accurately know what needs to be shaded in a texture-space-shading rendering system.

Feedback of sample operations is written to a "feedback map" which acts as a kind of opaque resource which must be transcoded to get application-inspectable information out. As for the writing of feedback itself, there are HLSL constructs in shader model 6_5 for that. The semantics are very similar to the semantics for Texture2D's Sample and its variants.

While sampler feedback makes good use of new shading language constructs, it also involves UMD changes. For device-capability-checking, there's a cap called SamplerFeedbackTier reported through [**D3D12DDI_D3D12_OPTIONS_DATA_0073**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_d3d12_options_data_0073). Resource creation has been revised to take a new field, the sampler feedback mip region, of type [**D3D12DDI_MIP_REGION_0075**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_mip_region_0075). Going along with this, there's also a new descriptor-creating method, [**PFND3D12DDI_CREATE_SAMPLER_FEEDBACK_UNORDERED_ACCESS_VIEW_0075**](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_create_sampler_feedback_unordered_access_view_0075).

## Content Protection

Optional protected resource support was added to Direct3D 12 video operations in WDDM 2.7. For background, protected resources existed before WDDM 2.7, but were available only for cross-API sharing and graphics or compute, not video.

Support for protected resources is not reported by the driver as a global thing; it's on a per-operation basis. If a driver reports supporting protected resources for a particular operation, that means that operation can read and write protected resources and supports cross-API sharing if the resource type allows for it. Another thing worth mentioning is that if a driver claims protected resource support for a particular format, it must support that format as a non-protected resource too.

With WDDM 2.7, resource creation methods are modified to take an optional D3D12DDI_HPROTECTEDRESOURCESESSION instance. Drivers are given this parameter at object-creation time to inform setup and allocations. Further, the memory budget checks are revised to indicate whether or not the operation will use protected resources. When the protected-resource-session parameter is non-NULL, this indicates that the operation will write to protected resources. To write to an unprotected resource, the operation object must be recreated.

Decoder and motion estimation references must be protected resources when the output is a protected resource. Video processing may read from a combination of protected and unprotected resources when writing to a protected resource.

Before recording one or more operations that writes to a protected resource, [**PFND3D12DDI_SETPROTECTEDRESOURCESESSION_0030**](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_setprotectedresourcesession_0030) must be called with a non-NULL protected resource session. Calling **PFND3D12DDI_SETPROTECTEDRESOURCESESSION_0030** with NULL is required before recording one or more operations that write to non-protected resources.

To know more beyond the above guided tour of DDI changes for content protection in WDDM 2.7, see [**D3D12DDI_VIDEO_DECODE_PROTECTED_RESOURCES_DATA_0072**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_decode_protected_resources_data_0072) as a starting point.

## Improved History Buffer Reporting for Tools

WDDM 2.7 introduces a DDI change which benefits GPU debugging tools' use of history buffers. With this change, a single command buffer submission can contain work corresponding to multiple command lists rather than just single command lists at a time. This change allows GPU debugging tools to more accurately report applications' performance characteristics.

This capability is reported through D3D12DDICAPS_TYPE_0073_SUPPORT_BATCHED_MARKERS. There is a new [**D3DDDI_MARKERLOGTYPE**](/windows-hardware/drivers/ddi/d3dumddi/ne-d3dumddi-d3dddi_markerlogtype) of enumeration value D3DDDIMLT_BATCHED, which corresponds to [**D3DDDI_BATCHEDMARKERDATA**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-d3dddi_batchedmarkerdata). ETW event data structures have been revved to contain some number of **D3DDDI_BATCHEDMARKERDATA** elements when they are of type D3DDDIMLT_BATCHED.

## DisplayPort (DP) AUX/I2C

The DP Auxiliary (AUX) channel provides access to DP Configuration Data (DPCD), which is a per-device register file used for reading the DP device's capabilities, link training, topology discovery, I2C bus access, and so forth. See [DXGK_DP_INTERFACE](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-dxgk_dp_interface) as a starting point.
