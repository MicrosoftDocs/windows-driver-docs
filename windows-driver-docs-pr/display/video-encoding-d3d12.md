---
title: D3D12 video encoding
description: Learn about D3D12 video encoding
keywords:
- Direct3D version 10.1 WDK Windows 7 display , extended format
- extended format WDK Windows 7 display
ms.date: 08/23/2021
ms.localizationpriority: medium
---

# D3D12 video encoding

Starting in Windows 11 (WDDM 3.0), video encoding was added to D3D12. This feature provides a coherent set of encoding APIs that are consistent with the D3D12 framework, and allows optimal usage of hardware encoding with D3D12 in a low-level fashion. The video encode API provides access to the video encode hardware acceleration capabilities for different scenarios such as Internet of Things (IoT), Cloud, Media APIs, machine learning and game streaming.

<!--- QUESTIONS:
What is the helper layer called?
Which blocks in the image are relevant to driver writers?
Where is image encoding spec/DDIs?
 --->

A system-supplied helper layer was developed on top of this API interface to provide a higher level entry point for users that need a higher level interface.

This spec covers video encoding; D3D12 image encoding is covered separately.

## Video encoding on D3D11

Video encoding on D3D11 is done via an extension mechanism, passing through parameters to D3D11 drivers. Hardware-specific Media Foundation transforms are provided by IHVs, who know which extensions to use in order to communicate with the drivers. In this way, applications can make use of video encoding capabilities via [Media Foundation](/windows/win32/medfound/microsoft-media-foundation-sdk).

The D3D12 API provides a consistent and unified interface to expose the low level hardware acceleration capabilities that can be used to write video encoding applications.

## Scenarios

### OneCore

The D3D12 video API enables portable hardware-accelerated video encoding on newer platforms where only D3D12 is available. This includes the various OneCore SKUs used by cloud compute and IoT platforms. Video encoding acceleration will be now available in this scenarios without the need for using platform specific solutions.

### Media APIs

This API provides access to video encoding capabilities in a low level and portable way across all hardware vendors. This allows higher level Media APIs (such as Media Foundation) to build their media layers on top of this API which takes care of abstracting the different hardware platforms. Given the low level design of the API, these higher level media layers can optimize for their scenarios by having fine grain control of synchronization and memory allocation/residency aspects of the video encode session such as full control of the reference picture management and bitstream headers writing responsibilities. This shift of responsibilities to the layer sitting above this API also allows hardware vendors to have a consistent set of encoding policies (eg. DPB heuristics such as adaptive GOP) in the media layer that can be reused across different hardware platforms.

### Interoperability with D3D graphics, compute, and machine learning

The D3D12 video encode API enables efficient interoperability between D3D12 video encode and D3D12 graphics, compute, and machine learning scenarios, which is interesting for scenarios such as running machine learning inference over a camera stream.

### Game streaming scenarios

The D3D12 video encode API enables game streaming scenarios that require a highly performant low level API.

## Codecs support extensibility

The main supported codecs are H264 and HEVC, but with open extensibility for newer codecs such as AV1. The codec-specific aspects of the API are delegated to codec-specific structures and their access to union types. The extension process to support a new codec is the following:

1. Extend the codecs enum with the new codec.
2. Create the codec-specific support flags and configuration structures and add it to the respective union types.
3. Create the codec-specific picture control structures and add it to the respective union types.
4. (If applicable) Extend the API to add new subregion partition modes following the same pattern exposed in this API for slice-based subregion partitioning. A common example is adding support for tiles, which can be combined with

<!--- Above sentence is incomplete: "combined with" what?? --->

Note: To preserve the binary interface compatibility on extensibility, the union types always contain pointers to the codec-specific structures. The union types will always have a constant size based on the pointer size of the host architecture. This decision also prevents structures holding members of (or containing anonymous) union types from changing their type sizes when extending the interface. Some of the unions today only contain pointers to enum types, but to be consistent with this, they were also referenced as pointers in the case a new codec requires some more complex type than an enum to represent those concepts.

