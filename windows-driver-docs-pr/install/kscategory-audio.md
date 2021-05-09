---
title: KSCATEGORY_AUDIO
description: KSCATEGORY_AUDIO
keywords: ["KSCATEGORY_AUDIO Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSCATEGORY_AUDIO
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# KSCATEGORY_AUDIO


The KSCATEGORY_AUDIO [device interface class](./overview-of-device-interface-classes.md) is defined for the [kernel streaming](../stream/streaming-minidrivers2.md) (KS) functional category for an audio device.

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
<td align="left"><p>KSCATEGORY_AUDIO</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{6994AD04-93EF-11D0-A3CC-00A0C9223196}</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Drivers for KS audio devices register instances of this device interface class to indicate to the operating system that the devices support the KSCATEGORY_AUDIO functional category.

For information about device interface classes for audio adapters, see [Installing Device Interfaces for an Audio Adapter](../audio/installing-device-interfaces-for-an-audio-adapter.md).

For information about how to register this functional category in an INF file, see the Help files *INFViewer.html* and *ac97smpl.inf*, which are included with the [AC'97 sample driver](/samples/browse/) in the WDK.

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

