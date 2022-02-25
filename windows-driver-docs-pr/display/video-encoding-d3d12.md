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

This page provides general information and guidance for driver developers regarding the Direct3D video encoding feature. For additional information, including application-level specifics, see the [D3D Video Encoding Specification](https://microsoft.github.io/DirectX-Specs/d3d/D3D12VideoEncoding.html).

## About Direct3D 12 video encoding

Prior to Windows 11 (WDDM 3.0), DirectX 12 provided application- and driver-level interfaces (APIs and DDIs) to support GPU acceleration for several video applications, including video decoding, video processing, and motion estimation.

Starting in Windows 11, D3D12 added a video encoding feature to the existing video API/DDI family. This feature provides a coherent set of encoding APIs/DDIs that are consistent with the existing D3D12 framework, and allows developers to perform video encoding using GPU-accelerated video engines.

The video encode framework provides access to the video encode hardware acceleration capabilities for different scenarios such as Internet of Things (IoT), cloud, media APIs, machine learning and game streaming.

## Reporting video encoding support and capabilities

The video-related support framework was extended to allow drivers to report video encoding support and capabilities.

* **D3D12DDI_FEATURE_VERSION_VIDEO_0083_0** is the version number that defines the first full implementation of all D3D12 video encode milestones, introduced in Windows 11 (WDDM 3.0).
* A driver provides pointers to the core video support callback functions that it supports, including the following callbacks introduced for video encoding support, in the [**D3D12DDI_DEVICE_FUNCS_VIDEO_0082_0**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_device_funcs_video_0082_0) structure:

* [**PFND3D12DDI_CALCPRIVATEVIDEOENCODERSIZE_0082_0**](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_calcprivatevideoencodersize_0082_0)
* [**PFND3D12DDI_CREATEVIDEOENCODER_0082_0**](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_createvideoencoder_0082_0)
* [**PFND3D12DDI_DESTROYVIDEOENCODER_0080**](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_destroyvideoencoder_0080)
* [**PFND3D12DDI_CALCPRIVATEVIDEOENCODERHEAPSIZE_0080_2**](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_calcprivatevideoencoderheapsize_0080_2)
* [**PFND3D12DDI_CREATEVIDEOENCODERHEAP_0080_2**](/windows-hardware/drivers/ddi/d3d12umddi/)
* [**PFND3D12DDI_DESTROYVIDEOENCODERHEAP_0080**](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_destroyvideoencoderheap_0080)

## Creating the video encoder

## Create the video encoder heap

## Encode a frame

## Resolve?? Stats?? etc

## Destroy the video encoder and associated heap


A system-supplied helper layer was developed on top of this API interface to provide a higher level entry point for users that need a higher level interface.

## Scenarios

### OneCore

The D3D12 video API enables portable hardware-accelerated video encoding on newer platforms where only D3D12 is available. This includes the various OneCore SKUs used by cloud compute and IoT platforms. Video encoding acceleration will be now available in these scenarios without the need for using platform-specific solutions.

### Media APIs

This API provides access to video encoding capabilities in a low level and portable way across all hardware vendors. This allows higher level Media APIs (such as Media Foundation) to build their media layers on top of this API which takes care of abstracting the different hardware platforms. Given the low level design of the API, these higher level media layers can optimize for their scenarios by having fine grain control of synchronization and memory allocation/residency aspects of the video encode session such as full control of the reference picture management and bitstream headers writing responsibilities. This shift of responsibilities to the layer sitting above this API also allows hardware vendors to have a consistent set of encoding policies (eg. DPB heuristics such as adaptive GOP) in the media layer that can be reused across different hardware platforms.

### Interoperability with D3D graphics, compute, and machine learning

The D3D12 video encode API enables efficient interoperability between D3D12 video encode and D3D12 graphics, compute, and machine learning scenarios, which is interesting for scenarios such as running machine learning inference over a camera stream.

### Game streaming scenarios

The D3D12 video encode API enables game streaming scenarios that require a highly performant low level API.

## Supported codecs

Starting in Windows 11, the supported codecs are H.264 and HEVC, but the D3D12 video encoding framework provides open extensibility for newer codecs such as AV1. The codec-specific aspects of the framework's interface are delegated to codec-specific structures and their access to union types.

For example, the [**D3D12DDI_VIDEO_ENCODER_CODEC_CONFIGURATION_0082_0**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_codec_configuration_0082_0) structure contains a union with pointers to codec-specific [**D3D12DDI_VIDEO_ENCODER_CODEC_CONFIGURATION_H264_0082_0**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_codec_configuration_h264_0082_0) and [**D3D12DDI_VIDEO_ENCODER_CODEC_CONFIGURATION_HEVC_0082_0**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_codec_configuration_hevc_0082_0) structures that contain the codec-specific configuration information.

To preserve the binary interface compatibility on extensibility, the union types always contain pointers to the codec-specific structures. The union types have a constant size based on the pointer size of the host architecture. This decision also prevents structures holding members of (or containing anonymous) union types from changing their type sizes when extending the interface. Some of the unions only contain pointers to enum types; to be consistent, these enum types are also referenced as pointers in the case a new codec requires some more complex type than an enum to represent those concepts.

## API and DDI similarities

The next sections detail the API and DDI for video encoding. In many cases, the device driver interface (DDI) is extremely similar to the application-level programming interface (API).


 

## DDIs???????????????????


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
