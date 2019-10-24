---
title: New AVStream Interfaces for Windows 8.1
description: AVStream streaming media driver interfaces are extended to support new camera platform functionality starting with Windows 8.1.
ms.assetid: 1D06A754-236B-441D-A0BB-A78B419270E9
ms.date: 05/15/2018
ms.localizationpriority: medium
---

# New AVStream Interfaces for Windows 8.1


AVStream streaming media driver interfaces are extended to support new camera platform functionality starting with Windows 8.1.

## Camera platform


Camera controls are extended starting with Windows 8.1. For info on how to implement these camera controls, see the topics under [Camera Control Properties](camera-control-properties.md).

These device driver interfaces (DDIs) support these extensions and are new or updated:

-   [**KSCAMERA\_EXTENDEDPROP\_CAMERAOFFSET**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_cameraoffset)
-   [**KSCAMERA\_EXTENDEDPROP\_EVCOMPENSATION**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_evcompensation)
-   [**KSCAMERA\_EXTENDEDPROP\_FIELDOFVIEW**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_fieldofview)
-   [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header)
-   [**KSCAMERA\_EXTENDEDPROP\_PHOTOMODE**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_photomode)
-   [**KSCAMERA\_EXTENDEDPROP\_VALUE**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_value)
-   [**KSCAMERA\_EXTENDEDPROP\_VIDEOPROCSETTING**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_videoprocsetting)
-   [**KSCAMERA\_MAXVIDEOFPS\_FORPHOTORES**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_maxvideofps_forphotores)
-   [KSEVENTSETID\_VolumeLimit](https://docs.microsoft.com/windows-hardware/drivers/stream/kseventsetid-volumelimit)
-   [**KSEVENT\_VOLUMELIMIT\_CHANGED**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksevent-volumelimit-changed)
-   [KSPROPERTYSETID\_ExtendedCameraControl](https://docs.microsoft.com/windows-hardware/drivers/stream/kspropertysetid-extendedcameracontrol) (includes these properties:)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_CAMERAANGLEOFFSET**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-cameraangleoffset)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_EVCOMPENSATION**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-evcompensation)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_EXPOSUREMODE**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-exposuremode)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FIELDOFVIEW**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-fieldofview)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FLASHMODE**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-flashmode)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FOCUSMODE**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-focusmode)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ISO**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-iso)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_MAXVIDFPS\_PHOTORES**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-maxvidfps-photores)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_OPTIMIZATIONHINT**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-optimizationhint)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOFRAMERATE**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-photoframerate)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOMAXFRAMERATE**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-photomaxframerate)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOMODE**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-photomode)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOTHUMBNAIL**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-photothumbnail)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOTRIGGERTIME**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-phototriggertime)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_SCENEMODE**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-scenemode)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_TORCHMODE**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-torchmode)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_WARMSTART**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-warmstart)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_WHITEBALANCEMODE**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-whitebalancemode)
-   [**KSPROPERTY\_PIN\_PROPOSEDATAFORMAT2**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-pin-proposedataformat2)
-   [**KSPROPERTY\_CAMERACONTROL\_IMAGE\_PIN\_CAPABILITY\_S**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_image_pin_capability_s) (new **KSPROPERTY\_CAMERACONTROL\_IMAGE\_PIN\_CAPABILITY\_SEQUENCE\_EXCLUSIVE\_WITH\_RECORD** member)
-   [**KSP\_PIN**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin) (new **Flags** member)
-   [**KSPROPERTY\_CAMERACONTROL\_REGION\_OF\_INTEREST\_S**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_region_of_interest_s) (new **Configuration** member)
-   [**KS\_VideoControlFlags**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-ks_videocontrolflags) (new **KS\_VideoControlFlag\_StartPhotoSequenceCapture** and **KS\_VideoControlFlag\_StopPhotoSequenceCapture** constant values)
-   [**KS\_FRAME\_INFO**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_frame_info) (new **FrameCompletionNumber** member)
-   Note also the additional [KSPROPERTYSETID\_ExtendedCameraControl](https://docs.microsoft.com/windows-hardware/drivers/stream/kspropertysetid-extendedcameracontrol) property set listed in [Video Capture Minidriver Property Sets](https://docs.microsoft.com/windows-hardware/drivers/stream/video-capture-minidriver-property-sets).

 

 




