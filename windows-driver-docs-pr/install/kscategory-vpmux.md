---
title: KSCATEGORY_VPMUX
description: KSCATEGORY_VPMUX
keywords: ["KSCATEGORY_VPMUX Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSCATEGORY_VPMUX
api_location:
- Ks.h
api_type:
- HeaderDef
ms.date: 10/17/2018
ms.topic: reference
---

# KSCATEGORY_VPMUX


The KSCATEGORY_VPMUX [device interface class](./overview-of-device-interface-classes.md) is defined for the [kernel streaming](../stream/streaming-minidrivers2.md) (KS) functional category that supports video multiplexing.

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
<td align="left"><p>KSCATEGORY_VPMUX</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{A799A803-A46D-11D0-A18C-00A02401DCD4}</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Drivers for KS devices register instances of KSCATEGORY_VPMUX to indicate to the operating system that the devices support the KSCATEGORY_VPMUX functional category.

For general information about video devices, see [Video Capture Devices](../stream/video-capture-devices.md).

For information about the device interface class for video devices, see [**KSCATEGORY_VIDEO**](kscategory-video.md).

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ks.h (include Ks.h)</td>
</tr>
</tbody>
</table>

## See also


[**KSCATEGORY_VIDEO**](kscategory-video.md)

 

