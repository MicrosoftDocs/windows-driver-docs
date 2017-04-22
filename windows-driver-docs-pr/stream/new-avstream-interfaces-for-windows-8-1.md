---
title: New AVStream Interfaces for Windows 8.1
author: windows-driver-content
description: AVStream streaming media driver interfaces are extended to support new camera platform functionality starting with Windows 8.1.
ms.assetid: 1D06A754-236B-441D-A0BB-A78B419270E9
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# New AVStream Interfaces for Windows 8.1


AVStream streaming media driver interfaces are extended to support new camera platform functionality starting with Windows 8.1.

## Camera platform


Camera controls are extended starting with Windows 8.1. For info on how to implement these camera controls, see the topics under [Camera Control Properties](camera-control-properties.md#win8-1-extended-props).

These device driver interfaces (DDIs) support these extensions and are new or updated:

-   [**KSCAMERA\_EXTENDEDPROP\_CAMERAOFFSET**](https://msdn.microsoft.com/library/windows/hardware/dn567560)
-   [**KSCAMERA\_EXTENDEDPROP\_EVCOMPENSATION**](https://msdn.microsoft.com/library/windows/hardware/dn567561)
-   [**KSCAMERA\_EXTENDEDPROP\_FIELDOFVIEW**](https://msdn.microsoft.com/library/windows/hardware/dn567562)
-   [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563)
-   [**KSCAMERA\_EXTENDEDPROP\_PHOTOMODE**](https://msdn.microsoft.com/library/windows/hardware/dn567564)
-   [**KSCAMERA\_EXTENDEDPROP\_VALUE**](https://msdn.microsoft.com/library/windows/hardware/dn567565)
-   [**KSCAMERA\_EXTENDEDPROP\_VIDEOPROCSETTING**](https://msdn.microsoft.com/library/windows/hardware/dn567566)
-   [**KSCAMERA\_MAXVIDEOFPS\_FORPHOTORES**](https://msdn.microsoft.com/library/windows/hardware/dn567567)
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20New%20AVStream%20Interfaces%20for%20Windows%208.1%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


