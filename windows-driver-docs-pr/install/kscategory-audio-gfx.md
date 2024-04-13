---
title: KSCATEGORY_AUDIO_GFX
description: KSCATEGORY_AUDIO_GFX
keywords: ["KSCATEGORY_AUDIO_GFX Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSCATEGORY_AUDIO_GFX
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 10/17/2018
ms.topic: reference
---

# KSCATEGORY_AUDIO_GFX


The KSCATEGORY_AUDIO_GFX [device interface class](./overview-of-device-interface-classes.md) is defined for the [kernel streaming](../stream/streaming-minidrivers2.md) (KS) functional category that supports a [global effects (GFX) filter](../audio/index.md).

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
<td align="left"><p>KSCATEGORY_AUDIO_GFX</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{9BAF9572-340C-11D3-ABDC-00A0C90AB16F}</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Drivers for KS audio adapter devices register instances of KSCATEGORY_AUDIO_GFX to indicate to the operating system that the devices support the KSCATEGORY_AUDIO_GFX functional category.

For information about other device interface classes for audio adapters, see [Installing Device Interfaces for an Audio Adapter](../audio/installing-device-interfaces-for-an-audio-adapter.md).

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows Server 2003, Windows XP, and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

 

