---
title: KSCATEGORY_CAPTURE
description: KSCATEGORY_CAPTURE
keywords: ["KSCATEGORY_CAPTURE Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSCATEGORY_CAPTURE
api_location:
- Ks.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# KSCATEGORY_CAPTURE


The KSCATEGORY_CAPTURE [device interface class](./overview-of-device-interface-classes.md) is defined for the [kernel streaming](../stream/streaming-minidrivers2.md) (KS) functional category that captures wave or MIDI data streams.

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
<td align="left"><p>KSCATEGORY_CAPTURE</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{65E8773D-8F56-11D0-A3B9-00A0C9223196}</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Drivers for KS devices register instances of KSCATEGORY_CAPTURE to indicate that the devices support the KSCATEGORY_CAPTURE functional category.

For information about how to register this functional category in an INF file, see the *Ac97smpl.inf* INF file that is included with the [AC'97 sample driver](/samples/browse/) that is provided in the WDK.

For information about device interface classes for audio adapters, see [Installing Device Interfaces for an Audio Adapter](../audio/installing-device-interfaces-for-an-audio-adapter.md).

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

