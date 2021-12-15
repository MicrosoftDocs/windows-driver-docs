---
title: Universal camera driver structures for Windows 10
description: Provides information about universal camera driver structures for Windows 10.
ms.date: 03/23/2021
---

# Universal camera driver structures for Windows 10

The camera driver interface for Windows 10 is converged for all devices and uses a universal camera driver model.

The following topics provide information about universal camera driver structures for Windows 10:

| Title | Description |
|--|--|
| [CapturedMetadataExposureCompensation](/windows/win32/api/mfapi/ns-mfapi-capturedmetadataexposurecompensation) | This structure contains blob information for the EV compensation feedback for the photo captured. |
| [CapturedMetadataISOGains](/windows/win32/api/mfapi/ns-mfapi-capturedmetadataisogains) | The CapturedMetadataISOGains structure describes the blob format for MF_CAPTURE_METADATA_ISO_GAINS. |
| [CapturedMetadataWhiteBalanceGains](/windows/win32/api/mfapi/ns-mfapi-capturedmetadatawhitebalancegains) | This structure describes the blob format for the MF_CAPTURE_METADATA_WHITEBALANCE_GAINS attribute. |
| [FaceCharacterization](/windows/win32/api/mfapi/ns-mfapi-facecharacterization) | The FaceCharacterization structure describes the blob format for the MF_CAPTURE_METADATA_FACEROICHARACTERIZATIONS attribute. |
| [FaceCharacterizationBlobHeader](/windows/win32/api/mfapi/ns-mfapi-facecharacterizationblobheader) | The FaceCharacterizationBlobHeader structure describes the size and count information of the blob format for the MF_CAPTURE_METADATA_FACEROICHARACTERIZATIONS attribute. |
| [FaceRectInfo](/windows/win32/api/mfapi/ns-mfapi-facerectinfo) | The FaceRectInfo structure describes the blob format for the MF_CAPTURE_METADATA_FACEROIS attribute. |
| [FaceRectInfoBlobHeader](/windows/win32/api/mfapi/ns-mfapi-facerectinfoblobheader) | The FaceRectInfoBlobHeader structure describes the size and count information of the blob format for the MF_CAPTURE_METADATA_FACEROIS attribute. |
| [HistogramBlobHeader](/windows/win32/api/mfapi/ns-mfapi-histogramblobheader) | The HistogramBlobHeader structure describes the blob size and the number of histograms in the blob for the MF_CAPTURE_METADATA_HISTOGRAM attribute. |
| [HistogramDataHeader](/windows/win32/api/mfapi/ns-mfapi-histogramdataheader) | The HistogramDataHeader structure describes the blob format for the MF_CAPTURE_METADATA_HISTOGRAM attribute. |
| [HistogramGrid](/windows/win32/api/mfapi/ns-mfapi-histogramgrid) | The HistogramGrid structure describes the blob format for MF_CAPTURE_METADATA_HISTOGRAM. |
| [HistogramHeader](/windows/win32/api/mfapi/ns-mfapi-histogramheader) | The HistogramHeader structure describes the blob format for MF_CAPTURE_METADATA_HISTOGRAM. |
| [KSCAMERA_EXTENDEDPROP_HEADER](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) | The KSCAMERA_EXTENDEDPROP_HEADER structure is the payload header for an extend control property. |
| [KSCAMERA_EXTENDEDPROP_METADATAINFO](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_metadatainfo) | This structure represents the metadata information for the extended property control. |
| [KSCAMERA_EXTENDEDPROP_PHOTOMODE](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_photomode) | The KSCAMERA_EXTENDEDPROP_PHOTOMODE structure contains the property data for the history frame counts in photo mode. |
| [KSCAMERA_EXTENDEDPROP_PROFILE](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_kscamera_extendedprop_profile) | The payload of the KSPROPERTY_CAMERACONTROL_EXTENDED_PROFILE control contains KSCAMERA_EXTENDEDPROP_HEADER + KSCAMERA_EXTENDEDPROP_PROFILE. |
| [KSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPS](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_roi_configcaps) | This structure contains the capabilities for an ROI control. |
| [KSCAMERA_EXTENDEDPROP_ROI_CONFIGCAPSHEADER](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_roi_configcapsheader) | This structure contains the header information for ROI capabilities. |
| [KSCAMERA_EXTENDEDPROP_ROI_EXPOSURE](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_roi_exposure) | This structure contains the ROI info structure for exposure. |
| [KSCAMERA_EXTENDEDPROP_ROI_FOCUS](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_roi_focus) | This structure contains the ROI info structure for focus. |
| [KSCAMERA_EXTENDEDPROP_ROI_INFO](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_roi_info) | This structure contains information about an ROI. |
| [KSCAMERA_EXTENDEDPROP_ROI_ISPCONTROL](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_roi_ispcontrol) | This structure contains information for an ROI ISP control. |
| [KSCAMERA_EXTENDEDPROP_ROI_ISPCONTROLHEADER](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_roi_ispcontrolheader) | This structure contains the header information for ROI ISP controls. |
| [KSCAMERA_EXTENDEDPROP_ROI_WHITEBALANCE](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_roi_whitebalance) | This structure contains the ROI info structure for white balance. |
| [KSCAMERA_METADATA_ITEMHEADER](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_metadata_itemheader) | This structure contains the metadata header information that is filled by the camera driver. |
| [KSCAMERA_METADATA_PHOTOCONFIRMATION](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_metadata_photoconfirmation) | This structure contains the photo confirmation metadata information that is filled by the camera driver. |
| [KSCAMERA_PERFRAMESETTING_CAP_HEADER](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-kscamera_perframesetting_cap_header) | This structure contains the header information for the per frame settings capabilities. |
| [KSCAMERA_PERFRAMESETTING_CAP_ITEM_HEADER](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-kscamera_perframesetting_cap_item_header) | This structure contains the header information for a per-frame settings item. |
| [KSCAMERA_PERFRAMESETTING_CUSTOM_ITEM](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-kscamera_perframesetting_custom_item) | This structure contains a custom item. |
| [KSCAMERA_PERFRAMESETTING_FRAME_HEADER](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-kscamera_perframesetting_frame_header) | This structure contains the header information for a frame in a per-frame settings payload. |
| [KSCAMERA_PERFRAMESETTING_HEADER](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-kscamera_perframesetting_header) | This structure contains header information for the per-frame settings payload. |
| [KSCAMERA_PERFRAMESETTING_ITEM_HEADER](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-kscamera_perframesetting_item_header) | This structure contains the header information for a per-frame settings item. |
| [KSCAMERA_PROFILE_CONCURRENCYINFO](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_kscamera_profile_concurrencyinfo) | An array of KSCAMERA_PROFILE_CONCURRENCYINFO structures from the camera. |
| [KSCAMERA_PROFILE_INFO](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_kscamera_profile_info) | The KSCAMERA_PROFILE_INFO structure is used to uniquely identify a given profile. |
| [KSCAMERA_PROFILE_MEDIAINFO](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_kscamera_profile_mediainfo) | This structure contains the relevant media type information presented for each camera profile. |
| [KSCAMERA_PROFILE_PININFO](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_kscamera_profile_pininfo) | This structure specifies the available list of media types for each of the camera driver pins. |
| [KSDEVICE_PROFILE_INFO](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ksdevice_profile_info) | The KSDEVICE_PROFILE_INFO is a generic structure designed to handle profile information for various device types. |
| [KSDEVICE_THERMAL_DISPATCH](/windows-hardware/drivers/ddi/ks/ns-ks-_ksdevice_thermal_dispatch) | The KSDEVICE_THERMAL_DISPATCH structure is used by the miniport driver in the API call to register thermal notification callbacks. This structure contains the callback function pointers for active and passive cooling interfaces. |
| [KSPIN_MDL_CACHING_NOTIFICATION](/windows-hardware/drivers/ddi/ks/ns-ks-kspin_mdl_caching_notification) | This structure is used internally by the operating system. |
| [KSPIN_MDL_CACHING_NOTIFICATION32](/windows-hardware/drivers/ddi/ks/ns-ks-kspin_mdl_caching_notification32) | This structure is used internally by the operating system. |
| [KSPROPERTY_STEPPING_LONG](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_stepping_long) | The KSPROPERTY_STEPPING_LONG structure defines the valid range of values for a 32-bit property. |
| [KSPROPERTY_STEPPING_LONGLONG](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_stepping_longlong) | The KSPROPERTY_STEPPING_LONGLONG structure defines the valid range of values for a 64-bit property. |
| [KSSTREAM_METADATA_INFO](/windows-hardware/drivers/ddi/ks/ns-ks-ksstream_metadata_info) | This structure contains the metadata information that is passed down to the driver. |
| [KSSTREAM_UVC_METADATA](/windows-hardware/drivers/ddi/ks/ns-ks-ksstream_uvc_metadata) | The KSSTREAM_UVC_METADATA structure contains start and end of frame timestamp information. |
| [KSSTREAM_UVC_METADATATYPE_TIMESTAMP](/windows-hardware/drivers/ddi/ks/ns-ks-ksstream_uvc_metadatatype_timestamp) | The KSSTREAM_UVC_METADATATYPE_TIMESTAMP structure contains USB video class (UVC) clock and timestamp information. |
| [MetadataTimeStamps](/windows/win32/api/mfapi/ns-mfapi-metadatatimestamps) | The MetadataTimeStamps structure describes the blob format for the MF_CAPTURE_METADATA_FACEROITIMESTAMPS attribute. |
| [MF_MDL_SHARED_PAYLOAD_KEY](/windows-hardware/drivers/ddi/ks/ns-ks-_mf_mdl_shared_payload_key) | This union is used internally by the operating system. |

## See also

[Universal camera driver design guide for Windows 10](windows-10-technical-preview-camera-drivers-design-guide.md)

[Universal camera driver controls for Windows 10](camera-driver-controls.md)

[Universal camera driver enumerations for Windows 10](camera-driver-enumerations.md)

[Universal camera driver functions for Windows 10](camera-driver-functions.md)

[Streaming media device driver reference](/windows-hardware/drivers/ddi/_stream/index)
