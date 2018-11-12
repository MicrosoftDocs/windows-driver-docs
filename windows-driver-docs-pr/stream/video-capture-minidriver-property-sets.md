---
title: Video Capture Minidriver Property Sets
description: Video Capture Minidriver Property Sets
ms.assetid: adbf62c4-1c66-46e9-ae8e-867a88bb107c
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Video Capture Minidriver Property Sets


## <span id="ddk_video_capture_minidriver_property_sets_ks"></span><span id="DDK_VIDEO_CAPTURE_MINIDRIVER_PROPERTY_SETS_KS"></span>


This section describes the video capture-specific property sets that are available for video capture minidrivers that use WDM kernel-streaming services in Microsoft Windows XP, Windows 2000, and Windows 98/Me and later operating systems.

The reference page for each property contains a table with the following column headings.


| Get | Set | Target | Property descriptor type | Property value type |
|-----|-----|--------|--------------------------|---------------------|
|     |     |        |                          |                     |

These headings have the following meanings:

-   **Get**

    Does the target KS object support the KSPROPERTY\_TYPE\_GET property request?

-   **Set**

    Does the target KS object support the KSPROPERTY\_TYPE\_SET property request?

-   **Target**

    The target is the KS object to which property request is sent. The target for a video capture property is either a filter or a pin. (The property request specifies the target object by its kernel handle.)

-   **Property descriptor type**

    The property descriptor specifies the property and the operation to perform on that property. The descriptor always begins with a [**KSPROPERTY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier) structure, but some types of descriptor contain additional information. For example, the [**KSNODEPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff537143) structure is a property descriptor that begins with a KSPROPERTY structure but also includes a node identifier.

-   **Property value type**

    A property has a value and the type of this value depends on the property. For example, a property that can be in one of only two states--on or off--typically has a BOOL value. A property that can assume integer values from 0x0 to 0xFFFFFFFF might have a ULONG value. More complex properties might have values that are arrays or structures.

The property descriptor and property value above are the property-specific versions of the instance-specification and operation-data buffers that [KS Properties, Events, and Methods](https://msdn.microsoft.com/library/windows/hardware/ff567673) discusses.

A property request uses one of the following flags to specify the operation to be performed on the property:

-   KSPROPERTY\_TYPE\_BASICSUPPORT

-   KSPROPERTY\_TYPE\_GET

-   KSPROPERTY\_TYPE\_SET

All filter and pin objects support the basic-support operation on their properties. Whether they support the *get* and *Set* operations depends on the property. A property that represents an inherent capability of the filter or pin object is likely to require only a get operation. A property that represents a configurable setting might require only a *Set* operation, although a get operation might also be useful for reading the current setting. For more information about using the get, set, and basic-support operations with video capture properties, see [KS Properties](https://msdn.microsoft.com/library/windows/hardware/ff567671).

Every property description contains a table that indicates whether video capture minidrivers must support reading or writing the property. Video capture minidrivers should return STATUS\_NOT\_SUPPORTED in response to get or set requests for properties that are not supported by the minidriver.

The following list describes kernel streaming property sets that video capture minidrivers use:

[PROPSETID\_ALLOCATOR\_CONTROL](propsetid-allocator-control.md)

[PROPSETID\_EXT\_DEVICE](propsetid-ext-device.md)

[PROPSETID\_EXT\_TRANSPORT](propsetid-ext-transport.md)

[PROPSETID\_TIMECODE\_READER](propsetid-timecode-reader.md)

[PROPSETID\_TUNER](propsetid-tuner.md)

[PROPSETID\_VIDCAP\_CAMERACONTROL](propsetid-vidcap-cameracontrol.md)

[KSPROPERTYSETID\_ExtendedCameraControl](kspropertysetid-extendedcameracontrol.md)

[PROPSETID\_VIDCAP\_CROSSBAR](propsetid-vidcap-crossbar.md)

[PROPSETID\_VIDCAP\_DROPPEDFRAMES](propsetid-vidcap-droppedframes.md)

[PROPSETID\_VIDCAP\_TVAUDIO](propsetid-vidcap-tvaudio.md)

[PROPSETID\_VIDCAP\_VIDEOCOMPRESSION](propsetid-vidcap-videocompression.md)

[PROPSETID\_VIDCAP\_VIDEOCONTROL](propsetid-vidcap-videocontrol.md)

[PROPSETID\_VIDCAP\_VIDEODECODER](propsetid-vidcap-videodecoder.md)

[PROPSETID\_VIDCAP\_VIDEOPROCAMP](propsetid-vidcap-videoprocamp.md)

The following property sets can be used with the [USB Video Class Driver](https://msdn.microsoft.com/library/windows/hardware/ff568649):

[PROPSETID\_VIDCAP\_CAMERACONTROL](propsetid-vidcap-cameracontrol.md)

[KSPROPERTYSETID\_ExtendedCameraControl](kspropertysetid-extendedcameracontrol.md)

[PROPSETID\_VIDCAP\_VIDEOPROCAMP](propsetid-vidcap-videoprocamp.md)

[PROPSETID\_VIDCAP\_SELECTOR](propsetid-vidcap-selector.md)

 

 