## Responsibilities separation between D3D12 API and Helper layer

The D3D12 API is designed to be a lower level API than the D3D11-like APIs, giving more control to the host in some aspects such as final bitstream header coding, frame reference management and exposing more complex synchronization mechanisms and explicit memory management.

The optional separate helper layer placed on top of this API interface has responsibilities such as the following:

* Produces the full encoded bitstream based on the D3D12 API payload output and subregion (eg. slice) headers. This includes handling SEI, VUI, VPS, SPS, PPS, and so forth.

* A reference picture management component that manages the reconstructed picture allocations and residency, B-frame reordering, and reference frames usage strategy.

* Delegation pattern for some of the D3D12 API features such as rate control, intra-refresh, encoder support cap queries, and so forth.

* Maps some of the finer grain control to higher level concepts, abstracting some of the lower level configuration options such as codec config flags.

* Overall, provides a higher level API for Video Encode by taking care of the D3D12 explicit memory management and synchronization aspects of this API into a simpler and higher level interface. This includes managing the command recording and submission, resource barriers, reference picture management related allocations and residency policies, etc.

The following diagram shows the D3D12 API versus helper layer interaction.

:::image type="content" source="images/d3d12-api-vs-helper-layer-interaction.jpg" alt-text="Shows the D3D12 API versus helper layer interaction.":::

The term "host" in this documentation refers to any user of the D3D12 lower level API. The helper layer is a particular instance of a host that takes care of some of the low level responsibilities and provides a higher level interface for entry level end users. Advanced users can use the D3D12 API directly without the helper layer.

## API and DDI similarities

The next sections detail the API and DDI for video encoding. In many cases, the DDI is extremely similar to the API. The structures and enumerations which are basically the same (differing solely in name convention) are not repeated in the this specification. We include just the DDI structures/enumerations and functions that differ substantially from the API.


DirectX VA permits one or more stages of the video decoding process to be divided between the *host CPU* and the video hardware accelerator. The accelerator executes the [motion-compensated prediction](motion-compensated-prediction.md) (MCP), and can also execute the inverse discrete-cosine transform (IDCT) and the variable-length decoding (VLD) stages of the decoding process.

The DirectX VA API decodes a single video stream. Support of multiple video streams requires a separate DirectX VA session for each video stream (for example, a separate pair of output and input pins for the video decoder and acceleration driver to use in filter graph operation). For more information about a filter graph, see [KS Minidriver Architecture](../stream/ks-minidriver-architecture.md).

 

## DDIs???????????????????

<!--- What is WDK-equivalent for 3.1.1. ENUM: D3D12_FEATURE_VIDEO:? --->

3.1.2
Yes, use   ENUM: d3d12umddi.D3D12DDI_VIDEO_ENCODER_CODEC_0080

<!--- What is WDK-equivalent for
3.1.3. STRUCT: D3D12_FEATURE_DATA_VIDEO_ENCODER_CODEC

--->

