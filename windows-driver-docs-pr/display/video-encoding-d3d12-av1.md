---
title: D3D12 AV1 Video Encoding
description: Describes the points of extension to D3D12 video encoding to support AV1 Encode.
keywords:
- D3D12 , video encoding
- D3D12 , AV1 video encoding
- Direct3D12 , video encoding
ms.date: 04/24/2025
---

# D3D12 AV1 video encoding

The Direct3D12 video encoding feature is extended to support AV1 encoding starting in Windows 11, version 24H2 (WDDM 3.2). This article describes the points of extension where the existing [D3D12 Video Encoding](video-encoding-d3d12.md) DDI needs modifications and new structures to support AV1 encoding. For more information, including application-level specifics, see the [AV1 D3D12 Video Encoding Specification](https://microsoft.github.io/DirectX-Specs/d3d/D3D12_Video_Encoding_AV1.html).

## Extensions to rate control

The following existing enumerations are updated with extensions to rate control and rate control support:

* Rate control support flags are added to [**D3D12DDI_VIDEO_ENCODER_SUPPORT_FLAGS_0083_0**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_video_encoder_support_flags_0083_0)

* Rate control flags are added to [**D3D12DDI_VIDEO_ENCODER_RATE_CONTROL_FLAGS_0080**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_video_encoder_rate_control_flags_0080)

* The following extended (*Extension 1*) **D3D12DDI_VIDEO_ENCODER_RATE_CONTROL_*XXX1*** structures are added and [**D3D12DDI_VIDEO_ENCODER_RATE_CONTROL_CONFIGURATION_PARAMS**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_rate_control_configuration_params_0080_2) is updated to include them. **QualityVsSpeed** is added to all modes and **VBVCapacity** and **InitialVBVFullness** are added to ***_QVBR1*** in addition.

  * [**D3D12DDI_VIDEO_ENCODER_RATE_CONTROL_CQP1_0096**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_rate_control_cqp1_0096)
  * [**D3D12DDI_VIDEO_ENCODER_RATE_CONTROL_CBR1_0096**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_rate_control_cbr1_0096)
  * [**D3D12DDI_VIDEO_ENCODER_RATE_CONTROL_VBR1_0096**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_rate_control_vbr1_0096)
  * [**D3D12DDI_VIDEO_ENCODER_RATE_CONTROL_QVBR1_0096**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_rate_control_qvbr1_0096)
  * [**D3D12DDI_VIDEO_ENCODER_RATE_CONTROL_ABSOLUTE_QP_MAP_0096**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_rate_control_absolute_qp_map_0096)

When **D3D12DDI_VIDEO_ENCODER_RATE_CONTROL_FLAG_0096_ENABLE_EXTENSION1_SUPPORT** is enabled, the extended rate control structures are used in [**D3D12DDI_VIDEO_ENCODER_RATE_CONTROL_CONFIGURATION_PARAMS_0080_2.pConfiguration_*XXX***](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_rate_control_configuration_params_0080_2); otherwise the legacy structures are used when disabled per the table documented on the **D3D12DDI_VIDEO_ENCODER_RATE_CONTROL_FLAGS_0080** reference page.

## Video encoding support extensions

The existing video-related framework is extended to allow drivers to report AV1 video encoding support and capabilities. This section lists the added or updated structures and enumerations that are used to query and report AV1 video encoding support.

* **D3D12DDI_FEATURE_VERSION_VIDEO_0095_0** is the version number that defines the minimum implementation of all D3D12 video encode milestones that were introduced in Windows 11, version 24H2 (WDDM 3.2)

* The [**D3D12DDICAPS_TYPE_VIDEO_0020**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddicaps_type_video_0020) enumeration was extended to include the following video encoding support values:

  * D3D12DDICAPS_TYPE_VIDEO_0095_ENCODER_FRAME_SUBREGION_LAYOUT_CONFIG
  * D3D12DDICAPS_TYPE_VIDEO_0096_ENCODER_SUPPORT1

* **D3D12DDI_VIDEO_ENCODER_CODEC_0095_AV1** is added to [**D3D12DDI_VIDEO_ENCODER_CODEC_0080**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_video_encoder_codec_0080)

* The [**D3D12DDI_VIDEO_ENCODER_AV1_PROFILE_0095**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_video_encoder_av1_profile_0095) enumeration was added to define the AV1 profiles supported by the driver. The driver uses [**D3D12DDICAPS_VIDEO_ENCODER_INPUT_FORMAT_DATA_0080_2**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddicaps_video_encoder_input_format_data_0080_2) to report optionally supported formats for a given **D3D12DDI_VIDEO_ENCODER_AV1_PROFILE_0095** input to the query.

* [**D3D12DDI_VIDEO_ENCODER_PROFILE_DESC_0080_2**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_profile_desc_0080_2) is updated to include the AV1 profile (**pAV1Profile**).

* The following structures and enumerations are added or extended to support AV1 encoding:

  * [**D3D12DDI_VIDEO_ENCODER_AV1_LEVELS_0095**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_video_encoder_av1_levels_0095)

  * [**D3D12DDI_VIDEO_ENCODER_AV1_TIER_0095**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_video_encoder_av1_tier_0095)

  * [**D3D12DDI_VIDEO_ENCODER_AV1_LEVEL_TIER_CONSTRAINTS_0095**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_av1_level_tier_constraints_0095) (**pAV1LevelSetting** is added to [**D3D12DDI_VIDEO_ENCODER_LEVEL_SETTING_0080_2**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_level_setting_0080_2))

  * [**D3D12DDI_VIDEO_ENCODER_FRAME_SUBREGION_LAYOUT_MODE_0080**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_video_encoder_frame_subregion_layout_mode_0080) is extended to include D3D12DDI_VIDEO_ENCODER_FRAME_SUBREGION_LAYOUT_MODE_0095_UNIFORM_GRID_PARTITION and D3D12DDI_VIDEO_ENCODER_FRAME_SUBREGION_LAYOUT_MODE_0095_CONFIGURABLE_GRID_PARTITION.

  * **D3D12DDI_VIDEO_ENCODER_MOTION_ESTIMATION_PRECISION_MODE_EIGHTH_PIXEL_0095** is added to [**D3D12DDI_VIDEO_ENCODER_MOTION_ESTIMATION_PRECISION_MODE_0080**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_video_encoder_motion_estimation_precision_mode_0080)

  * [**D3D12DDI_VIDEO_ENCODER_AV1_FEATURE_0095_FLAGS**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_video_encoder_av1_feature_0095_flags)

  * [**D3D12DDI_VIDEO_ENCODER_AV1_TX_MODE_0095**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_video_encoder_av1_tx_mode_0095) and [**D3D12DDI_VIDEO_ENCODER_AV1_TX_MODE_0095_FLAGS**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_video_encoder_av1_tx_mode_0095_flags)

  * [**D3D12DDI_VIDEO_ENCODER_AV1_INTERPOLATION_FILTERS_0095**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_video_encoder_av1_interpolation_filters_0095) and [**D3D12DDI_VIDEO_ENCODER_AV1_INTERPOLATION_FILTERS_0095_FLAGS**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_video_encoder_av1_interpolation_filters_0095_flags)

  * [**D3D12DDI_VIDEO_ENCODER_AV1_SEGMENTATION_BLOCK_SIZE_0095**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_video_encoder_av1_segmentation_block_size_0095)

  * [**D3D12DDI_VIDEO_ENCODER_AV1_SEGMENTATION_MODE_0095**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_video_encoder_av1_segmentation_mode_0095) and [**D3D12DDI_VIDEO_ENCODER_AV1_SEGMENTATION_MODE_0095_FLAGS**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_video_encoder_av1_segmentation_mode_0095_flags)

  * [**D3D12DDI_VIDEO_ENCODER_AV1_RESTORATION_TYPE_0095**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_video_encoder_av1_restoration_type_0095)

  * [**D3D12DDI_VIDEO_ENCODER_AV1_RESTORATION_TILESIZE_0095**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_video_encoder_av1_restoration_tilesize_0095)

  * [**D3D12DDI_VIDEO_ENCODER_AV1_REFERENCE_WARPED_MOTION_TRANSFORMATION_0095**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_video_encoder_av1_reference_warped_motion_transformation_0095) and [**D3D12DDI_VIDEO_ENCODER_AV1_REFERENCE_WARPED_MOTION_TRANSFORMATION_0095_FLAGS**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_video_encoder_av1_reference_warped_motion_transformation_0095_flags)

  * [**D3D12DDI_VIDEO_ENCODER_AV1_POST_ENCODE_VALUES_0095_FLAGS**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_video_encoder_av1_post_encode_values_0095_flags)

  * [**D3D12DDI_VIDEO_ENCODER_AV1_CODEC_CONFIGURATION_SUPPORT**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_av1_codec_configuration_support_0095), with **pAV1Support** added to [**D3D12DDI_VIDEO_ENCODER_CODEC_CONFIGURATION_SUPPORT_0083_0**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_codec_configuration_support_0083_0)

  * [**D3D12DDI_VIDEO_ENCODER_AV1_FRAME_TYPE_0095**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_video_encoder_av1_frame_type_0095) and [**D3D12DDI_VIDEO_ENCODER_AV1_FRAME_TYPE_0095_FLAGS**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_video_encoder_av1_frame_type_0095_flags)

  * [**D3D12DDI_VIDEO_ENCODER_AV1_COMP_PREDICTION_TYPE_0095**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_video_encoder_av1_comp_prediction_type_0095)

  * [**D3D12DDI_VIDEO_ENCODER_CODEC_AV1_PICTURE_CONTROL_SUPPORT_0095**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_codec_av1_picture_control_support_0095), with **pAV1Support** added to [**D3D12DDI_VIDEO_ENCODER_CODEC_PICTURE_CONTROL_SUPPORT_0080_2**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_codec_picture_control_support_0080_2)

  * [**D3D12DDI_VIDEO_ENCODER_AV1_CODEC_CONFIGURATION_0095**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_av1_codec_configuration_0095)

  * [**D3D12DDI_VIDEO_ENCODER_AV1_FRAME_SUBREGION_LAYOUT_CONFIG_SUPPORT_0095**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_av1_frame_subregion_layout_config_support_0095) and [**D3D12DDI_VIDEO_ENCODER_AV1_FRAME_SUBREGION_LAYOUT_CONFIG_VALIDATION_0095_FLAGS**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_video_encoder_av1_frame_subregion_layout_config_validation_0095_flags)

  * [**D3D12DDI_FEATURE_DATA_VIDEO_ENCODER_FRAME_SUBREGION_LAYOUT_CONFIG_0095**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_feature_data_video_encoder_frame_subregion_layout_config_0095) and [**D3D12DDI_VIDEO_ENCODER_FRAME_SUBREGION_LAYOUT_CONFIG_SUPPORT_0095**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_frame_subregion_layout_config_support_0095)

  * **pAV1Config** is added to [**D3D12DDI_VIDEO_ENCODER_CODEC_CONFIGURATION_0082_0**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_codec_configuration_0082_0)

  * The **D3D12DDI_VIDEO_ENCODER_VALIDATION_FLAG_0080_SUBREGION_LAYOUT_MODE_NOT_SUPPORTED** flag is added to [**D3D12DDI_VIDEO_ENCODER_VALIDATION_FLAGS_0080**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_video_encoder_validation_flags_0080) to use with the extended [**D3D12DDICAPS_TYPE_VIDEO_0096_ENCODER_SUPPORT1**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddicaps_type_video_0020) query cap.

  * [**D3D12DDICAPS_VIDEO_ENCODER_SUPPORT1_DATA_0096**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddicaps_video_encoder_support1_data_0096) is added to extend the previous **D3D12DDICAPS_VIDEO_ENCODER_SUPPORT_DATA_0083_0** query, with parameters added at the bottom of the structure. This extended query can be used with all H264, HEVC, and AV1 codecs and must behave exactly as D3D12_FEATURE_VIDEO_ENCODER_SUPPORT semantics.

  * The semantics for the **MaxSubregionsNumber**, **SubregionBlockPixelsSize**, and **QPMapRegionPixelsSize** members of [**D3D12DDI_VIDEO_ENCODER_RESOLUTION_SUPPORT_LIMITS_0080_2**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_resolution_support_limits_0080_2) are updated for AV1.

  * [**_D3D12DDI_VIDEO_ENCODER_AV1_SEQUENCE_STRUCTURE_0095**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_av1_sequence_structure_0095) is added, and **pAV1SequenceStructure** is added to [**D3D12DDI_VIDEO_ENCODER_SEQUENCE_GOP_STRUCTURE_0082_0**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_sequence_gop_structure_0082_0).

## Encoding operation

### Expected bitstream header values for AV1

#### Driver/host header coding responsibilities

Given an encoded frame with K tiles, the driver writes the K decode_tile() AV1 syntax elements in the compressed bitstream, corresponding to the requested tiles in [*EncodeFrame*](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_video_encode_frame_0082_0) arguments.

The API Client then builds the tile_group_obu() AV1 syntax elements with tile_start_and_end_present_flag/tg_start/tg_end elements to arrange the tiles into tile groups as desired with the condition that the tiles are placed sequentially. The tile_size_minus_1 element is coded from the related tile **D3D12_VIDEO_ENCODER_FRAME_SUBREGION_METADATA** information and decode_tile() elements are copied from the compressed bitstream buffer. Finally, each tile_group_obu() is wrapped around open_bitstream_unit() elements of type OBU_TILE_GROUP and prepended with an OBU_FRAME_HEADER. For a single tile group, an OBU_FRAME type can be used instead.

The API Client is responsible for inferring obu_extension_flag as ```!(TemporalLayerIndexPlus1 || SpatialLayerIndexPlus1)``` for the current frame and also code if necessary temporal_id and spatial_id in the open_bitstream_unit().

The *EncodeFrame* submissions are in encode order, like the other codecs implemented in the D3D12 Encode API.

#### Resolution changes and spatial scalability

If the driver reports [**D3D12_VIDEO_ENCODER_SUPPORT_FLAG_RESOLUTION_RECONFIGURATION_AVAILABLE**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_video_encoder_support_flags_0080), it still only applies to resolution changes on a key frame.

The active sequence header must have the max_frame_\*_minus_1 syntax set to the maximum resolution present in the associated ID3D12VideoEncoderHeap being used. Different frames using resolutions also present in the associated ID3D12VideoEncoderHeap can use the AV1 syntax frame_size_override_flag in frame_size() to convey change of resolution.

If D3D12_VIDEO_ENCODER_AV1_FRAME_TYPE_FLAG_SWITCH_FRAME is supported:

* The reference frames must point to higher or equal resolution than the current switch frame being encoded.
* The different resolutions must be all present in the associated ID3D12VideoEncoderHeap being used.

Similarly, if spatial scalability is supported, the different resolutions of the reference frames must be all present in the associated ID3D12VideoEncoderHeap being used.

#### Rate control notes

The accepted range for [**D3D12DDI_VIDEO_ENCODER_RATE_CONTROL_QVBR1_0096.ConstantQualityTarget**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_rate_control_qvbr1_0096) is [0..63]. The lowest value yields the highest quality.

In general, **D3D12DDI_VIDEO_ENCODER_SUPPORT_FLAG_0083_0_RATE_CONTROL_RECONFIGURATION_AVAILABLE** applies to the quality versus speed tweaking and the following rate control parameters of the different rate control modes: QP in constant QP, bitrates and quality levels in CBR, VBR and QVBR. The driver can return **D3D12DDI_VIDEO_ENCODER_ENCODE_ERROR_FLAG_0082_0_RECONFIGURATION_REQUEST_NOT_SUPPORTED** in **D3D12DDI_VIDEO_ENCODER_OUTPUT_METADATA_0083_0.EncodeErrorFlags** for other unsupported rate control parameter reconfiguration.

### Encoding operation API

The following structures and enumerations are added or updated with extensions to support the AV1 encoding operation:

* [**D3D12DDI_VIDEO_ENCODER_AV1_REFERENCE_PICTURE_WARPED_MOTION_INFO_0095**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_av1_reference_picture_warped_motion_info_0095)

* [**D3D12DDI_VIDEO_ENCODER_AV1_REFERENCE_PICTURE_DESCRIPTOR_0095**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_av1_reference_picture_descriptor_0095)

* [**D3D12DD1_VIDEO_ENCODER_AV1_PICTURE_CONTROL_0095_FLAGS**](/windows-hardware/drivers/ddi/d3d12umddi/ne-d3d12umddi-d3d12ddi_video_encoder_av1_picture_control_0095_flags)

* [**D3D12DDI_VIDEO_ENCODER_AV1_RESTORATION_CONFIG_0095**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_av1_restoration_config_0095)

* [**D3D12DDI_VIDEO_ENCODER_AV1_SEGMENT_DATA_0095**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_av1_segment_data_0095)

* [**D3D12DDI_VIDEO_ENCODER_AV1_SEGMENTATION_CONFIG_0095**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_av1_segmentation_config_0095)

* [**D3D12DDI_VIDEO_ENCODER_AV1_SEGMENTATION_MAP_0095**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_av1_segmentation_map_0095)

* [**D3D12DDI_VIDEO_ENCODER_CODEC_AV1_LOOP_FILTER_CONFIG_0095**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_codec_av1_loop_filter_config_0095)

* [**D3D12DDI_VIDEO_ENCODER_CODEC_AV1_LOOP_FILTER_DELTA_CONFIG_0095**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_codec_av1_loop_filter_delta_config_0095)

* [**D3D12DDI_VIDEO_ENCODER_CODEC_AV1_QUANTIZATION_CONFIG_0095**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_codec_av1_quantization_config_0095)

* [**D3D12DDI_VIDEO_ENCODER_CODEC_AV1_QUANTIZATION_DELTA_CONFIG_0095**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_codec_av1_quantization_delta_config_0095)

* [**D3D12DDI_VIDEO_ENCODER_AV1_CDEF_CONFIG_0095**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_av1_cdef_config_0095)

* [**D3D12DDI_VIDEO_ENCODER_AV1_PICTURE_CONTROL_CODEC_DATA_0095**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_av1_picture_control_codec_data_0095)

* **pAV1PicData** is added to [**D3D12DDI_VIDEO_ENCODER_PICTURE_CONTROL_CODEC_DATA_0082_0**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_picture_control_codec_data_0082_0)

* [**D3D12DDI_VIDEO_ENCODER_AV1_PICTURE_CONTROL_SUBREGIONS_LAYOUT_DATA_TILES_0095**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_av1_picture_control_subregions_layout_data_tiles_0095)

* **pTilesPartition_AV1** is added to [**D3D12DDI_VIDEO_ENCODER_PICTURE_CONTROL_SUBREGIONS_LAYOUT_DATA_0080_2**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_picture_control_subregions_layout_data_0080_2)

* [**D3D12DDI_VIDEO_ENCODER_AV1_POST_ENCODE_VALUES_0095**](/windows-hardware/drivers/ddi/d3d12umddi/ns-d3d12umddi-d3d12ddi_video_encoder_av1_post_encode_values_0095)

In addition, a driver's existing [**PFND3D12DDI_VIDEO_ENCODE_RESOLVE_OUTPUT_METADATA_0082_0**](/windows-hardware/drivers/ddi/d3d12umddi/nc-d3d12umddi-pfnd3d12ddi_video_encode_resolve_output_metadata_0082_0) callback needs to be updated to handle the AV1-specific resolved buffer layout added for AV1 encoding.
