---
title: Video Capture Property Sets
description: Video Capture Property Sets
keywords:
- video capture WDK AVStream , property sets
- capturing video WDK AVStream , property sets
- property sets WDK video capture
- hardware property sets WDK video capture
- stream property sets WDK video capture
- ranges WDK video capture
- default video capture property sets WDK AVStream
- capture property sets WDK video capture
ms.date: 06/11/2018
ms.localizationpriority: medium
---

# Video Capture Property Sets

Video capture property sets group related properties of devices and streams. Whenever possible, minidrivers should implement the standard property sets defined in the *ksmedia.h* header file, such as [KSPROPSETID\_Pin](kspropsetid-pin.md) and [PROPSETID\_ALLOCATOR\_CONTROL](propsetid-allocator-control.md). Minidrivers should avoid defining new property sets if one of the standard property sets provides the same functionality.

User-mode applications typically call COM interfaces to control property settings. The COM interface then sends and receives stream and adapter property sets to the minidriver through the Win32 **DeviceIoControl** API. The reference page for each property set describes the COM interface that user-mode applications call to control the kernel streaming properties of that set.

Depending on which kernel streaming interface a minidriver uses (AVStream or the Stream class), the minidriver specifies the video capture property sets that it supports differently. For example, if a minidriver uses the AVStream interface, then it specifies its properties in a recursive hierarchy encapsulated in a [**KSPROPERTY\_SET**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_set) structure. If the minidriver uses the Stream class interface, then it specifies its properties in an [**HW\_STREAM\_HEADER**](/windows-hardware/drivers/ddi/strmini/ns-strmini-_hw_stream_header) structure. Microsoft defines several macros that driver developers can use to specify the properties that their minidriver supports, regardless of which kernel streaming interface their minidriver uses.

For more information about how to support properties and property sets if your minidriver uses the AVStream interface, see the [AVStream Filter-Centric Simulated Capture Driver (Avssamp)](/samples/microsoft/windows-driver-samples/avstream-filter-centric-simulated-capture-sample-driver-avssamp/) and [AVStream Simulated Hardware Sample Driver (AVSHwS)](/samples/microsoft/windows-driver-samples/avstream-simulated-hardware-sample-driver-avshws/) sample minidrivers in the Windows driver samples repo on GitHub.

For more information about how to support properties and property sets if your minidriver uses the Stream Class interface, see [Supporting Property Sets](supporting-property-sets.md).

## Hardware and stream property sets

Property sets are classified as belonging to either the hardware or to a specific stream. Hardware property sets apply to all devices and affect all streams. For example, [PROPSETID\_VIDCAP\_CAMERACONTROL](propsetid-vidcap-cameracontrol.md), which is used for camera positioning, affects all output streams and is therefore classified as a hardware property set. Note that some property sets, such as [PROPSETID\_VIDCAP\_VIDEOCOMPRESSION](propsetid-vidcap-videocompression.md), which controls the compression behavior of a single output stream, are implemented as a hardware property set that include an index to a specific stream. This method is required because stream property sets are unavailable when the pin is not connected. Hardware property sets are always available.

The following table lists the primary property sets used by video capture minidrivers. It also indicates whether the property set affects video capture hardware, or individual video capture streams. The list also indicates whether minidrivers are required to implement the property set.

| Property set | Hardware property set | Video capture property set | Required |
| --- | --- | --- | --- |
| [PROPSETID_ALLOCATOR_CONTROL](propsetid-allocator-control.md) |  | Y |  |
| [PROPSETID_TUNER](propsetid-tuner.md) | Y |  |  |
| [PROPSETID_VIDCAP_CAMERACONTROL](propsetid-vidcap-cameracontrol.md) | Y |  |  |
| [PROPSETID_VIDCAP_CROSSBAR](propsetid-vidcap-crossbar.md) | Y |  |  |
| [PROPSETID_VIDCAP_DROPPEDFRAMES](propsetid-vidcap-droppedframes.md) |  | Y | Y |
| [PROPSETID_VIDCAP_TVAUDIO](propsetid-vidcap-tvaudio.md) | Y |  |  |
| [PROPSETID_VIDCAP_VIDEOCOMPRESSION](propsetid-vidcap-videocompression.md) | Y |  |  |
| [PROPSETID_VIDCAP_VIDEOCONTROL](propsetid-vidcap-videocontrol.md) | Y |  |  |
| [PROPSETID_VIDCAP_VIDEODECODER](propsetid-vidcap-videodecoder.md) | Y |  |  |
| [PROPSETID_VIDCAP_VIDEOPROCAMP](propsetid-vidcap-videoprocamp.md) | Y |  |  |

At a minimum, a minidriver must report the number of frames dropped during capture as noted in the table above. Support for all other property sets is optional, depending on the capabilities of the device. It is strongly recommended that cameras, which offer only a limited set of capture frame rates, implement the [PROPSETID\_VIDCAP\_VIDEOCONTROL](propsetid-vidcap-videocontrol.md) to allow video conferencing applications to make optimal use of system bandwidth.

## Property set default values and ranges

Properties can support default values and ranges. User-interface elements, such as sliders and scrollbars, use this information, as shown in the following image.

![screen shot of a properties dialog box showing how user-interface elements, such as sliders and scrollbars, use default values and ranges.](images/vcuiprop.gif)

The default value and range information is provided in a [**KSPROPERTY\_VALUES**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_values) structure that is part of a property definition. This structure includes a pointer to a static table that consists of one or more [**KSPROPERTY\_MEMBERSLIST**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_memberslist) structure instances. Within the KSPROPERTY\_MEMBERSLIST structure, the minidriver can specify either a default value or a range of values. A range of values can be specified through the minimum, maximum, and stepping value. Set the **MembersFlags** member of the [**KSPROPERTY\_MEMBERSHEADER**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_membersheader) structure to the KSPROPERTY\_MEMBER\_RANGES value to indicate that the KSPROPERTY\_MEMBERSLIST structure is a range of values. A KSPROPERTY\_MEMBERSLIST structure is also used to specify a default value for the property. This is done by setting the **MembersFlags** member of the KSPROPERTY\_MEMBERSHEADER to the KSPROPERTY\_MEMBER\_VALUE value.
