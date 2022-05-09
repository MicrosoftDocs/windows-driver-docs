---
title: Direct3D enhanced barriers
description: Learn about Direct3D enhanced barriers
keywords:
- Direct3D12 enhanced barriers
- WDDM 3.1 , enhanced barriers
ms.date: 05/24/2022
ms.localizationpriority: medium
---

# Direct3D enhanced barriers

Enhanced barriers are a set of Direct3D APIs and DDIs that give developers independent control over GPU work synchronization, texture layout transitions, and cache flushing (resource memory access). Enhanced barriers replace legacy resource state barriers with more expressive barrier types. Enhanced barriers offer less latency, support for concurrent read and write (including same-resource copy), diverse aliasing topologies, and better concurrency.

Although enhanced barriers are by no means simpler than [legacy resource barriers](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_resourcebarrier_0022), they are far less ambiguous, and therefore actually easier for developers to use. The legacy resource barriers design was intended to abstract the nuance around cache flushing, hazard tracking, and texture layout using the concept of a “resource state”. However, this over-simplification caused as much harm as good in many ways; for example:

* Developers were often forced to use expensive barriers when a less expensive (or even no) barrier should be allowed.
* Legacy resource barriers were often incapable of fully expressing hardware-supported scenarios, such as concurrent read and write on a single resource or indicating resource state during aliasing transitions.
* Developers still had to understand the inner complexities behind resource states, such as state promotion and decay rules and “simple” vs “advanced” aliasing models, in order to use barriers effectively.

There are three types of enhanced barriers:

* Buffer barriers
* Texture barriers
* Global barriers

All barriers control GPU work synchronization and read or write access types before and after the barrier.

Texture barriers additionally manage layout of texture subresources. Subresource selection can be expressed as a range of mip, array, and plane slices, in addition to the familiar one-or-all option used by legacy resource barriers.

Buffer barriers and global barriers control only synchronization and resource access and have no impact on resource layout (buffers don’t have a layout). Global barriers affect all cached memory so they can be expensive and should only be used when a more scoped barrier is insufficient.

Enhanced buffers do not include implicit state transitions for resource state promotion and decay, which was a major source of developer confusion. Instead, all resources initially have *common* access at the start of any command list execution. This common access means that any resource can be accessed without a barrier as long as the access type is compatible with the current layout and create-time constraints (for example, D3D12DDI_RESOURCE_FLAG_ALLOW_RENDER_TARGET, etc). Since buffers have no layout, any buffer access type is allowed within the limits of create-time constraints. The only stateful attribute of a resource is texture layout. A texture subresource can only be in one layout at a time, and transitioning layout always requires a barrier.

All write operations must be finished and flushed using a barrier before any subsequent dependent access in the same [**PFND3D12DDI_EXECUTECOMMANDLISTS**](nc-d3d12umddi-pfnd3d12ddi_executecommandlists.md) scope. This is accomplished by specifying before/after synchronization scopes and before/after access types in a barrier, as well as any before/after texture layout changes if required.

Frequently, developers want to write to one region of a buffer/subresource, while concurrently reading from a different region of the same buffer/subresource. Legacy resource barrier rules prevented placing a resource in both read and write states at the same time, which was a necessary limitation imposed by the state model rather than by any hardware constraints. Enhanced barriers do allow concurrent read and write access to the same subresource, including same-resource copy.

Managing aliased resources with legacy resource barriers was difficult or impossible to handle efficiently. In many cases, developers simply used NULL/NULL aliasing barriers (akin to a sync-and-flush-everything barrier). Even then, the state of the affected resources might have be ambiguous, requiring additional barriers to establish known states (which itself is a dubious act given the resource data might be ‘garbage’). In addition, Clear, Discard, or Copy operations were needed if aliased textures were to be used as render target or depth-stencil resources. Resource aliasing with enhanced barriers is much more direct. For example, finish and flush any work on ‘deactivating’ resources and declare a layout on any ‘activating’ textures, with the option to perform a full-texture Discard as part of the barrier. There are a variety of ways to accomplish aliasing transitions depending on whether data-sharing requirements or alignment of aliased resources. There is a set of barriers to efficiently accomplish just about any aliasing scenario supported by hardware, or you can use a big sync-and-flush-everything global barrier if simplicity is preferred.

