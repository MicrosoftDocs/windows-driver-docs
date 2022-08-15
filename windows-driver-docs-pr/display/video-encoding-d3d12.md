---
title: D3D12 video encoding
description: Learn about D3D12 video encoding
keywords:
- Direct3D12 video encoding
- WDDM 3.0 , video encoding
ms.date: 02/16/2022
ms.localizationpriority: medium
---

# D3D12 video encoding

This page provides general information for driver developers regarding the Direct3D12 video encoding feature. For additional information, including application-level specifics, see the [D3D Video Encoding Specification](https://microsoft.github.io/DirectX-Specs/d3d/D3D12VideoEncoding.html).

## About Direct3D 12 video encoding

Prior to Windows 11 (WDDM 3.0), DirectX 12 provided application- and driver-level interfaces (APIs and DDIs) to support GPU acceleration for several video applications, including video decoding, video processing, and motion estimation.

Starting in Windows 11, D3D12 added a video encoding feature to the existing video API/DDI family. This feature provides a coherent set of encoding APIs/DDIs that are consistent with the existing D3D12 framework, and allows developers to perform video encoding using GPU-accelerated video engines.

The video encode framework provides access to the video encode hardware acceleration capabilities for different scenarios such as Internet of Things (IoT), cloud, media APIs, machine learning and game streaming.

## Supported codecs

Starting in Windows 11, the supported codecs are H.264 and HEVC, although the D3D12 video encoding framework provides open extensibility for newer codecs such as AV1.

The codec-specific aspects of the framework's interface are delegated to codec-specific structures and their access to union types. For example, the [**D3D12DDI_VIDEO_ENCODER_CODEC_CONFIGURATION_0082_0**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_codec_configuration_0082_0) structure contains a union with pointers to codec-specific [**D3D12DDI_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_0082_0**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_codec_configuration_h264_0082_0) and [**D3D12DDI_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_0082_0**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_codec_configuration_hevc_0082_0) structures that contain the codec-specific configuration information.

To preserve the binary interface compatibility on extensibility, the union types always contain pointers to the codec-specific structures. The union types have a constant size based on the pointer size of the host architecture. This decision also prevents structures holding members of (or containing anonymous) union types from changing their type sizes when extending the interface. Some of the unions only contain pointers to enum types; to be consistent, these enum types are also referenced as pointers in the case a new codec requires some more complex type than an enum to represent those concepts.

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
