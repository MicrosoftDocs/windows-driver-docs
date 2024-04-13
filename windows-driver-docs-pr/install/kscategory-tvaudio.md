---
title: KSCATEGORY_TVAUDIO
description: KSCATEGORY_TVAUDIO
keywords: ["KSCATEGORY_TVAUDIO Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSCATEGORY_TVAUDIO
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 10/17/2018
ms.topic: reference
---

# KSCATEGORY_TVAUDIO


The KSCATEGORY_TVAUDIO [device interface class](./overview-of-device-interface-classes.md) is defined for the [kernel streaming](../stream/streaming-minidrivers2.md) (KS) functional category for a TV audio device.

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
<td align="left"><p>KSCATEGORY_TVAUDIO</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{A799A802-A46D-11D0-A18C-00A02401DCD4}</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Drivers for KS devices register instances of this KSCATEGORY_TVAUDIO to indicate to the operating system that the devices support the KSCATEGORY_TVAUDIO functional category.

For an example of how to register this functional category in an INF file, see the *Bdan.inf* INF file that is included with the software tuner sample in the *src/swtuner/algtuner* directory of the WDK.

For information about video devices, see [Video Capture Devices](../stream/video-capture-devices.md), [Filter Graph Examples](../stream/filter-graph-examples.md), and [Encoder Devices](../stream/encoder-devices.md).

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


[**KSCATEGORY_TVTUNER**](kscategory-tvtuner.md)

 