Applications can use both legacy resource barriers and enhanced barriers simultaneously, with the limitation that a resource switching between these is first placed in RESOURCE_STATE_COMMON or BARRIER_LAYOUT_COMMON/BARRIER_ACCESS_COMMON. For the most part, the debug layer continues to validate legacy resource state for all resources that were last assigned a legacy state. However, [GPU-Based Validation](/windows/win32/direct3d12/using-d3d12-debug-layer-gpu-based-validation) (GBV) cannot reasonably validate both legacy state and enhanced barriers state, so GBV always performs enhanced barrier validation when the underlying hardware supports enhanced barriers, reporting equivalent enhance barrier state for resources using a legacy barrier state. This means that some GBV errors might report layout or access bits errors on a resource that was transitioned using a legacy state. This will become less of an issue as developers switch to enhanced barriers. There is an option to force GBV to use legacy state validation.

For additional information, including application-level specifics, see the [D3D12 Enhanced Barriers Specification](https://microsoft.github.io/DirectX-Specs/d3d/D3D12EnhancedBarriers.html).




------------ everything below is video encoding -------------------------





## Reporting video encoding support and capabilities

The existing video-related framework was extended to allow drivers to report video encoding support and capabilities.

* **D3D12DDI_FEATURE_VERSION_VIDEO_0083_0** is the version number that defines the first full implementation of all D3D12 video encode milestones that were introduced in Windows 11.

* The [**D3D12DDICAPS_TYPE_VIDEO_0020**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddicaps_type_video_0020) enumeration was extended to include the following video encoding support values:

  * D3D12DDICAPS_TYPE_VIDEO_0080_ENCODER_CODEC = 31,
  * D3D12DDICAPS_TYPE_VIDEO_0080_ENCODER_PROFILE_LEVEL = 32,
  * D3D12DDICAPS_TYPE_VIDEO_0080_ENCODER_OUTPUT_RESOLUTION_RATIOS_COUNT = 33,
  * D3D12DDICAPS_TYPE_VIDEO_0080_ENCODER_OUTPUT_RESOLUTION = 34,
  * D3D12DDICAPS_TYPE_VIDEO_0080_ENCODER_INPUT_FORMAT = 35,
  * D3D12DDICAPS_TYPE_VIDEO_0080_ENCODER_RATE_CONTROL_MODE = 36,
  * D3D12DDICAPS_TYPE_VIDEO_0080_ENCODER_INTRA_REFRESH_MODE = 37,
  * D3D12DDICAPS_TYPE_VIDEO_0080_ENCODER_FRAME_SUBREGION_LAYOUT_MODE = 38,
  * D3D12DDICAPS_TYPE_VIDEO_0080_ENCODER_HEAP_SIZE = 39,
  * D3D12DDICAPS_TYPE_VIDEO_0080_ENCODER_CODEC_CONFIGURATION_SUPPORT = 40,
  * D3D12DDICAPS_TYPE_VIDEO_0080_ENCODER_SUPPORT = 41,
  * D3D12DDICAPS_TYPE_VIDEO_0080_ENCODER_CODEC_PICTURE_CONTROL_SUPPORT = 42,
  * D3D12DDICAPS_TYPE_VIDEO_0080_ENCODER_RESOURCE_REQUIREMENTS = 43

  The D3D runtime calls the driver's [**PFND3D12DDI_VIDEO_GETCAPS**](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_video_getcaps) callback to query for video encoding support.

* A driver that supports video encoding provides the D3D runtime with pointers to its video encoding callback functions in the [**D3D12DDI_DEVICE_FUNCS_VIDEO_0082_0**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_device_funcs_video_0082_0) structure.

## D3D12 video encoding callback functions

A driver implements the following callback functions to support D3D12 video encoding.

* Create the driver object that represents the video encoder:

  * [**PFND3D12DDI_CALCPRIVATEVIDEOENCODERSIZE_0082_0**](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_calcprivatevideoencodersize_0082_0) calculates the amount of memory that the D3D runtime needs to allocate for the driver object.

  * [**PFND3D12DDI_CREATEVIDEOENCODER_0082_0**](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_createvideoencoder_0082_0) creates the actual video encoder object that holds the state of the video encoding session.

* Create the driver object that represents the video encoder heap:

  * [**PFND3D12DDI_CALCPRIVATEVIDEOENCODERHEAPSIZE_0080_2**](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_calcprivatevideoencoderheapsize_0080_2) calculates the amount of memory that the D3D runtime needs to allocate for the driver object.

  * [**PFND3D12DDI_CREATEVIDEOENCODERHEAP_0080_2**](/windows-hardware/drivers/ddi/d3d12umddi/) creates the video encoder heap object that contains resolution-dependent driver resources and state.

* Encode a frame:

  * [**PFND3D12DDI_VIDEO_ENCODE_FRAME_0082_0**](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_video_encode_frame_0082_0) records an encode frame operation to the command list.

  * After the encoding operation, [**PFND3D12DDI_VIDEO_ENCODE_RESOLVE_OUTPUT_METADATA_0082_0**](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_video_encode_resolve_output_metadata_0082_0) must also be called to resolve the encode operation's output metadata into a readable format. The layout of the driver's resolved metadata is similar to the example shown in a diagram [in the specification](https://microsoft.github.io/DirectX-Specs/d3d/D3D12VideoEncoding.html).

* Destroy the video encoder and associated heap:

  * [**PFND3D12DDI_DESTROYVIDEOENCODER_0080**](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_destroyvideoencoder_0080)

  * [**PFND3D12DDI_DESTROYVIDEOENCODERHEAP_0080**](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_destroyvideoencoderheap_0080)

## Testing

The following tests are included as part of the [Windows Hardware Lab Kit (WHLK)](/windows-hardware/test/hlk/). See the WHLK for details.

| Test Name | Description |
| --------- | ----------- |
| CreateVideoEncoder | Validates the creation of VideoEncoder/VideoEncoderHeap based on the reported CheckFeatureSupport related cases. |
| SingleEncodeH264/HEVC | QR-code based tests for structural image basic checks. The input images sequence is stamped with predefined QR content, then encoded and decoded, and finally checked to ensure that the output values (and to some extent, quality), are what is expected. |
| EncodeProfileLevelSuggestionsH264/HEVC | Validates that the D3D12_FEATURE_DATA_VIDEO_ENCODER_SUPPORT.SuggestedProfile/Level values are as expected based on H.264/HEVC specifications and on the configurations passed as input to D3D12_FEATURE_DATA_VIDEO_ENCODER_SUPPORT. |
| EncodeHeapSizeCap | Validates increasing memory footprint with different increasing input arguments. |
| SimpleGOPEncodeH264/HEVC(10bit) | Transcodes an input video using different resolutions, GOP patterns, slice modes and other codec configurations, and validates the output encoded video against the input video stream difference is acceptable. This comparison is done using peak signal to noise ratio (PSNR). |
| EncodeSubregions/ResolutionReconfiguration | Validates on-the-fly reconfigurations. |
| EncodeH264LongTermReferences | Validates the use of long term picture references. |
| EncodeIntraRefresh | Validates a simple scenario of intra-refresh with an open IPP...P...P... GOP. |
| VideoEncodeCommandListFeatures | Validates Predication and Markers for Video encode command lists. |
| VideoEncodeTimestamps | Validates Timestamps for Video encode command lists. |

## Video encoding scenarios

### OneCore

D3D12 video encoding support enables portable hardware-accelerated video encoding on platforms where only D3D12 is available. This includes the various OneCore SKUs used by cloud compute and IoT platforms. Video encoding acceleration is available in these scenarios without the need for using platform-specific solutions.

### Media APIs

Video encoding capabilities in a low level and portable way is accessible across all hardware vendors. This allows higher level Media APIs (such as Media Foundation) to build their media layers on top of this API which takes care of abstracting the different hardware platforms. Given the low level design of the API, these higher level media layers can optimize for their scenarios by having fine grain control of synchronization and memory allocation/residency aspects of the video encode session such as full control of the reference picture management and bitstream headers writing responsibilities. This shift of responsibilities to the layer sitting above this API also allows hardware vendors to have a consistent set of encoding policies (eg. DPB heuristics such as adaptive GOP) in the media layer that can be reused across different hardware platforms.

### Interoperability with D3D graphics, compute, and machine learning

The D3D12 video encode API enables efficient interoperability between D3D12 video encode and D3D12 graphics, compute, and machine learning scenarios, which is interesting for scenarios such as running machine learning inference over a camera stream.

### Game streaming scenarios

The D3D12 video encode API enables game streaming scenarios that require a highly performant low level API.