3.1.4. ENUM: D3D12DDI_VIDEO_ENCODER_PROFILE_H264_0080
3.1.5. ENUM: D3D12DDI_VIDEO_ENCODER_PROFILE_HEVC_0080
Yes, use  3.1.6: struct D3D12DDI_VIDEO_ENCODER_PROFILE_DESC_0080_2
3.1.7 enum: D3D12DDI_VIDEO_ENCODER_LEVELS_H264_0080
3.1.8 enum D3D12DDI_VIDEO_ENCODER_TIER_HEVC_0080
3.1.9 enum D3D12DDI_VIDEO_ENCODER_LEVELS_HEVC_0080
3.1.10 struct D3D12DDI_VIDEO_ENCODER_LEVEL_TIER_CONSTRAINTS_HEVC_0080
3.1.11 struct D3D12DDI_VIDEO_ENCODER_LEVEL_SETTING_0080_2
3.1.12 struct D3D12DDICAPS_VIDEO_ENCODER_PROFILE_LEVEL_DATA_0080_2
3.1.13 struct D3D12DDI_VIDEO_ENCODER_PICTURE_RESOLUTION_RATIO_DESC_0080
3.1.14 struct D3D12DDICAPS_VIDEO_ENCODER_OUTPUT_RESOLUTION_RATIOS_COUNT_DATA_0080_2
3.1.15 struct D3D12DDI_VIDEO_ENCODER_PICTURE_RESOLUTION_DESC_0080
3.1.16 struct D3D12DDICAPS_VIDEO_ENCODER_OUTPUT_RESOLUTION_DATA_0080_2
3.1.17 struct D3D12DDICAPS_VIDEO_ENCODER_INPUT_FORMAT_DATA_0080_2
3.1.18 enum D3D12DDI_VIDEO_ENCODER_RATE_CONTROL_MODE_0080
3.1.19 struct D3D12DDICAPS_VIDEO_ENCODER_RATE_CONTROL_MODE_DATA_0080
3.1.20 enum D3D12DDI_VIDEO_ENCODER_INTRA_REFRESH_MODE_0080
3.1.21 struct D3D12DDICAPS_VIDEO_ENCODER_INTRA_REFRESH_MODE_DATA_0080_2
3.1.22 enum D3D12DDI_VIDEO_ENCODER_FRAME_SUBREGION_LAYOUT_MODE_0080
3.1.23 struct D3D12DDICAPS_VIDEO_ENCODER_FRAME_SUBREGION_LAYOUT_MODE_DATA_0080_2
3.1.24 enum D3D12DDI_VIDEO_ENCODER_HEAP_FLAGS_0080
3.1.25 struct D3D12DDIARG_CREATE_VIDEO_ENCODER_HEAP_0080_2
3.1.26 struct D3D12DDICAPS_VIDEO_ENCODER_HEAP_SIZE_DATA_0080_2
3.1.27 enum D3D12DDI_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_H264_FLAGS_0080
3.1.28 enum D3D12DDI_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODES_0082_0
3.1.29 enum D3D12DDI_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_SLICES_DEBLOCKING_MODE_FLAGS_0082_0
3.1.30 struct D3D12DDI_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_H264_0082_0
3.1.31 enum D3D12DDI_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_HEVC_FLAGS_0083_0
3.1.32 enum D3D12DDI_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_CUSIZE_0080
3.1.33 enum D3D12DDI_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_TUSIZE_0082_0
3.1.34 struct D3D12DDI_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_HEVC_0082_0
3.1.35 struct D3D12DDI_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_0082_0
3.1.36 struct D3D12DDICAPS_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_DATA_0082_0
3.1.37 struct D3D12DDI_VIDEO_ENCODER_CODEC_PICTURE_CONTROL_SUPPORT_H264_0080_2
3.1.38 struct D3D12DDI_VIDEO_ENCODER_CODEC_PICTURE_CONTROL_SUPPORT_HEVC_0080_2
3.1.39 struct D3D12DDI_VIDEO_ENCODER_CODEC_PICTURE_CONTROL_SUPPORT_0080_2
3.1.40 struct D3D12DDICAPS_VIDEO_ENCODER_CODEC_PICTURE_CONTROL_SUPPORT_DATA_0080_2
3.1.41 enum D3D12DDI_VIDEO_ENCODER_SUPPORT_FLAGS_0082_0
3.1.42 enum D3D12DDI_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_DIRECT_MODES_0080
3.1.43 enum D3D12DDI_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_FLAGS_0080
3.1.44 struct D3D12DDI_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_0080_2
3.1.45 enum D3D12DDI_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_FLAGS_0082_0
3.1.46 struct D3D12DDI_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_0082_0
Yes, use 3.1.47 struct D3D12DDI_VIDEO_ENCODER_CODEC_CONFIGURATION_0080_2
3.1.48 struct D3D12DDI_VIDEO_ENCODER_INTRA_REFRESH_0080
Yes, use  3.1.49 enum D3D12DDI_VIDEO_ENCODER_MOTION_ESTIMATION_PRECISION_MODE_0080
3.1.50 struct D3D12DDI_VIDEO_ENCODER_RESOLUTION_SUPPORT_LIMITS_0080_2
3.1.51 enum D3D12DDI_VIDEO_ENCODER_VALIDATION_FLAGS_0082_0
3.1.52 struct D3D12DDI_VIDEO_ENCODER_SEQUENCE_GOP_STRUCTURE_H264_0082_0
3.1.53 struct D3D12DDI_VIDEO_ENCODER_SEQUENCE_GOP_STRUCTURE_HEVC_0082_0
3.1.54 struct D3D12DDI_VIDEO_ENCODER_SEQUENCE_GOP_STRUCTURE_0082_0
3.1.55 struct D3D12DDICAPS_VIDEO_ENCODER_SUPPORT_DATA_0082_0
3.1.56 struct D3D12DDICAPS_VIDEO_ENCODER_RESOURCE_REQUIREMENTS_DATA_0080_2

