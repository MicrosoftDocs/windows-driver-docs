---
title: KSCATEGORY_VIDEO
description: KSCATEGORY_VIDEO
keywords: ["KSCATEGORY_VIDEO Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSCATEGORY_VIDEO
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 10/17/2018
ms.topic: reference
---

# KSCATEGORY_VIDEO


The KSCATEGORY_VIDEO [device interface class](./overview-of-device-interface-classes.md) is defined for the [kernel streaming](../stream/streaming-minidrivers2.md) (KS) functional category for a video device.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Attribute</th>
<th align="left">Setting</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Identifier</p></td>
<td align="left"><p>KSCATEGORY_VIDEO</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{6994AD05-93EF-11D0-A3CC-00A0C9223196}</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Drivers for KS video devices register instances of KSCATEGORY_VIDEO to indicate to the operating system that the devices support the KSCATEGORY_VIDEO functional category.

For an example of how to register this functional category in an INF file, see the *Bdan.inf* INF file that is included with the software tuner sample in the *src/swtuner/algtuner* directory of the WDK.

For more information about this functional category, see [Providing a UVC INF File](../stream/providing-a-uvc-inf-file.md).

For general information about video devices, see [Video Capture Devices](../stream/video-capture-devices.md).

For information about other device interface classes for video devices, see [**KSCATEGORY_TVAUDIO**](kscategory-tvaudio.md) and [**KSCATEGORY_TVTUNER**](kscategory-tvtuner.md).

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## See also


[**KSCATEGORY_TVAUDIO**](kscategory-tvaudio.md)

[**KSCATEGORY_TVTUNER**](kscategory-tvtuner.md)

 

