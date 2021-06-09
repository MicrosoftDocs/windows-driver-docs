---
title: New AVStream Interfaces for Windows 8.1
description: AVStream streaming media driver interfaces are extended to support new camera platform functionality starting with Windows 8.1.
ms.date: 05/15/2018
ms.localizationpriority: medium
---

# New AVStream Interfaces for Windows 8.1


AVStream streaming media driver interfaces are extended to support new camera platform functionality starting with Windows 8.1.

## Camera platform


Camera controls are extended starting with Windows 8.1. For info on how to implement these camera controls, see the topics under [Camera Control Properties](camera-control-properties.md).

These device driver interfaces (DDIs) support these extensions and are new or updated:

-   [**KSCAMERA\_EXTENDEDPROP\_CAMERAOFFSET**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_cameraoffset)
-   [**KSCAMERA\_EXTENDEDPROP\_EVCOMPENSATION**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_evcompensation)
-   [**KSCAMERA\_EXTENDEDPROP\_FIELDOFVIEW**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_fieldofview)
-   [**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header)
-   [**KSCAMERA\_EXTENDEDPROP\_PHOTOMODE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_photomode)
-   [**KSCAMERA\_EXTENDEDPROP\_VALUE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_value)
-   [**KSCAMERA\_EXTENDEDPROP\_VIDEOPROCSETTING**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_videoprocsetting)
-   [**KSCAMERA\_MAXVIDEOFPS\_FORPHOTORES**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_maxvideofps_forphotores)
-   [KSEVENTSETID\_VolumeLimit](./kseventsetid-volumelimit.md)
-   [**KSEVENT\_VOLUMELIMIT\_CHANGED**](./ksevent-volumelimit-changed.md)
-   [KSPROPERTYSETID\_ExtendedCameraControl](./kspropertysetid-extendedcameracontrol.md) (includes these properties:)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_CAMERAANGLEOFFSET**](./ksproperty-cameracontrol-extended-cameraangleoffset.md)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_EVCOMPENSATION**](./ksproperty-cameracontrol-extended-evcompensation.md)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_EXPOSUREMODE**](./ksproperty-cameracontrol-extended-exposuremode.md)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FIELDOFVIEW**](./ksproperty-cameracontrol-extended-fieldofview.md)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FLASHMODE**](./ksproperty-cameracontrol-extended-flashmode.md)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FOCUSMODE**](./ksproperty-cameracontrol-extended-focusmode.md)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ISO**](./ksproperty-cameracontrol-extended-iso.md)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_MAXVIDFPS\_PHOTORES**](./ksproperty-cameracontrol-extended-maxvidfps-photores.md)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_OPTIMIZATIONHINT**](./ksproperty-cameracontrol-extended-optimizationhint.md)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOFRAMERATE**](./ksproperty-cameracontrol-extended-photoframerate.md)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOMAXFRAMERATE**](./ksproperty-cameracontrol-extended-photomaxframerate.md)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOMODE**](./ksproperty-cameracontrol-extended-photomode.md)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOTHUMBNAIL**](./ksproperty-cameracontrol-extended-photothumbnail.md)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOTRIGGERTIME**](./ksproperty-cameracontrol-extended-phototriggertime.md)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_SCENEMODE**](./ksproperty-cameracontrol-extended-scenemode.md)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_TORCHMODE**](./ksproperty-cameracontrol-extended-torchmode.md)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_WARMSTART**](./ksproperty-cameracontrol-extended-warmstart.md)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_WHITEBALANCEMODE**](./ksproperty-cameracontrol-extended-whitebalancemode.md)
-   [**KSPROPERTY\_PIN\_PROPOSEDATAFORMAT2**](./ksproperty-pin-proposedataformat2.md)
-   [**KSPROPERTY\_CAMERACONTROL\_IMAGE\_PIN\_CAPABILITY\_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_image_pin_capability_s) (new **KSPROPERTY\_CAMERACONTROL\_IMAGE\_PIN\_CAPABILITY\_SEQUENCE\_EXCLUSIVE\_WITH\_RECORD** member)
-   [**KSP\_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin) (new **Flags** member)
-   [**KSPROPERTY\_CAMERACONTROL\_REGION\_OF\_INTEREST\_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_region_of_interest_s) (new **Configuration** member)
-   [**KS\_VideoControlFlags**](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-ks_videocontrolflags) (new **KS\_VideoControlFlag\_StartPhotoSequenceCapture** and **KS\_VideoControlFlag\_StopPhotoSequenceCapture** constant values)
-   [**KS\_FRAME\_INFO**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_frame_info) (new **FrameCompletionNumber** member)
-   Note also the additional [KSPROPERTYSETID\_ExtendedCameraControl](./kspropertysetid-extendedcameracontrol.md) property set listed in [Video Capture Minidriver Property Sets](./video-capture-minidriver-property-sets.md).

 