## 3.2 Video encoder DDI support

See note about IsSupported

## Rate Control

### API

4.1 enum D3D12DDI_VIDEO_ENCODER_RATE_CONTROL_FLAGS_0080
4.2 struct D3D12DDI_VIDEO_ENCODER_RATE_CONTROL_CONFIGURATION_PARAMS_0080_2
4.3 struct D3D12DDI_VIDEO_ENCODER_RATE_CONTROL_0080_2
4.4 struct D3D12DDI_VIDEO_ENCODER_RATE_CONTROL_CQP_0080
4.5 struct D3D12DDI_VIDEO_ENCODER_RATE_CONTROL_CBR_0080
4.6 struct D3D12DDI_VIDEO_ENCODER_RATE_CONTROL_VBR_0080
4.7 struct D3D12DDI_VIDEO_ENCODER_RATE_CONTROL_QVBR_0080_2

### Rate Control DDI
Same as API

## Video encoder creation

### API

Yes, use 5.1.1 enum D3D12DDI_VIDEO_ENCODER_FLAGS_0080
5.1.2 See 5.2.1
5.1.3-end: Interfaces and methods

5.2 Video encoder creation DDI
5.2.1 struct D3D12DDIARG_CREATE_VIDEO_ENCODER_0082_0
*** DONE *** 5.2.2 (APIENTRY* PFND3D12DDI_CALCPRIVATEVIDEOENCODERSIZE_0082_0)
5.2.3 (APIENTRY* PFND3D12DDI_CREATEVIDEOENCODER_0082_0)
5.2.4 ( APIENTRY* PFND3D12DDI_DESTROYVIDEOENCODER_0080 )
5.2.5 struct D3D12DDIARG_CREATE_VIDEO_ENCODER_HEAP_0080_2    Spec says this should be _0082_0??
5.2.6 (APIENTRY* PFND3D12DDI_CALCPRIVATEVIDEOENCODERHEAPSIZE_0080_2)
5.2.7 ( APIENTRY* PFND3D12DDI_CREATEVIDEOENCODERHEAP_0080_2 )
5.2.8 ( APIENTRY* PFND3D12DDI_DESTROYVIDEOENCODERHEAP_0080 )
5.2.9 D3D12DDI_DEVICE_FUNCS_CORE modified to include new object creation methods and query caps
5.2.10 Add D3D12DDI_DEVICE_FUNCS_VIDEO_VERSION?? struct to include new functions for video encoder create/destroy

##  Encoding operation

Several tables

6.1 Encoding operation API

