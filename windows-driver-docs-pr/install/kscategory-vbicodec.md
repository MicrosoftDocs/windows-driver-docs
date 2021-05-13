---
title: KSCATEGORY_VBICODEC
description: KSCATEGORY_VBICODEC
keywords: ["KSCATEGORY_VBICODEC Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSCATEGORY_VBICODEC
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# KSCATEGORY_VBICODEC


The KSCATEGORY_VBICODEC [device interface class](./overview-of-device-interface-classes.md) is defined for the [kernel streaming](../stream/streaming-minidrivers2.md) (KS) functional category for a video blanking interval (VBI) codec device.

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
<td align="left"><p>KSCATEGORY_VBICODEC</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{07DAD660-22F1-11D1-A9F4-00C04FBBDE8F}</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Drivers for KS devices register instances of KSCATEGORY_VBICODEC to indicate to the operating system that the devices support the KSCATEGORY_VBICODEC functional category.

For general information about video devices, see [Video Capture Devices](../stream/video-capture-devices.md).

For more information about video blanking, see [Streaming Data from a Video Capture Device](../stream/streaming-data-from-a-video-capture-device.md) and [VBI Category](../stream/vbi-category.md).

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


[**KSCATEGORY_VIDEO**](kscategory-video.md)

 

