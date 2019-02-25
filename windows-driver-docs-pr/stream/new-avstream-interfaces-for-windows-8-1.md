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

-   [**KSCAMERA\_EXTENDEDPROP\_CAMERAOFFSET**](https://msdn.microsoft.com/library/windows/hardware/dn567560)
-   [**KSCAMERA\_EXTENDEDPROP\_EVCOMPENSATION**](https://msdn.microsoft.com/library/windows/hardware/dn567561)
-   [**KSCAMERA\_EXTENDEDPROP\_FIELDOFVIEW**](https://msdn.microsoft.com/library/windows/hardware/dn567562)
-   [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header)
-   [**KSCAMERA\_EXTENDEDPROP\_PHOTOMODE**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_photomode)
-   [**KSCAMERA\_EXTENDEDPROP\_VALUE**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_value)
-   [**KSCAMERA\_EXTENDEDPROP\_VIDEOPROCSETTING**](https://msdn.microsoft.com/library/windows/hardware/dn567566)
-   [**KSCAMERA\_MAXVIDEOFPS\_FORPHOTORES**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_maxvideofps_forphotores)
-   [KSEVENTSETID\_VolumeLimit](https://msdn.microsoft.com/library/windows/hardware/dn567568)
-   [**KSEVENT\_VOLUMELIMIT\_CHANGED**](https://msdn.microsoft.com/library/windows/hardware/dn567569)
-   [KSPROPERTYSETID\_ExtendedCameraControl](https://msdn.microsoft.com/library/windows/hardware/dn567570) (includes these properties:)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_CAMERAANGLEOFFSET**](https://msdn.microsoft.com/library/windows/hardware/dn567571)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_EVCOMPENSATION**](https://msdn.microsoft.com/library/windows/hardware/dn567572)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_EXPOSUREMODE**](https://msdn.microsoft.com/library/windows/hardware/dn567573)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FIELDOFVIEW**](https://msdn.microsoft.com/library/windows/hardware/dn567574)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FLASHMODE**](https://msdn.microsoft.com/library/windows/hardware/dn567575)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FOCUSMODE**](https://msdn.microsoft.com/library/windows/hardware/dn567576)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ISO**](https://msdn.microsoft.com/library/windows/hardware/dn567577)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_MAXVIDFPS\_PHOTORES**](https://msdn.microsoft.com/library/windows/hardware/dn567578)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_OPTIMIZATIONHINT**](https://msdn.microsoft.com/library/windows/hardware/dn567579)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOFRAMERATE**](https://msdn.microsoft.com/library/windows/hardware/dn567580)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOMAXFRAMERATE**](https://msdn.microsoft.com/library/windows/hardware/dn567581)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOMODE**](https://msdn.microsoft.com/library/windows/hardware/dn567582)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOTHUMBNAIL**](https://msdn.microsoft.com/library/windows/hardware/dn567583)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOTRIGGERTIME**](https://msdn.microsoft.com/library/windows/hardware/dn567584)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_SCENEMODE**](https://msdn.microsoft.com/library/windows/hardware/dn567585)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_TORCHMODE**](https://msdn.microsoft.com/library/windows/hardware/dn567586)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_WARMSTART**](https://msdn.microsoft.com/library/windows/hardware/dn567587)
    -   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_WHITEBALANCEMODE**](https://msdn.microsoft.com/library/windows/hardware/dn567588)
-   [**KSPROPERTY\_PIN\_PROPOSEDATAFORMAT2**](https://msdn.microsoft.com/library/windows/hardware/dn567589)
-   [**KSPROPERTY\_CAMERACONTROL\_IMAGE\_PIN\_CAPABILITY\_S**](https://msdn.microsoft.com/library/windows/hardware/jj553707) (new **KSPROPERTY\_CAMERACONTROL\_IMAGE\_PIN\_CAPABILITY\_SEQUENCE\_EXCLUSIVE\_WITH\_RECORD** member)
-   [**KSP\_PIN**](https://msdn.microsoft.com/library/windows/hardware/ff566722) (new **Flags** member)
-   [**KSPROPERTY\_CAMERACONTROL\_REGION\_OF\_INTEREST\_S**](https://msdn.microsoft.com/library/windows/hardware/jj151592) (new **Configuration** member)
-   [**KS\_VideoControlFlags**](https://msdn.microsoft.com/library/windows/hardware/ff567696) (new **KS\_VideoControlFlag\_StartPhotoSequenceCapture** and **KS\_VideoControlFlag\_StopPhotoSequenceCapture** constant values)
-   [**KS\_FRAME\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567645) (new **FrameCompletionNumber** member)
-   Note also the additional [KSPROPERTYSETID\_ExtendedCameraControl](https://msdn.microsoft.com/library/windows/hardware/dn567570) property set listed in [Video Capture Minidriver Property Sets](https://msdn.microsoft.com/library/windows/hardware/ff568714).

 

 