6.1.1 enum D3D12DDI_VIDEO_ENCODER_FRAME_TYPE_H264_0080
6.1.2 struct D3D12DDI_VIDEO_ENCODER_REFERENCE_PICTURE_DESCRIPTOR_H264_0080
6.1.3 enum D3D12DDI_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_H264_FLAGS_0080
6.1.4 struct D3D12DDI_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_H264_REFERENCE_PICTURE_MARKING_OPERATION_0080
6.1.5 struct D3D12DDI_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_H264_REFERENCE_PICTURE_LIST_MODIFICATION_OPERATION_0082
6.1.6 struct D3D12DDI_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_H264_0082_0
6.1.7 enum D3D12DDI_VIDEO_ENCODER_FRAME_TYPE_HEVC_0080
6.1.8 struct D3D12DDI_VIDEO_ENCODER_REFERENCE_PICTURE_DESCRIPTOR_HEVC_0080
6.1.9 enum D3D12DDI_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_HEVC_FLAGS_0080
6.1.10 struct D3D12DDI_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_HEVC_0080_2
6.1.11 struct D3D12DDI_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_0080_2
6.1.12 struct D3D12DDI_VIDEO_ENCODE_REFERENCE_FRAMES_0080
6.1.13 enum D3D12DDI_VIDEO_ENCODER_PICTURE_CONTROL_FLAGS_0080
6.1.14 struct D3D12DDI_VIDEO_ENCODER_PICTURE_CONTROL_DESC_0080_2 OR struct D3D12DDI_VIDEO_ENCODER_PICTURE_CONTROL_DESC_0082_0
6.1.15 enum D3D12DDI_VIDEO_ENCODER_SEQUENCE_CONTROL_FLAGS_0082_0
6.1.16 struct D3D12DDI_VIDEO_ENCODER_PICTURE_CONTROL_SUBREGIONS_LAYOUT_DATA_SLICES_0080
6.1.17 struct D3D12DDI_VIDEO_ENCODER_PICTURE_CONTROL_SUBREGIONS_LAYOUT_DATA_0080_2
6.1.18 struct D3D12DDI_VIDEO_ENCODER_SEQUENCE_CONTROL_DESC_0080_2 OR struct D3D12DDI_VIDEO_ENCODER_SEQUENCE_CONTROL_DESC_0082_0
6.1.19 missing from spec
6.1.20 struct D3D12DDI_VIDEO_ENCODER_ENCODEFRAME_INPUT_STREAM_ARGUMENTS_0082_0
6.1.21 struct D3D12DDI_VIDEO_ENCODER_COMPRESSED_BITSTREAM_0080
6.1.22 struct D3D12DDI_VIDEO_ENCODE_RECONSTRUCTED_PICTURE_0080
6.1.23 struct D3D12DDI_VIDEO_ENCODER_FRAME_SUBREGION_METADATA_0080
6.1.24 enum D3D12DDI_VIDEO_ENCODER_ENCODE_ERROR_FLAGS_0082_0
6.1.25 struct D3D12DDI_VIDEO_ENCODER_METADATA_STATISTICS_0083_0
6.1.26 struct D3D12DDI_VIDEO_ENCODER_OUTPUT_METADATA_0083_0
6.1.27 struct D3D12DDI_VIDEO_ENCODER_ENCODE_OPERATION_METADATA_BUFFER_0080_2
6.1.28 struct D3D12DDI_VIDEO_ENCODER_RESOLVE_METADATA_INPUT_ARGUMENTS_0080_2
6.1.29 struct D3D12DDI_VIDEO_ENCODER_RESOLVE_METADATA_OUTPUT_ARGUMENTS_0082_0 or 0080_2
6.1.30 struct D3D12DDI_VIDEO_ENCODER_ENCODEFRAME_OUTPUT_STREAM_ARGUMENTS_0080_2
6.1.31 interface
6.1.32 Method
6.1.33 Method

### 6.2 DDI

Substantially different structs/funcs:

6.2.1 see 6.1.20
6.2.2 see 6.1.21
6.2.3 see 6.1.22
6.2.4 see 6.1.27
6.2.5 see 6.1.30
6.2.6 ( APIENTRY* PFND3D12DDI_VIDEO_ENCODE_FRAME_0082_0 )
6.2.7 ( APIENTRY* PFND3D12DDI_VIDEO_ENCODE_RESOLVE_OUTPUT_METADATA_0082_0 )

## Other video encode command list requirements

????? For WDK???

## Testing

See spec for several HLK tests to document

## High-level host usage flow example for the D3D12 API



# Questions for Sil

What is DataSize for various structs/enums?
